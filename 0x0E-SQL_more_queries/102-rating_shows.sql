-- This script list all shows by their   ratings
SELECT ts.title, SUM(tr.rate) AS rating
FROM tv_shows AS ts
INNER JOIN tv_show_ratings AS tr ON ts.id = tr.show_id
GROUP BY ts.title
ORDER BY rating DESC;
