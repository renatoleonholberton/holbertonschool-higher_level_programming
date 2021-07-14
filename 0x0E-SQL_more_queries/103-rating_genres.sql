-- This script lists all genres by their rating
SELECT tg.name, SUM(tr.rate) AS rating
FROM tv_shows AS ts
INNER JOIN tv_show_ratings AS tr ON ts.id = tr.show_id
INNER JOIN tv_show_genres AS tsg ON ts.id = tsg.show_id
INNER JOIN tv_genres AS tg ON tg.id = tsg.genre_id
GROUP BY tg.name
ORDER BY rating DESC;
