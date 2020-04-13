import os
import sqlite3
from search_book import searchBook
db_filename = 'mybook.db'


def read_file(datafile):
    if os.path.exists(datafile):
        with open(datafile) as file_object:
            lines = file_object.readlines()
        return lines
    else:
        print("%s not exists" % datafile)
        return ''

def insert_book(lines):
    with sqlite3.connect(db_filename) as conn:
        for line in lines:
            cols = line.split(',')
            chi_title = cols[0]
            if searchBook('chi_title', chi_title):
                continue
            eng_title = cols[1]
            if searchBook('eng_title', eng_title):
                continue
            author = cols[2]
            if cols[3]:
                language = cols[3]
            else:
                language = 'Chinese'
            if cols[4]:
                volume = int(cols[4])
            else:
                volume = 1
            price = float(cols[5])
            publisher = cols[6]

            insert_sql = "insert into books (chi_title, eng_title, \
                author, language, volume, price, publisher) values \
                ('{a}','{b}','{c}','{d}','{e}','{f}','{g}')".format(a=chi_title,
                                                      b=eng_title,
                                                      c=author,
                                                      d=language,
                                                      e=volume,
                                                      f=price,
                                                      g=publisher)

            conn.executescript(insert_sql)
            print('insert one\n')
        print('done')

if __name__ == '__main__':
    lines = read_file('books.txt')
    if lines:
        insert_book(lines)

