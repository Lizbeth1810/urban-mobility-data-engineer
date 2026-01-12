import os
import json
import requests
import pandas as pd

DATASET_ID = "7ym2-wayt"
BASE_URL = f"https://data.cityofnewyork.us/resource/{DATASET_ID}.json"

def extract_traffic(app_token: str | None = None, limit: int = 20000) -> list[dict]:
    params = {"$limit": int(limit)}
    headers = {}
    if app_token:
        headers["X-App-Token"] = app_token

    r = requests.get(BASE_URL, params=params, headers=headers, timeout=60)
    r.raise_for_status()
    return r.json()

if __name__ == "__main__":
    with open("config/config.json", "r", encoding="utf-8") as f:
        config = json.load(f)

    data = extract_traffic(
        app_token=config.get("socrata_app_token") or None,
        limit=config.get("nyc_traffic_limit", 20000),
    )

    df = pd.DataFrame(data)
    os.makedirs("data/raw", exist_ok=True)
    df.to_csv("data/raw/traffic_nyc.csv", index=False)

    print("Archivo guardado en data/raw/traffic_nyc.csv")
