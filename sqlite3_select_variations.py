import sqlite3

db_filename = 'mybook.db'

with sqlite3.connect(db_filename) as conn:
    cursor = conn.cursor()

    cursor.execute("""
select chi_title, eng_title, author from books
    """)
    chi_title, eng_title, author = cursor.fetchone()

    print("Book details for {:20} {:20} {:20}".format(
        chi_title, eng_title, author
    ))
