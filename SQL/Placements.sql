/*
Enter your query here.
*/
-- SELECT s.name 
-- FROM Students AS s 
-- JOIN Friends AS f ON f.id = s.id
-- JOIN Packages AS p ON p.id = s.id
-- JOIN Packages AS fp ON fp.id = f.friend_ID
-- WHERE p.salary < fp.salary
-- ORDER BY fp.salary

SELECT s.name
FROM Students as s, Friends as f, Packages as p1, Packages as p2
WHERE s.id = f.id and s.id = p1.id and f.friend_ID = p2.id and p1.salary < p2.salary
ORDER BY p2.salary