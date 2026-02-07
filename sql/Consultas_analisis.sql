
--Ranking LATAM por GDP per capita (último año)
SELECT
    country,
    year,
    gdp_per_capita
FROM macro_analysis
WHERE year = 2024
ORDER BY gdp_per_capita DESC;

--Top 5 economías por GDP total
SELECT
    country,
    year,
    gdp_usd
FROM macro_analysis
WHERE year = 2024
ORDER BY gdp_usd DESC
LIMIT 5;

--Crecimiento GDP YoY
WITH gdp_lag AS (
    SELECT
        country,
        year,
        gdp_usd,
        LAG(gdp_usd) OVER (
            PARTITION BY country
            ORDER BY year
        ) AS prev_year_gdp
    FROM macro_analysis
)

SELECT
    country,
    year,
    gdp_usd,
    prev_year_gdp,
    ROUND(
        ((gdp_usd - prev_year_gdp) / prev_year_gdp)::numeric * 100,
        2
    ) AS growth_pct
FROM gdp_lag;



--Impacto COVID (2019–2021)
SELECT
    country,
    MAX(CASE WHEN year = 2019 THEN gdp_usd END) AS gdp_2019,
    MAX(CASE WHEN year = 2020 THEN gdp_usd END) AS gdp_2020,
    MAX(CASE WHEN year = 2021 THEN gdp_usd END) AS gdp_2021
FROM macro_analysis
GROUP BY country;

--Crecimiento poblacional
SELECT
    country,
    year,
    population,
    population - LAG(population) OVER (
        PARTITION BY country
        ORDER BY year
    ) AS pop_growth
FROM macro_analysis;
