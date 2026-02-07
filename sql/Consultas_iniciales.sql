
CREATE TABLE fact_gdp (
    country VARCHAR(3),
    year INT,
    gdp_usd NUMERIC,
    PRIMARY KEY (country, year)
);

CREATE TABLE fact_population (
    country VARCHAR(3),
    year INT,
    population NUMERIC,
    PRIMARY KEY (country, year)
);

SELECT COUNT(*) FROM gdp_fact;
SELECT COUNT(*) FROM population_fact;

CREATE TABLE macro_analysis AS
SELECT
    g.country,
    g.year,
    g.value AS gdp_usd,
    p.value AS population,
    (g.value / p.value) AS gdp_per_capita
FROM gdp_fact g
JOIN population_fact p
    ON g.country = p.country
   AND g.year = p.year;

SELECT COUNT(*) FROM macro_analysis;

SELECT *
FROM macro_analysis
ORDER BY year DESC
LIMIT 10;

