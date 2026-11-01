# Write your MySQL query statement below
WITH ranked AS (
    SELECT
        num,
        frequency,
        SUM(frequency) OVER (ORDER BY num) AS cumulative,
        SUM(frequency) OVER () AS total
    FROM Numbers
),

middle AS (
    SELECT
        MIN(
            CASE
                WHEN cumulative >= FLOOR((total + 1) / 2)
                THEN num
            END
        ) AS first_middle,
        
        MIN(
            CASE
                WHEN cumulative >= CEIL((total + 1) / 2)
                THEN num
            END
        ) AS second_middle
    FROM ranked
)

SELECT
    (first_middle + second_middle) / 2 AS median
FROM middle
