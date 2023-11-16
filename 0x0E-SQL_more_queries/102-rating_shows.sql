-- list all the shows from hbtn_0d_tvshows_rate by the rating
-- list all the rows of table by sum of a linked row
SELECT title, SUM(tv_show_ratings.rate) 'rating'
FROM tv_shows
LEFT JOIN tv_show_ratings ON tv_show_ratings.show_id = tv_shows.id
GROUP BY title
ORDER BY rating DESC;
