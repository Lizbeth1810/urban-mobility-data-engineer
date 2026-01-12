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
- Apache Spark instalado (para usar `spark-submit`) **o** PySpark instalado (ver abajo)

---

## 2) Instalación rápida (modo local)
Desde la raíz del proyecto:

```bat
python -m venv venv
venv\Scripts\activate
pip install -r requirements.txt
```

Configura `config/config.json` con tu API Key de OpenWeather.

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

---

## 4) Ejecutar con HDFS (opcional)
1) Asegura que tienes `hdfs` CLI configurado (Hadoop client).
2) Ejecuta:

```bash
bash scripts/hdfs_mkdirs.sh
bash scripts/hdfs_put_raw.sh
```

---

## 5) Spark (PySpark) – Feature Engineering + Correlation Analysis (requerimiento)
El job está en `spark/spark_processing.py`.

### Opción A: Ejecutar con Spark instalado (recomendado)
```bash
spark-submit spark/spark_processing.py
```

### Opción B: Ejecutar solo con PySpark instalado
Si no tienes Spark instalado, puedes intentar:
```bat
python spark\spark_processing.py
```
(depende de tu instalación; lo más estable es `spark-submit`).

Salida:
- `data/processed/spark_features.csv` (dataset con features)
- `data/processed/spark_correlations.json` (resultados de correlación)

---

## 6) Airflow (opcional)
El DAG está en `airflow/dags/urban_mobility_dag.py`.

Para correr Airflow localmente (rápido):
```bash
airflow db init
airflow users create --username admin --firstname Admin --lastname User --role Admin --email admin@example.com
airflow webserver
airflow scheduler
```
UI: http://localhost:8080

En el DAG, ajusta `PROJECT_DIR` a tu ruta local.

---

## 7) Power BI
Importa el archivo:
- `data/analytics/powerbi_dataset.csv`

Guía: `power_bi/README.md`

---

## 8) Tests
```bat
pytest -q
```

---

## 9) Entregables
- **Source code**: este repo
- **Dashboard**: publica en Power BI Service y pega el link en el ticket/README
- **Report**: `docs/report.md`
