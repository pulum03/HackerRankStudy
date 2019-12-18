/*
Enter your query here.
*/
SELECT IF(gd.grade >= 8, st.name, NULL), gd.grade, st.marks
FROM STUDENTS as st, GRADES as gd
-- WHERE st.marks >= gd.min_mark and st.marks <= gd.max_mark
WHERE st.marks BETWEEN gd.min_mark AND gd.max_mark
GROUP BY gd.grade DESC, st.name, st.marks DESC
-- ORDER BY
--     CASE WHEN st.marks >= 70 THEN st.name AND gd.grade END DESC,
--     CASE WHEN st.marks < 70  THEN st.name AND gd.grade END DESC

