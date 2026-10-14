
from pathlib import Path
import pandas as pd

RAW_DIR = Path("data/raw")

fund_file = next(RAW_DIR.glob("*fund_master*.csv"))
nav_file = next(RAW_DIR.glob("*nav_history*.csv"))

fund_master = pd.read_csv(fund_file)
nav_history = pd.read_csv(nav_file)

print("Fund master columns:", fund_master.columns.tolist())
print("NAV history columns:", nav_history.columns.tolist())

print("\nFund master preview:")
print(fund_master.head())

print("\nNAV history preview:")
print(nav_history.head())

# Validate scheme codes in NAV history against fund master

fund_code_col = "amfi_code"
nav_code_col = "amfi_code"

if fund_code_col in fund_master.columns and nav_code_col in nav_history.columns:
    fund_codes = set(fund_master[fund_code_col].dropna().astype(str).str.strip())
    nav_codes = set(nav_history[nav_code_col].dropna().astype(str).str.strip())

    unmatched_codes = nav_codes - fund_codes

    print("\nTotal unique fund master codes:", len(fund_codes))
    print("Total unique NAV history codes:", len(nav_codes))
    print("NAV codes missing from fund master:", len(unmatched_codes))
    print("Sample unmatched codes:", list(unmatched_codes)[:10])
else:
    print("\nColumn names do not match.")
    print("Fund master columns:", fund_master.columns.tolist())
    print("NAV history columns:", nav_history.columns.tolist())
