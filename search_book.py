import sqlite3
db_filename = 'mybook.db'

def searchBook(col, data):
    with sqlite3.connect(db_filename) as conn:
        cursor = conn.cursor()

        query = "select * from books where {c} = '{d}'".format(c=col,
                 d=data)
        #print(query)
        cursor.execute(query)
        #cursor.execute(query, {'col': col, 'data': data})

        #for row in cursor.fetchall():
        #    print(row)
        allinfo = cursor.fetchall()
        if len(allinfo) > 0:
            return True
        return False

if __name__ == "__main__":
    searchBook('eng_title', 'Discovering Modern C++')


