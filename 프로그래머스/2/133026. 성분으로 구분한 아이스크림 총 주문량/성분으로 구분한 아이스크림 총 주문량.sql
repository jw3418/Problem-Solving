-- 코드를 입력하세요
SELECT INGREDIENT_TYPE, SUM(TOTAL_ORDER) AS TOTAL_ORDER
FROM FIRST_HALF a
JOIN ICECREAM_INFO b
ON a.FLAVOR = b.FLAVOR
GROUP BY b.INGREDIENT_TYPE