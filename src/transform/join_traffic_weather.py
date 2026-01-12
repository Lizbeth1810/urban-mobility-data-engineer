import os
import pandas as pd

TRAFFIC_PATH = "data/processed/traffic_nyc_clean.csv"
WEATHER_PATH = "data/raw/weather.csv"
OUT_PATH = "data/analytics/traffic_weather_dataset.csv"

if __name__ == "__main__":
    traffic = pd.read_csv(TRAFFIC_PATH)
    weather = pd.read_csv(WEATHER_PATH)

    weather_row = weather.iloc[0]

    traffic["city"] = weather_row["city"]
    traffic["temperature"] = weather_row["temperature"]
    traffic["humidity"] = weather_row["humidity"]
    traffic["weather"] = weather_row["weather"]
    traffic["wind_speed"] = weather_row["wind_speed"]

    os.makedirs("data/analytics", exist_ok=True)
    traffic.to_csv(OUT_PATH, index=False)

    print(f"Dataset unido guardado en {OUT_PATH} (filas: {len(traffic)})")
