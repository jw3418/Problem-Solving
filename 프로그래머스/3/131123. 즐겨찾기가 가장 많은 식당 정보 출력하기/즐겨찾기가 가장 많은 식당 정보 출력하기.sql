-- 코드를 입력하세요
SELECT a.FOOD_TYPE, a.REST_ID, a.REST_NAME, a.FAVORITES
FROM REST_INFO a
JOIN (SELECT FOOD_TYPE, MAX(FAVORITES) AS MAX_FAV FROM REST_INFO GROUP BY FOOD_TYPE) b
ON a.FOOD_TYPE = b.FOOD_TYPE AND a.FAVORITES = b.MAX_FAV
ORDER BY FOOD_TYPE DESC;

# SELECT * FROM REST_INFO;