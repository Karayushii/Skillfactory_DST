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
