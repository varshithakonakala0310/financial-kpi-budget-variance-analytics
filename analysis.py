import os, warnings; warnings.filterwarnings("ignore")
import numpy as np, pandas as pd
BASE=os.path.dirname(os.path.abspath(__file__)); os.makedirs(os.path.join(BASE,"data"),exist_ok=True); os.makedirs(os.path.join(BASE,"results"),exist_ok=True)
rng=np.random.default_rng(42)
depts=["Sales","Marketing","Operations","IT","HR","Finance"]
rows=[]
for d in depts:
    base=rng.uniform(80000,250000)
    for month in range(1,13):
        budget=base*(1+0.02*month)*rng.uniform(0.95,1.05)
        actual=budget*rng.normal(1.0,0.12)
        rows.append({"department":d,"month":f"2024-{month:02d}","budget_gbp":round(budget,2),"actual_gbp":round(actual,2)})
df=pd.DataFrame(rows); df["variance_gbp"]=(df.actual_gbp-df.budget_gbp).round(2); df["variance_pct"]=((df.actual_gbp-df.budget_gbp)/df.budget_gbp*100).round(2)
df["kpi_flag"]=np.where(df.variance_pct>10,"OVER_BUDGET",np.where(df.variance_pct<-10,"UNDER_BUDGET","ON_TRACK"))
df.to_csv(os.path.join(BASE,"data","budget_vs_actual_synthetic.csv"),index=False)
by=df.groupby("department").agg(budget=("budget_gbp","sum"),actual=("actual_gbp","sum")); by["variance_pct"]=(by.actual-by.budget)/by.budget*100
over=(df.kpi_flag=="OVER_BUDGET").sum(); under=(df.kpi_flag=="UNDER_BUDGET").sum()
with open(os.path.join(BASE,"results","results_summary.txt"),"w") as f:
    f.write("Financial KPI Budget Variance Analytics — SYNTHETIC RESULTS\n")
    f.write(f"Departments: {len(depts)}, Months: 12 (2024), Rows: {len(df)}\n")
    f.write(f"Total budget: GBP {df.budget_gbp.sum():.2f}, Total actual: GBP {df.actual_gbp.sum():.2f}, Overall variance: {(df.actual_gbp.sum()-df.budget_gbp.sum())/df.budget_gbp.sum()*100:.2f}%\n")
    f.write(f"KPI flags: OVER_BUDGET={over}, UNDER_BUDGET={under}, ON_TRACK={len(df)-over-under}\n")
    for d,r in by.iterrows(): f.write(f"  {d}: budget=GBP {r['budget']:.2f} actual=GBP {r['actual']:.2f} variance={r['variance_pct']:.2f}%\n")
    worst=by["variance_pct"].abs().idxmax(); f.write(f"Largest absolute department variance: {worst} ({by.loc[worst,'variance_pct']:.2f}%)\n")
print(by); print(f"over={over} under={under}")
