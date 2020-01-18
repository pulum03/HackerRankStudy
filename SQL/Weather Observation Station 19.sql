/*
Enter your query here.
*/
SELECT ROUND(POW(POW(abs(Max(Lat_n)-min(Lat_n)),2)+POW(abs(Max(long_w)-min(long_w)),2),1/2),4) 
FROM STATION;