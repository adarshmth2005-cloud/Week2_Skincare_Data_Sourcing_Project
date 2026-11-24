"""
Week 2 - Data Identification, Sourcing Strategy & Initial Analysis Planning
Project: Skincare Customer Preference & Product Review Analysis

Run from the project root:
    python analysis.py

The included CSV is a small synthetic/demo dataset to make this project runnable
immediately. It is NOT real customer research and must not be presented as such.
Replace it with a properly licensed dataset after checking its source and licence.
"""
from pathlib import Path
import json
import pandas as pd
import matplotlib.pyplot as plt

ROOT = Path(__file__).resolve().parent
DATA_FILE = ROOT / "data" / "sample_skincare_reviews.csv"
OUTPUT_DIR = ROOT / "outputs"
FIGURE_DIR = OUTPUT_DIR / "figures"
REQUIRED_COLUMNS = [
    "product_name", "skin_type", "skin_concern", "price_inr",
    "rating", "is_recommended", "ingredients"
]

def load_data(path: Path) -> pd.DataFrame:
    if not path.exists():
        raise FileNotFoundError(
            f"Dataset not found: {path}\nPlace sample_skincare_reviews.csv in the data folder."
        )
    data = pd.read_csv(path)
    missing_columns = [c for c in REQUIRED_COLUMNS if c not in data.columns]
    if missing_columns:
        raise ValueError(f"Missing required columns: {missing_columns}")
    return data

def clean_data(raw: pd.DataFrame) -> pd.DataFrame:
    data = raw.copy()
    for col in ["product_name", "skin_type", "skin_concern", "ingredients"]:
        data[col] = data[col].astype("string").str.strip()
        data[col] = data[col].replace("", pd.NA)
    for col in ["price_inr", "rating", "is_recommended"]:
        data[col] = pd.to_numeric(data[col], errors="coerce")
    data = data.drop_duplicates()
    data = data.dropna(subset=["product_name", "skin_type", "rating"])
    data = data[data["rating"].between(1, 5)]
    data.loc[~data["is_recommended"].isin([0, 1]), "is_recommended"] = pd.NA
    data.loc[data["price_inr"] <= 0, "price_inr"] = pd.NA
    return data

def save_quality_outputs(raw: pd.DataFrame, clean: pd.DataFrame) -> None:
    missing = raw.isna().sum().rename("missing_count").to_frame()
    missing["missing_percent"] = (missing["missing_count"] / max(len(raw), 1) * 100).round(2)
    missing.to_csv(OUTPUT_DIR / "missing_value_report.csv")
    profile = pd.DataFrame({
        "metric": ["source_rows", "source_columns", "duplicate_rows",
                   "cleaned_rows", "removed_rows", "missing_cells_after_cleaning"],
        "value": [len(raw), len(raw.columns), int(raw.duplicated().sum()),
                  len(clean), len(raw) - len(clean), int(clean.isna().sum().sum())]
    })
    profile.to_csv(OUTPUT_DIR / "data_quality_summary.csv", index=False)
    clean.to_csv(OUTPUT_DIR / "cleaned_skincare_data.csv", index=False)

def create_analysis(clean: pd.DataFrame) -> dict:
    OUTPUT_DIR.mkdir(exist_ok=True)
    FIGURE_DIR.mkdir(parents=True, exist_ok=True)

    overall = {
        "records_analyzed": int(len(clean)),
        "unique_products": int(clean["product_name"].nunique()),
        "skin_type_categories": int(clean["skin_type"].nunique()),
        "skin_concern_categories": int(clean["skin_concern"].nunique()),
        "average_rating": round(float(clean["rating"].mean()), 2) if len(clean) else None,
        "median_rating": round(float(clean["rating"].median()), 2) if len(clean) else None,
        "average_price_inr": round(float(clean["price_inr"].mean()), 2) if clean["price_inr"].notna().any() else None,
        "recommendation_rate_percent": round(float(clean["is_recommended"].mean() * 100), 2) if clean["is_recommended"].notna().any() else None,
    }
    (OUTPUT_DIR / "overall_metrics.json").write_text(json.dumps(overall, indent=4), encoding="utf-8")

    by_skin = clean.groupby("skin_type", dropna=False).agg(
        record_count=("product_name", "size"),
        average_rating=("rating", "mean"),
        average_price_inr=("price_inr", "mean"),
        recommendation_rate=("is_recommended", "mean")
    ).reset_index()
    by_skin["average_rating"] = by_skin["average_rating"].round(2)
    by_skin["average_price_inr"] = by_skin["average_price_inr"].round(2)
    by_skin["recommendation_rate_percent"] = (by_skin.pop("recommendation_rate") * 100).round(2)
    by_skin.to_csv(OUTPUT_DIR / "skin_type_summary.csv", index=False)

    concerns = clean["skin_concern"].value_counts(dropna=False).rename_axis("skin_concern").reset_index(name="record_count")
    concerns.to_csv(OUTPUT_DIR / "skin_concern_summary.csv", index=False)

    # Figure 1: average rating by skin type
    if not by_skin.empty:
        plt.figure(figsize=(9, 5))
        plt.bar(by_skin["skin_type"], by_skin["average_rating"])
        plt.title("Average Product Rating by Skin Type")
        plt.xlabel("Skin Type")
        plt.ylabel("Average Rating (1-5)")
        plt.ylim(0, 5)
        plt.xticks(rotation=20, ha="right")
        plt.tight_layout()
        plt.savefig(FIGURE_DIR / "average_rating_by_skin_type.png", dpi=160)
        plt.close()

    # Figure 2: frequency of recorded skin concerns
    if not concerns.empty:
        plt.figure(figsize=(9, 5))
        plt.bar(concerns["skin_concern"].astype(str), concerns["record_count"])
        plt.title("Records by Skin Concern")
        plt.xlabel("Skin Concern")
        plt.ylabel("Number of Records")
        plt.xticks(rotation=25, ha="right")
        plt.tight_layout()
        plt.savefig(FIGURE_DIR / "records_by_skin_concern.png", dpi=160)
        plt.close()

    # Figure 3: price distribution
    prices = clean["price_inr"].dropna()
    if not prices.empty:
        plt.figure(figsize=(9, 5))
        plt.hist(prices, bins=min(8, max(3, prices.nunique())))
        plt.title("Skincare Product Price Distribution")
        plt.xlabel("Listed Price (INR)")
        plt.ylabel("Frequency")
        plt.tight_layout()
        plt.savefig(FIGURE_DIR / "price_distribution.png", dpi=160)
        plt.close()

    return overall

def main():
    print("=" * 68)
    print("WEEK 2 | DATA IDENTIFICATION, SOURCING STRATEGY & INITIAL ANALYSIS")
    print("=" * 68)
    raw = load_data(DATA_FILE)
    clean = clean_data(raw)
    save_quality_outputs(raw, clean)
    metrics = create_analysis(clean)

    print(f"\nDataset loaded successfully: {DATA_FILE.name}")
    print(f"Original shape: {raw.shape[0]} rows x {raw.shape[1]} columns")
    print(f"Rows retained after validation: {len(clean)}")
    print(f"Rows removed: {len(raw) - len(clean)}")
    print("\nINITIAL DESCRIPTIVE METRICS")
    for key, value in metrics.items():
        print(f"{key.replace('_', ' ').title():32}: {value}")
    print("\nFILES GENERATED")
    for path in sorted(OUTPUT_DIR.rglob("*")):
        if path.is_file():
            print(f"- {path.relative_to(ROOT)}")
    print("\nIMPORTANT DATA NOTE:")
    print("The bundled dataset is synthetic/demo data. Findings are illustrative only.")
    print("Use a verified, licensed public dataset for real-world business conclusions.")
    print("\nAnalysis completed successfully.")

if __name__ == "__main__":
    main()
