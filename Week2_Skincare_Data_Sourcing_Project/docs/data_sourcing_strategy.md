# Data Sourcing Strategy – Week 2

## 1. Business problem carried forward
The Week 1 project explored how recorded skincare product ratings and recommendation flags vary across skin types and skin concerns, while summarising listed product prices. Week 2 defines a repeatable strategy for identifying stronger, documented data sources and planning initial analysis.

## 2. Data requirements
| Data domain | Required fields | Why it matters | Priority |
|---|---|---|---|
| Product identity | product name, brand, barcode, category | Identify and de-duplicate products | High |
| Ingredients | ingredient list, ingredient labels | Describe product formulation metadata | High |
| Customer feedback | rating, review text, review date | Study satisfaction and sentiment | High |
| Customer/product segment | skin type, skin concern, product category | Compare descriptive patterns between groups | Medium |
| Price | listed price, currency, capture date | Explore price distribution and group differences | Medium |
| Provenance | source URL, publisher, licence, retrieval date | Reproducibility and lawful reuse | High |

## 3. Candidate sources and suitability
The machine-readable source register is stored in `data/data_source_catalog.csv`.

- **Open Beauty Facts:** suitable for cosmetic product metadata, ingredients, categories and labels. It is community-contributed, so missingness and accuracy must be checked. It is not a customer-review ratings source. Its database is published under ODbL; attribution and share-alike obligations must be followed.
- **Open Beauty Facts API documentation:** useful for structured product lookup and reproducible collection. API behaviour and field availability may change, so record retrieval date and endpoint.
- **Kaggle:** useful for discovering review datasets, but each dataset has its own provenance and licence. Do not assume a dataset is reusable merely because it is downloadable.
- **Google Dataset Search:** a discovery index, not the original publisher. Always open the original host and verify its documentation and licence.

## 4. Collection approach
1. Search for datasets that contain product identifiers, rating/review fields and dates.
2. Prefer publisher-hosted downloads or documented APIs over copied spreadsheets.
3. Record source name, URL, access date, licence, dataset version and field definitions.
4. Download only fields needed for the stated business problem.
5. Preserve an unchanged raw copy; perform cleaning on a separate working copy.
6. Check duplicate products/reviews, missingness, invalid rating ranges, inconsistent categories and stale prices.
7. Retain source-level provenance so every row can be traced to its origin where permitted.

## 5. Data quality and relevance assessment
Assess completeness, validity, uniqueness, consistency, timeliness, accuracy/provenance, representativeness and licence/access conditions. Open Beauty Facts is relevant for product/ingredient enrichment, while a separate licensed review dataset is required for customer ratings and review text. Product metadata must not be treated as customer sentiment.

## 6. Initial exploratory analysis plan
- Descriptive statistics: count, mean, median, standard deviation, minimum and maximum for numeric fields.
- Frequency analysis: skin type, skin concern, product category and recommendation flag.
- Group comparisons: average rating and recommendation rate by skin type, subject to sufficient sample size.
- Visualisation: rating distribution, concern counts, price histogram and average rating by skin type.
- Data-quality outputs: missing-value percentages, duplicate counts, invalid-value checks and cleaned-row counts.

## 7. Hypothesis alignment
The planned dataset can support descriptive checks of whether rating and recommendation patterns differ across recorded skin-type groups. These are exploratory comparisons, not causal tests. A sufficiently large, representative, independently collected review sample would be required before drawing business conclusions.

## 8. Risks and limitations
- Public product databases may have incomplete or user-submitted fields.
- Review datasets may be biased toward people who choose to post reviews.
- Skin type and skin concern labels may be self-reported or inconsistently defined.
- Price changes over time and across regions; currency and capture date are essential.
- Licences differ by source and must be checked before redistribution.
- Small demo data cannot support population-level inference.

## 9. Decision
Use Open Beauty Facts as the preferred source for product and ingredient metadata. Identify a separate, clearly licensed review dataset for rating and review analysis. The bundled CSV is synthetic/demo data used only to make the code executable and demonstrate the profiling workflow.
