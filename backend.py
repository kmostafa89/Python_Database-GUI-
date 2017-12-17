import sqlite3 as sql

class Database:
    
    
    def __init__(self , db="test.db"):
        self.conn = sql.connect(db)
        self.cur = self.conn.cursor()
        self.cur.execute("CREATE TABLE IF NOT EXISTS drugs(id INTEGER PRIMARY KEY, name TEXT , cause TEXT , price REAL)")
        self.conn.commit()
        
    def view(self):
        self.cur.execute("SELECT * FROM drugs")
        rows = self.cur.fetchall()
        return rows
    
    def search(self ,name="" , cause="" , price=""):
        self.cur.execute("SELECT * FROM drugs WHERE name =? OR cause = ? OR price = ?", ( name , cause , price))
        row = self.cur.fetchall()
        return row
    
    
    def insert(self, name , cause , price):
        self.cur.execute("INSERT INTO drugs VALUES(NULL , ?, ? , ?)",(name ,cause , price))
        self.conn.commit()
        
    def update(self, id , name , cause , price):
        self.cur.execute("UPDATE drugs SET name = ? , cause= ? , price = ? WHERE id = ?",(name , cause , price,id))
        self.conn.commit()
        
    def delete(self , id):
        self.cur.execute("DELETE FROM drugs WHERE id = ? ", (id, ))
        self.conn.commit()
        
database =Database("test.db")
#database.insert(name = "ciais",cause = "Erection" ,price =10.99)
#database.delete(1)
#database.update(6, name = "cialis", cause = "erection", price = "10.99999")
print(database.search(name="cialis"))
#print(database.view())
