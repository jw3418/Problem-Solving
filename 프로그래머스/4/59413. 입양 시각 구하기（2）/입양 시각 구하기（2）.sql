-- 코드를 입력하세요
WITH RECURSIVE a AS (
    SELECT 0 AS HOUR
    UNION ALL
    SELECT HOUR+1
    FROM a
    WHERE HOUR < 23
)

SELECT a.HOUR, IFNULL(b.COUNT, 0)
FROM a
LEFT JOIN (SELECT HOUR(DATETIME) AS HOUR, COUNT(DISTINCT ANIMAL_ID) AS COUNT
    FROM ANIMAL_OUTS
    GROUP BY HOUR(DATETIME)) b
ON a.HOUR = b.HOUR