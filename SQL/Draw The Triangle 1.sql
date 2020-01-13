/*
Enter your query here.
*/
SET @number = 21;
SELECT REPEAT('* ', @number := @number - 1) 
FROM information_schema.TABLES;