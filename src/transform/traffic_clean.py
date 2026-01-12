import os
import pandas as pd

RAW_PATH = "data/raw/traffic_nyc.csv"
OUT_PATH = "data/processed/traffic_nyc_clean.csv"

if __name__ == "__main__":
    df = pd.read_csv(RAW_PATH)

    df["datetime"] = pd.to_datetime(
        df[["yr", "m", "d", "hh", "mm"]].rename(
            columns={
                "yr": "year",
                "m": "month",
                "d": "day",
                "hh": "hour",
                "mm": "minute"
            }
        ),
        errors="coerce"
    )

    # Volumen
    df["volume"] = pd.to_numeric(df["vol"], errors="coerce")

    # Ubicación
    df["location"] = df["boro"]

    cleaned = df[["datetime", "location", "volume"]].dropna()
    cleaned["hour"] = cleaned["datetime"].dt.floor("h")

    os.makedirs("data/processed", exist_ok=True)
    cleaned.to_csv(OUT_PATH, index=False)

    print(f"Traffic limpio guardado en {OUT_PATH} (filas: {len(cleaned)})")
