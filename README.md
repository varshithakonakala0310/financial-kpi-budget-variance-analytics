# Financial KPI & Budget Variance Analytics

## Business problem

Finance teams need a fast, repeatable view of budget vs actual spending by department and month, with clear flags where variance needs attention.

## Questions

1. Which departments are over or under budget, and by how much?
2. How many department-months breach a ±10% KPI threshold?
3. What is the overall business variance?

## Dataset

**Synthetic data only** — generated in `analysis.py` with a fixed seed (42): 6 departments × 12 months of 2024 (72 rows). Saved to `data/budget_vs_actual_synthetic.csv`.

## Method

- Variance (£ and %) per department-month in pandas and SQL (`sql/analysis.sql`)
- KPI flags: `OVER_BUDGET` (> +10%), `UNDER_BUDGET` (< −10%), otherwise `ON_TRACK`

## Key findings (actual run results)

From `results/results_summary.txt`:

- Total budget **£13,043,574.49** vs total actual **£12,866,123.04** — overall variance **−1.36%**
- KPI flags: **OVER_BUDGET = 10, UNDER_BUDGET = 18, ON_TRACK = 44** (of 72 department-months)
- Largest absolute department variance: **Operations, −5.22%** (budget £2,886,744.23, actual £2,735,992.25)
- Other departments: Sales +2.19%, Marketing +1.86%, HR +0.62%, Finance −1.79%, IT −4.00%

## Tech stack

Python · pandas · NumPy · SQL

## How to run

```bash
pip install -r requirements.txt
python3 analysis.py
```

## Repository structure

```
├── analysis.py
├── data/
├── sql/analysis.sql
├── results/results_summary.txt
├── requirements.txt
└── LICENSE
```

## License

MIT — see `LICENSE`. Copyright (c) 2026 Varshitha Konakala.
