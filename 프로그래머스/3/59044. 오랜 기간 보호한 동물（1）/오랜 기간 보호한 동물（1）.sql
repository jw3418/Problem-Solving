SELECT a.NAME, a.DATETIME
FROM ANIMAL_INS a
LEFT OUTER JOIN ANIMAL_OUTS b
ON a.ANIMAL_ID = b.ANIMAL_ID
WHERE b.ANIMAL_ID IS NULL
ORDER BY a.DATETIME ASC
LIMIT 3;