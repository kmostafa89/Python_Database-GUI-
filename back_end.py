
import sqlite3 as sql


def connection():
    conn = sql.connect("books.db")
    cur = conn.cursor()
    cur.execute("CREATE TABLE IF NOT EXISTS book (id INTEGER PRIMARY KEY , title TEXT , author TEXT , year INTEGER , isbn INTEGER)")
    conn.commit()
    conn.close()
    


"""
CREATE TABLE IF NOT EXIST BOOK (id INTEGER PRIMARY KEY ,title TEXT  ,author TEXT ,year INTEGER ,isbn INTEGER)"

INSERT INTO BOOK VALUES (?)


"""

def  insert(title, author , year , isbn):
    conn = sql.connect("books.db")
    cur = conn.cursor()
    cur.execute("INSERT INTO book VALUES(NULL, ?,?,?,?)",(title, author , year , isbn))
    conn.commit()
    conn.close()
    
    
def  view():
    conn = sql.connect("books.db")
    cur = conn.cursor()
    cur.execute("SELECT * FROM book")
    row = cur.fetchall()
    conn.close()
    return row


def delete(id):
    conn = sql.connect('books.db')
    cur = conn.cursor()
    cur.execute("DELETE FROM book WHERE id = ?",(id,) )
    conn.commit()
    conn.close()
    

def search(title = "" , author= "" , year = "" , isbn = ""):
    conn = sql.connect("books.db")
    cur = conn.cursor()
    cur.execute("SELECT * FROM book WHERE title = ? or author = ? or year = ? or isbn = ?",(title , author , year , isbn))
    row = cur.fetchall()
    conn.close()
    return row


def update(id,title,author, year , isbn):
    conn = sql.connect('books.db')
    cur = conn.cursor()
    cur.execute("UPDATE book SET title = ? , author = ? , year = ? , isbn = ? WHERE id = ?  ",(title , author , year , isbn, id))
    conn.commit()
    conn.close()    
