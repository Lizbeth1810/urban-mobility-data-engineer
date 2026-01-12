# Urban Mobility & Traffic Analysis – Data Engineer Challenge (Junior-friendly)

Este repo cumple con los requerimientos del case:

- **Python** para extracción (Traffic + Weather) y limpieza
- **HDFS** (scripts/guía) para almacenamiento
- **Spark (PySpark)** para feature engineering y correlation analysis
- **Airflow** para orquestación (extract → transform → spark → export BI)
- **Power BI**: dataset final CSV listo para importar
- **Documentación** + **Tests** (pytest)

> Nota Jr: el proyecto está hecho para correr localmente (sin cluster). Incluye scripts para HDFS y un job PySpark que corre en modo local con `spark-submit`.

---

## 1) Requisitos

- Python 3.10+
- Java 8/11 (si vas a ejecutar Spark)
- Apache Spark instalado (para usar `spark-submit`) **o** PySpark instalado

---

## 2) Instalación rápida (modo local)

Desde la raíz del proyecto:

```bat
python -m venv venv
venv\Scripts\activate
pip install -r requirements.txt
```

---

## 3) Ejecutar pipeline en modo local (sin HDFS/Spark)

Esto genera el dataset base (para unión) en `data/analytics/traffic_weather_dataset.csv` y el dataset final para BI en `data/analytics/powerbi_dataset.csv`:

```bat
python src\extract\weather_api.py
python src\extract\traffic_nyc.py
python src\transform\traffic_clean.py
python src\transform\join_traffic_weather.py
python src\load\powerbi_export.py
```

## 4) Power BI

Importa el archivo:

- `data/analytics/powerbi_dataset.csv`

Guía: `power_bi/README.md`
