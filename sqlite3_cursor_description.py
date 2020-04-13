import sqlite3

db_filename = 'mybook.db'

with sqlite3.connect(db_filename) as conn:
    cursor = conn.cursor()

    cursor.execute("""
select * from books
    """)

    print('books table has these columns:')
    for colinfo in cursor.description:
        print(colinfo)
