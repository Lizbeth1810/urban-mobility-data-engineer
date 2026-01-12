import os
import json
import requests
import pandas as pd
from datetime import datetime

def extract_weather(api_key: str, city: str) -> dict:
    url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric"
    r = requests.get(url, timeout=60)
    r.raise_for_status()
    return r.json()

if __name__ == "__main__":
    with open("config/config.json", "r", encoding="utf-8") as f:
        config = json.load(f)

    data = extract_weather(config["openweather_api_key"], config["city"])

    weather_row = {
        "city": data.get("name"),
        "temperature": data["main"]["temp"],
        "humidity": data["main"]["humidity"],
        "weather": data["weather"][0]["description"] if data.get("weather") else None,
        "wind_speed": data["wind"]["speed"] if data.get("wind") else None,
        "timestamp": datetime.now().isoformat(timespec="seconds"),
    }

    df = pd.DataFrame([weather_row])
    os.makedirs("data/raw", exist_ok=True)
    df.to_csv("data/raw/weather.csv", index=False)

    print("Archivo guardado en data/raw/weather.csv")
