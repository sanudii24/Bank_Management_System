#database management banking
import mysql.connector as a
con=a.connect(host="localhost",user="root",password="S3r$7Lp!wB#2xQz4",database="library")


import mysql.connector as sql 
mydb=sql.connect(
    host="localhost",
    password="S3r$7Lp!wB#2xQz4",
    user="root",
    database="bank"
)
cursor=mydb.cursor()

def db_query(str):
    cursor.execute(str)
    result=cursor.fetchall()
    return result

def createcustomertable():
    cursor.execute('''
               CREATE TABLE IF NOT EXISTS customers
               (username VARCHAR(20) NOT NULL,
               password VARCHAR(20)NOT NULL,
               name VARCHAR(20) NOT NULL,
               age INTEGER NOT NULL,
               city VARCHAR(20)NOT NULL,
               balance INTEGER NOT NULL,
               account_number INTEGER NOT NULL,
               status BOOLEAN)
               ''')
mydb.commit()
if __name__=="__main__":
    createcustomertable()

