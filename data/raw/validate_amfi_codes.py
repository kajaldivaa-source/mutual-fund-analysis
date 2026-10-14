
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
