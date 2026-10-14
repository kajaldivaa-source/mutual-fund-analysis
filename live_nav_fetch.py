
from pathlib import Path
import requests
import pandas as pd

RAW_DIR = Path("data/raw")
RAW_DIR.mkdir(parents=True, exist_ok=True)

SCHEMES = {
    "HDFC Top 100 Direct": 125497,
    "SBI Bluechip": 119551,
    "ICICI Bluechip": 120503,
    "Nippon Large Cap": 118632,
    "Axis Bluechip": 119092,
    "Kotak Bluechip": 120841,
}

def fetch_nav(name, scheme_code):
    url = f"https://api.mfapi.in/mf/{scheme_code}"

    try:
        response = requests.get(url, timeout=30)
        response.raise_for_status()
        data = response.json()

        if not data.get("data"):
            print(f"No NAV data returned for {name}")
            return

        df = pd.DataFrame(data["data"])
        df["scheme_code"] = scheme_code
        df["scheme_name"] = name

        output = RAW_DIR / f"live_nav_{scheme_code}.csv"
        df.to_csv(output, index=False)

        print(f"Saved {name}: {len(df)} records -> {output}")

    except (requests.RequestException, ValueError) as exc:
        print(f"Failed for {name}: {exc}")

if __name__ == "__main__":
    for name, code in SCHEMES.items():
        fetch_nav(name, code)
