-- Financial KPI Budget Variance — SQL
-- Table: budget_vs_actual_synthetic

-- Department variance summary
SELECT department, ROUND(SUM(budget_gbp),2) AS budget, ROUND(SUM(actual_gbp),2) AS actual,
       ROUND((SUM(actual_gbp)-SUM(budget_gbp))/SUM(budget_gbp)*100,2) AS variance_pct
FROM budget_vs_actual_synthetic GROUP BY department ORDER BY ABS(variance_pct) DESC;

-- Months flagged over budget
SELECT department, month, budget_gbp, actual_gbp, variance_pct, kpi_flag
FROM budget_vs_actual_synthetic WHERE kpi_flag = 'OVER_BUDGET' ORDER BY variance_pct DESC;

-- Monthly totals across the business
SELECT month, ROUND(SUM(budget_gbp),2) AS budget, ROUND(SUM(actual_gbp),2) AS actual
FROM budget_vs_actual_synthetic GROUP BY month ORDER BY month;
