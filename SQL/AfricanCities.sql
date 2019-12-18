-- SELECT city.name
-- FROM city, country
-- WHERE city.countrycode = country.code and country.continent = 'Africa'

Select city.name 
FROM city INNER JOIN country On countrycode = code
WHERE continent = 'Africa';
