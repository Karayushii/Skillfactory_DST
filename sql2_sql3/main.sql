SELECT movie_title,year,rating
FROM sql.kinopoisk 


SELECT 
    director,
    movie_title,
    10-rating
FROM sql.kinopoisk 


SELECT 
    director,
    movie_title,
    rating * 10 as rating_100
FROM sql.kinopoisk 

SELECT *
FROM sql.kinopoisk
WHERE year > 1999


SELECT 
movie_title,
director,
screenwriter,
actors
FROM sql.kinopoisk
WHERE (rating BETWEEN 7.9 AND 8.6 OR year < 1990) AND overview IS NOT NULL AND movie_title NOT LIKE 'Т%'  AND movie_title LIKE '_____________'
ORDER BY rating DESC
LIMIT 7

SELECT 
MAX (heal)
FROM sql.pokemon
WHERE type1 = 'Dragon'
