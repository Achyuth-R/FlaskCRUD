import os
import psycopg2

conn = psycopg2.connect(
        host="localhost",
        database="Dev_DB",
        user='ApplicationRole',
        password='applicationpassword')


def initDb():
        cur = conn.cursor()
        print(cur)

        cur.execute('DROP TABLE IF EXISTS TestSchema.books;')
        print('creating table TestSchema.books')
        cur.execute('CREATE TABLE TestSchema.books (id serial PRIMARY KEY,'
                                        'title varchar (150) NOT NULL,'
                                        'author varchar (50) NOT NULL,'
                                        'pages_num integer NOT NULL,'
                                        'review text,'
                                        'date_added date DEFAULT CURRENT_TIMESTAMP);'
                                        )
        print('add data to books table')
        cur.execute('INSERT INTO TestSchema.books (title, author, pages_num, review)'
                'VALUES (%s, %s, %s, %s)',
                ('A Tale of Two Cities',
                'Charles Dickens',
                489,
                'A great classic!')
                )


        cur.execute('INSERT INTO TestSchema.books (title, author, pages_num, review)'
                'VALUES (%s, %s, %s, %s)',
                ('Anna Karenina',
                'Leo Tolstoy',
                864,
                'Another great classic!')
                )


        conn.commit()
        cur.close()

def getConnection():
        return conn

def closeConnection():
        conn.commit()
        conn.close()