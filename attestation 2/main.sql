select *
from sqlprotest.movies m
where rating is not null
order by year
limit 3 


select 
g.name genre_name,
avg(m.rating) average_rating,
count(distinct m.id) movie_count
from sqlprotest.movies m
join sqlprotest.movie_genres mg on m.id = mg.movie_id
right join sqlprotest.genres g on g.id = mg.genre_id
group by genre_name
order by average_rating desc


select 
name,
coalesce(rating,0)
from sqlprotest.movies m
order by name




select 
g.name genre_name,
count(m.id) movies_count
from sqlprotest.movies m
join sqlprotest.movie_genres mg on m.id = mg.movie_id
right join sqlprotest.genres g on g.id = mg.genre_id
group by g.name
having count(m.id) >=3 
order by count(m.id) desc


(select m.id,m.name,m.year,m.rating
from sqlprotest.movies m
join sqlprotest.movie_genres mg on m.id = mg.movie_id
right join sqlprotest.genres g on g.id = mg.genre_id
where m.id is not null
order by m.name)
except
(select m.id,m.name,m.year,m.rating
from sqlprotest.movies m
join sqlprotest.movie_genres mg on m.id = mg.movie_id
right join sqlprotest.genres g on g.id = mg.genre_id
where g.name like 'Криминал')