import sqlite3

db_filename = 'mybook.db'

with sqlite3.connect(db_filename) as conn:
    cursor = conn.cursor()

    cursor.execute("""
select id, chi_title, eng_title, author, language, volume, price,
publisher from books
    """)

    '''

    print('{:3} {:20} {:20} {:20} {:8} {:2} {:7} {:20} '.format("id",
                                                                     "chi_title",
                                                                     "eng_title",
                                                                     "auther",
                                                                     "language",
                                                                     "volume",
                                                                     "price",
                                                                     "publisher"))
    '''
    for row in cursor.fetchall():
        book_id, chi_title, eng_title, author, language, volume,price, publisher = row
        print('{:2d} {:20} {:20} {:20} {:8} {:2d} {:-7.02f} {:20} '.format(
            book_id, chi_title, eng_title, author, language, volume,
            price, publisher))
