-- This script lists all genres of the shows that are not 'dexter'
SELECT tg.name
FROM tv_genres AS tg
WHERE tg.id NOT IN (
	SELECT tv_genres.id
	FROM tv_shows
	INNER JOIN tv_show_genres ON tv_shows.id = tv_show_genres.show_id
	INNER JOIN tv_genres ON tv_genres.id = tv_show_genres.genre_id
	WHERE tv_shows.title = 'Dexter')
ORDER BY tg.name ASC;
