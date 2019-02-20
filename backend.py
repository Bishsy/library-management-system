import sqlite3
def connect():
	conn=sqlite3.connect("books.db")
	cur=conn.cursor()
	cur.execute("CREATE TABLE IF NOT EXISTS book(id INTEGER PRIMARY KEY, title TEXT,author TEXT, year INTEGER, isbn INTEGER)")
	conn.commit()
	conn.close()
def insert(title,author,year,isbn):
	conn=sqlite3.connect("books.db")
	cur=conn.cursor()
	cur.execute("INSERT INTO book VALUES(NULL,?,?,?,?)",(title,author,year,isbn))
	conn.commit()
	conn.close()
def view():
	conn=sqlite3.connect("books.db")
	cur=conn.cursor()
	cur.execute("SELECT * FROM book")
	rows=cur.fetchall()
	conn.close()
	return rows
def search(title="",author="",year="",isbn=""):
	conn=sqlite3.connect("books.db")
	cur=conn.cursor()
	cur.execute("SELECT * FROM book where title=? or author=? or year=? or isbn=?",(title,author,year,isbn))
	rows=cur.fetchall()
	conn.close()
	return rows
def delete(id):
	conn=sqlite3.connect("books.db")
	cur=conn.cursor()
	cur.execute("DELETE FROM book where id=?",(id,))
	conn.commit()
	conn.close()
def update(id,title,author,year,isbn):
	conn=sqlite3.connect("books.db")
	cur=conn.cursor()
	cur.execute("UPDATE book SET title=?, author=?, year=?,isbn=? WHERE id=?",(title,author,year,isbn,id))
	conn.commit()
	conn.close()
connect()

insert("The Bible ","John snow",1918,912345311)
#print(delete(3))
#update(4,"The moon","John smile",1917,909099)
print(view())
#print(search(author="John smile"))