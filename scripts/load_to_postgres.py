import pandas as pd
from sqlalchemy import create_engine

# =========================
# 1. CONFIG CONEXIÓN
# =========================

user = "postgres"
password = "haru"
host = "localhost"
port = "5432"
database = "macro_latam"

engine = create_engine(
    f"postgresql+psycopg2://{user}:{password}@{host}:{port}/{database}"
)

print("✅ Conexión establecida")

# =========================
# 2. LEER CSVs
# =========================

gdp_df = pd.read_csv("data/gdp_fact.csv")
population_df = pd.read_csv("data/population_fact.csv")

print("GDP filas:", len(gdp_df))
print("Population filas:", len(population_df))

# =========================
# 3. CARGAR A POSTGRESQL
# =========================

gdp_df.to_sql(
    "gdp_fact",
    engine,
    if_exists="append",
    index=False
)

population_df.to_sql(
    "population_fact",
    engine,
    if_exists="append",
    index=False
)

print("✅ Datos cargados correctamente")
