# DROP TABLES

songplay_table_drop = "DROP table if exists songplays"
user_table_drop = "DROP table if exists users"
song_table_drop = "DROP table if exists songs"
artist_table_drop = "DROP table if exists artists"
time_table_drop = "DROP table if exists time"

# CREATE TABLES

songplay_table_create = ("""CREATE TABLE IF NOT EXISTS songplays (songplay_id serial primary key, start_time timestamp NOT NULL, user_id int NOT NULL, level varchar, song_id varchar, artist_id varchar, session_id int NOT NULL, location varchar, user_agent text)""")

user_table_create = ("""CREATE TABLE IF NOT EXISTS users (user_id varchar primary key, first_name varchar, last_name varchar, gender varchar, level varchar)""")

song_table_create = ("""CREATE TABLE IF NOT EXISTS songs (song_id varchar(255) primary key, title varchar(255), artist_id varchar(255), year int, duration float)""")

artist_table_create = ("""CREATE TABLE IF NOT EXISTS artists (artist_id varchar primary key, name varchar, location varchar, latitude varchar, longitude varchar)""")

time_table_create = ("""CREATE TABLE IF NOT EXISTS time (start_time timestamp primary key, hour int, day int, week int, month varchar, year int, weekday varchar)""")

# INSERT RECORDS

songplay_table_insert = ("""
INSERT INTO songplays(start_time, user_id, level, song_id, artist_id,
session_id, location, user_agent) 
VALUES(%s,%s,%s,%s,%s,%s,%s,%s);
""")
user_table_insert = ("""
INSERT INTO users(user_id, first_name, last_name, gender, level)
VALUES(%s,%s,%s,%s,%s)
ON CONFLICT(user_id) DO UPDATE
SET first_name = excluded.first_name,
    last_name = excluded.last_name,
    gender = excluded.gender,
    level = excluded.level;
""")

song_table_insert = ("""
insert into songs(song_id, title, artist_id, year, duration)
VALUES(%s,%s,%s,%s,%s)
ON CONFLICT(song_id) DO UPDATE
SET title = excluded.title,
    artist_id = excluded.artist_id,
    year = excluded.year,
    duration = excluded.duration;
""")

artist_table_insert = ("""
INSERT INTO artists(artist_id, name, location, latitude, longitude)
VALUES(%s,%s,%s,%s,%s)
ON CONFLICT(artist_id) DO UPDATE
SET name = excluded.name,
    location = excluded.location,
    latitude = excluded.latitude,
    longitude = excluded.longitude;
""")


time_table_insert = ("""
INSERT INTO time(start_time, hour, day, week, month, year, weekday)
VALUES(%s,%s,%s,%s,%s,%s,%s)
ON CONFLICT(start_time) DO UPDATE
SET hour = excluded.hour,
    day = excluded.day,
    week = excluded.week,
    month = excluded.month,
    year = excluded.year,
    weekday = excluded.weekday;
""")

# FIND SONGS

song_select = ("""
select s.song_id, a.artist_id from songs s
inner join artists a on s.artist_id = a.artist_id where
s.title = %s and a.name = %s and s.duration = %s;
""")


# QUERY LISTS

create_table_queries = [songplay_table_create, user_table_create, song_table_create, artist_table_create, time_table_create]
drop_table_queries = [songplay_table_drop, user_table_drop, song_table_drop, artist_table_drop, time_table_drop]