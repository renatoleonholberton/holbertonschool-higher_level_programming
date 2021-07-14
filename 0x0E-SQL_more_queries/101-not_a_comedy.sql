-- This script lists all shows without the genre Comedy 
SELECT ts.title
FROM tv_shows AS ts
WHERE ts.id NOT IN (
	SELECT tv_shows.id
	FROM tv_shows
	INNER JOIN tv_show_genres ON tv_shows.id = tv_show_genres.show_id
	INNER JOIN tv_genres ON tv_genres.id = tv_show_genres.genre_id
	WHERE tv_genres.name = 'Comedy')
ORDER BY ts.title ASC;
