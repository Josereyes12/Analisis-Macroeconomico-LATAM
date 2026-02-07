import requests
import pandas as pd
import os

BASE_URL = "https://api.worldbank.org/v2/country/{countries}/indicator/{indicator}"

PARAMS = {
    "format": "json",
    "per_page": 20000
}

COUNTRIES = [
    "ARG",  # Argentina
    "BOL",  # Bolivia
    "BRA",  # Brazil
    "CHL",  # Chile
    "COL",  # Colombia
    "CRI",  # Costa Rica
    "CUB",  # Cuba
    "DOM",  # Dominican Republic
    "ECU",  # Ecuador
    "SLV",  # El Salvador
    "GTM",  # Guatemala
    "HND",  # Honduras
    "MEX",  # Mexico
    "NIC",  # Nicaragua
    "PAN",  # Panama
    "PRY",  # Paraguay
    "PER",  # Peru
    "URY",  # Uruguay
    "VEN",  # Venezuela
    "HTI"   # Haiti
]

def fetch_indicator_data(countries, indicator):
    country_str = ";".join(countries)
    url = BASE_URL.format(countries=country_str, indicator=indicator)

    response = requests.get(url, params=PARAMS)
    response.raise_for_status()

    data = response.json()[1]
    return data


def transform_to_dataframe(data):
    records = []

    for item in data:
        if item["value"] is not None:
            records.append({
                "country": item["country"]["id"],
                "year": int(item["date"]),
                "value": item["value"]
            })

    df = pd.DataFrame(records)
    return df


def save_to_csv(df, filename):
    os.makedirs("data", exist_ok=True)
    path = f"data/{filename}"
    df.to_csv(path, index=False)
    print(f"Archivo guardado en {path}")


if __name__ == "__main__":

    # GDP
    gdp_data = fetch_indicator_data(COUNTRIES, "NY.GDP.MKTP.CD")
    df_gdp = transform_to_dataframe(gdp_data)
    save_to_csv(df_gdp, "gdp_fact.csv")

    # Population
    pop_data = fetch_indicator_data(COUNTRIES, "SP.POP.TOTL")
    df_pop = transform_to_dataframe(pop_data)
    save_to_csv(df_pop, "population_fact.csv")

    print("\nGDP preview:")
    print(df_gdp.head())

    print("\nPopulation preview:")
    print(df_pop.head())
