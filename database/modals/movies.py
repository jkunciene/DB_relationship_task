from database.database import create_table_database, query_database


def create_movies_table():
    query = """CREATE TABLE IF NOT EXISTS movies (
                        moviesId INTEGER PRIMARY KEY AUTOINCREMENT,
                        movie_name TEXT,
                        release_date DATE,                        
                        rating REAL,
                        genre TEXT,
                        studioId INTEGER,
                        boxofficeId INTEGER,
                        FOREIGN KEY (studioId) REFERENCES studios(studioId),
                        FOREIGN KEY (boxofficeId) REFERENCES box_offices(boxofficeId)                 
                       )"""
    create_table_database(query)


query_database("PRAGMA table_info(movies)")
create_movies_table()


# create_table_database("DROP TABLE movies")
