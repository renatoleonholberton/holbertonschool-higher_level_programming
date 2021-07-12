-- This script displays the 3 top cities with highest temperatures in July and August
SELECT city, AVG(value) AS avg_temp
	FROM temperatures
	WHERE month = 7 OR month = 8
	GROUP BY city
	ORDER BY avg_temp DESC
	LIMIT 3;
