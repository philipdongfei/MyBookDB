# sqlite3_create_schema.py

import os
import sqlite3

db_filename = 'mybook.db'
schema_filename = 'todo_schema.sql'

db_is_new = not os.path.exists(db_filename)

with sqlite3.connect(db_filename) as conn:
    if db_is_new:
        print('Creating schema')
        with open(schema_filename, 'rt') as f:
            schema = f.read()
        conn.executescript(schema)

        print('Inserting initial data')

        while True:
            chi_title = input("Enter the chinese title: ")
            eng_title = input("Enter the english title: ")
            author = input("Enter the author: ")
            language = input("Enter the language: ")
            volume = int(input("Enter the volume: "))
            price = float(input("Enter the price: "))
            publisher = input("Enter the publisher: ")

            insert_sql = "insert into books (chi_title, eng_title, \
                author, language, volume, price, publisher) values \
                ('{a}','{b}','{c}','{d}','{e}','{f}','{g}')".format(a=chi_title,
                                                      b=eng_title,
                                                      c=author,
                                                      d=language,
                                                      e=volume,
                                                      f=price,
                                                      g=publisher)
            print(insert_sql+'\n')
            conn.executescript(insert_sql)
            q = input("is quit(yes/no)?")
            if q != 'no':
                break

        print('insert done')
    else:
        print('Database exists, assume schema does, too.')
