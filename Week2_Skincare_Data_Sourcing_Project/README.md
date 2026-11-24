# Week 2 – Skincare Data Identification, Sourcing Strategy & Initial Analysis

**Intern:** Adarsh Kumar  
**Organization:** YuvaIntern  
**Project theme:** Beauty & Wellness – Skincare Customer Preference & Product Review Analysis

## What this project does
This ready-to-run Python project documents candidate public data sources, assesses their suitability, validates a skincare dataset, produces a data-quality report, prepares initial descriptive summaries, and exports charts.

## Run in VS Code
1. Extract/open this folder in VS Code.
2. Open Terminal → New Terminal.
3. Create a virtual environment (optional but recommended):
   ```bash
   python -m venv .venv
   ```
4. Activate it on Windows:
   ```bash
   .venv\Scripts\activate
   ```
5. Install packages:
   ```bash
   pip install -r requirements.txt
   ```
6. Run:
   ```bash
   python analysis.py
   ```
   Or double-click `run_project.bat` on Windows.

## Output files
The program creates these inside `outputs/`:
- `cleaned_skincare_data.csv`
- `missing_value_report.csv`
- `data_quality_summary.csv`
- `overall_metrics.json`
- `skin_type_summary.csv`
- `skin_concern_summary.csv`
- `figures/average_rating_by_skin_type.png`
- `figures/records_by_skin_concern.png`
- `figures/price_distribution.png`

## Data source strategy
See `data/data_source_catalog.csv` and `docs/data_sourcing_strategy.md`.
Open Beauty Facts is a strong source for cosmetic product and ingredient metadata, but it does **not** provide customer-review ratings in the same way a review dataset does. Kaggle and Google Dataset Search are discovery routes only; each original dataset's provenance and licence must be checked before reuse.

## Important data limitation
The included `data/sample_skincare_reviews.csv` is a **synthetic/demo dataset** created so the project runs immediately without extra downloads. It is not real customer data and must not be used to make market, medical, or product-safety claims. Replace it with a properly licensed public dataset before drawing real-world conclusions. Keep the same column names or update `REQUIRED_COLUMNS` in `analysis.py`.

## GitHub
Create a new GitHub repository, then upload the complete project folder. Do not upload `.venv/` or temporary cache files. The `.gitignore` file already excludes common local files.
