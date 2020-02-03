/*
Enter your query here.
*/
SELECT h.hacker_id, h.name, sum(ms) as ts
FROM 
    hackers as h, 
    (SELECT hacker_id, challenge_id, max(score) as ms             FROM submissions
      GROUP BY hacker_id, challenge_id 
     ) as sub 
WHERE h.hacker_id = sub.hacker_id
GROUP BY sub.hacker_id, h.name
HAVING ts <> 0
ORDER BY ts DESC, h.hacker_id