# DROP TABLES

songplay_table_drop = "drop table if exists songplays;"
user_table_drop = "drop table if exists users;"
song_table_drop = "drop table if exists songs;"
artist_table_drop = "drop table if exists artists;"
time_table_drop = "drop table if exists time;"

# CREATE TABLES

songplay_table_create = ("""Create table If not exists songplays 
                            (songplay_id serial primary key, 
                             start_time bigint, 
                             user_id int, 
                             level varchar, 
                             song_id varchar, 
                             artist_id varchar, 
                             session_id int, 
                             location varchar, 
                             user_agent varchar);
""")

user_table_create = ("""Create table if not exists  users 
                        (user_id int not null, 
                         first_name varchar, 
                         last_name varchar, 
                         gender varchar, 
                         level varchar,
                         primary key (user_id)
                         );
""")

song_table_create = ("""Create table if not exists songs 
                        (song_id varchar not null , 
                         title varchar, 
                         artist_id varchar, 
                         year int, 
                         duration float,
                         primary key (song_id));
""")

artist_table_create = ("""Create table if not exists artists 
                            (artist_id varchar not null, 
                             name varchar, 
                             location varchar, 
                             lattitude numeric, 
                             longitude numeric,
                             primary key (artist_id));
""")

time_table_create = ("""create table if not exists time 
                        (start_time bigint not null, 
                         hour int, day int, 
                         week int, 
                         month int, 
                         year int, 
                         weekday int,
                         primary key (start_time));
""")

# INSERT RECORDS

songplay_table_insert = ("""insert into songplays (start_time, user_id, level, song_id, \
                            artist_id, session_id, location, user_agent) values (%s, %s, %s, %s, %s, %s, %s, %s)
                            on conflict do nothing
""")

user_table_insert = ("""insert into users (user_id, 
                         first_name, 
                         last_name, 
                         gender, 
                         level) 
                         values(%s, %s, %s,%s, %s) 
                         on conflict (user_id) do nothing
                         ;
""")

song_table_insert = ("""insert into songs (song_id, 
                         title, 
                         artist_id, 
                         year, 
                         duration) 
                         values(%s, %s, %s, %s, %s) 
                         on conflict (song_id) do nothing
                         ;
""")

artist_table_insert = ("""insert into artists (
                          artist_id, 
                          name, 
                          location, 
                          lattitude, 
                          longitude) 
                          values(%s, %s, %s,%s, %s) 
                          on conflict (artist_id) do nothing
                          ;
""")


time_table_insert = ("""insert into time (start_time, 
                         hour, 
                         day, 
                         week, 
                         month, 
                         year, 
                         weekday) values(%s, %s, %s,%s, %s,%s, %s) 
                         on conflict (start_time) do nothing
                         ;
""")

# FIND SONGS

song_select = ("""SELECT distinct a.song_id, b.artist_id\
               FROM songs a join artists b on a.artist_id = b.artist_id \
               WHERE a.title = (%s) AND b.name = (%s) AND a.duration = (%s);
""")

# QUERY LISTS

create_table_queries = [songplay_table_create, user_table_create, song_table_create, artist_table_create, time_table_create]
drop_table_queries = [songplay_table_drop, user_table_drop, song_table_drop, artist_table_drop, time_table_drop]