import os
import pandas as pd

IN_PATH = "data/analytics/traffic_weather_dataset.csv"
OUT_PATH = "data/analytics/powerbi_dataset.csv"

def build_powerbi_dataset(df: pd.DataFrame) -> pd.DataFrame:
    df = df.copy()
    df["hour"] = pd.to_datetime(df["hour"], errors="coerce")

    agg = (df.dropna(subset=["hour"])
             .groupby(["hour"], as_index=False)
             .agg(
                 traffic_volume_sum=("volume", "sum"),
                 traffic_volume_avg=("volume", "mean"),
                 records=("volume", "count"),
                 temperature=("temperature", "mean"),
                 humidity=("humidity", "mean"),
                 wind_speed=("wind_speed", "mean"),
             )
             .sort_values("hour"))
    return agg

if __name__ == "__main__":
    if not os.path.exists(IN_PATH):
        raise FileNotFoundError(f"No existe {IN_PATH}. Corre src/transform/join_traffic_weather.py")

    df = pd.read_csv(IN_PATH)
    out = build_powerbi_dataset(df)

    os.makedirs("data/analytics", exist_ok=True)
    out.to_csv(OUT_PATH, index=False)
    print(f"Power BI dataset guardado en {OUT_PATH} (filas: {len(out)})")
