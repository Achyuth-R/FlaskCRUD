import os
import psycopg2

conn = psycopg2.connect(
                host="localhost",
                database="Dev_DB",
                user='ApplicationRole',
                password='applicationpassword')

def initDb():
            
        cur = conn.cursor()

        cur.execute('CREATE TABLE IF NOT EXISTS TestSchema.TestTable (id serial PRIMARY KEY,name varchar (150) NOT NULL)')
        print('created table TestSchema.TestTable')

        conn.commit()
        cur.close()
        return conn

def getConnection():
    return conn

def closeConnection():
        conn.commit()
        conn.close()
