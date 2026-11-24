# Initial Analysis Plan – Week 2

| Analysis | Variables | Method | Expected output |
|---|---|---|---|
| Dataset structure | all columns | shape, dtypes, unique counts | dataset profile |
| Missingness | all columns | null count and percentage | missing_value_report.csv |
| Duplicate check | all columns | exact duplicate count | data_quality_summary.csv |
| Rating distribution | rating | mean, median, range, histogram (future extension) | descriptive metrics |
| Skin type comparison | skin_type, rating, price_inr, is_recommended | groupby summaries | skin_type_summary.csv and chart |
| Concern frequency | skin_concern | value counts | skin_concern_summary.csv and chart |
| Price distribution | price_inr | histogram, mean and median | price chart and metrics |

## Cleaning rules
- Convert rating, price and recommendation fields to numeric values.
- Remove exact duplicate rows.
- Exclude rows without product name, skin type or rating.
- Keep ratings only in the 1–5 range.
- Treat recommendation values outside 0/1 as missing.
- Treat non-positive prices as missing rather than silently correcting them.

## Interpretation rule
All outputs describe only the file supplied to the program. If the bundled demo file is used, every result must be described as illustrative synthetic data.
