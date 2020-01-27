from database.database import create_table_database, query_database


def create_box_offices_table():
    query = """CREATE TABLE IF NOT EXISTS box_offices (
                        boxofficeId INTEGER PRIMARY KEY AUTOINCREMENT,
                        gross REAL)"""
    create_table_database(query)

query_database("PRAGMA table_info(box_offices)")
create_box_offices_table()
