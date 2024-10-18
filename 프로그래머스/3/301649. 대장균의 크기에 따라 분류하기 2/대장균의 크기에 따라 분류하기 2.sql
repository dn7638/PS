SELECT ID, COLONY_NAME
FROM(
    SELECT ID,
        CASE
            WHEN (row_num-1) DIV (total DIV 4) = 0 THEN 'CRITICAL'
            WHEN (row_num-1) DIV (total DIV 4) = 1 THEN 'HIGH'
            WHEN (row_num-1) DIV (total DIV 4) = 2 THEN 'MEDIUM'
            WHEN (row_num-1) DIV (total DIV 4) = 3 THEN 'LOW'
            ELSE 'null'
        END AS COLONY_NAME
    FROM (
        SELECT ROW_NUMBER() OVER (ORDER BY SIZE_OF_COLONY DESC) AS row_num, ID, SIZE_OF_COLONY,
               (SELECT COUNT(*) FROM ECOLI_DATA) AS total
        FROM ECOLI_DATA
        ) AS subquery
    ) AS final
ORDER BY ID ASC;

