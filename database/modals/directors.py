from database.database import create_table_database, query_database


def create_directors_table():
    query = """CREATE TABLE IF NOT EXISTS directors (
                        directorsId INTEGER PRIMARY KEY AUTOINCREMENT,
                        Name TEXT)"""
    create_table_database(query)


def create_directors_movies_table():
    query = """CREATE TABLE IF NOT EXISTS directors_movies (
                        directors_movies_Id INTEGER PRIMARY KEY AUTOINCREMENT,  
                        directorsId int,
                        moviesId int,
                        FOREIGN KEY (directorsId) REFERENCES directors(directorsId)                
                        FOREIGN KEY (moviesId) REFERENCES movies(moviesId))"""
    create_table_database(query)


create_directors_table()
create_directors_movies_table()
query_database("PRAGMA table_info(directors)")
query_database("PRAGMA table_info(directors_movies)")
