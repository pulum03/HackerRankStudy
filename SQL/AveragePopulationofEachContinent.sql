-- SELECT COUNTRY.continent, FLOOR(AVG(CITY.population))
-- FROM CITY, COUNTRY
-- WHERE CITY.countrycode = COUNTRY.code
-- GROUP BY COUNTRY.continent

SELECT COUNTRY.continent, FLOOR(AVG(CITY.population))
FROM CITY JOIN COUNTRY ON CITY.countrycode = COUNTRY.code
GROUP BY COUNTRY.continent