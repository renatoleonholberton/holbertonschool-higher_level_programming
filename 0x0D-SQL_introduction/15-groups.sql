-- This script displays the count of record with the same socre
SELECT score, COUNT(score) AS number
	FROM second_table
	GROUP BY score
	ORDER BY number DESC;
