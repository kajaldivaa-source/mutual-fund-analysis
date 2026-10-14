
from pathlib import Path
import pandas as pd

# Project ke raw data folder ka path
RAW_DIR = Path("data/raw")

def inspect_csv_files():
    csv_files = list(RAW_DIR.glob("*.csv"))

    if not csv_files:
        print("No CSV files found in data/raw.")
        print("Please copy your 10 provided CSV datasets into this folder.")
        return

    print(f"Found {len(csv_files)} CSV file(s).")

    for file in csv_files:
        print("\n" + "=" * 60)
        print(f"File: {file.name}")

        try:
            df = pd.read_csv(file)

            print("Shape (rows, columns):", df.shape)
            print("\nData types:")
            print(df.dtypes)
            print("\nFirst 5 rows:")
            print(df.head())
            print("\nMissing values:")
            print(df.isnull().sum())
            print("\nDuplicate rows:", df.duplicated().sum())

        except Exception as exc:
            print(f"Could not read {file.name}: {exc}")

def create_data_quality_summary():
    RAW_DIR = Path("data/raw")
    REPORT_DIR = Path("reports")
    REPORT_DIR.mkdir(parents=True, exist_ok=True)

    results = []

    for file in RAW_DIR.glob("*.csv"):
        try:
            df = pd.read_csv(file)

            results.append({
                "file_name": file.name,
                "rows": df.shape[0],
                "columns": df.shape[1],
                "missing_cells": int(df.isnull().sum().sum()),
                "duplicate_rows": int(df.duplicated().sum())
            })

        except Exception as exc:
            results.append({
                "file_name": file.name,
                "error": str(exc)
            })

    report = pd.DataFrame(results)
    report.to_csv(REPORT_DIR / "data_quality_summary.csv", index=False)

    print("\nData quality report saved to reports/data_quality_summary.csv")
    print(report.to_string(index=False))

 
if __name__ == "__main__":
    inspect_csv_files()
    create_data_quality_summary()
