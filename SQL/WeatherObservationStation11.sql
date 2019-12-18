/*
Enter your query here.
*/
SELECT DISTINCT city 
FROM station
WHERE NOT city REGEXP '^[aeiou].*[aeiou]$'