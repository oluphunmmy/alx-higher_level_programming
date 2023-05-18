-- This script lists all shows without the comedy genre in the database hbtn_0d_tvshows.
-- Records are ordered by ascending show title.

SELECT DISTINCT tvs.title
FROM tv_shows tvs
WHERE tvs.title NOT IN (
	SELECT tvs.title
	FROM tv_shows tvs
	INNER JOIN tv_show_genres it
	ON tvs.id = it.show_id
	INNER JOIN tv_genres tvg
	ON tvg.id = it.genre_id
	WHERE name = 'Comedy')
ORDER BY tvs.title ASC;
