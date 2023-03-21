''' 
Should be similar to todolist.py: 
  Acts as the ORM middle-stage between tracker.py and the database.
'''

import sqlite3
import os

class Transaction():
    def __init__(self,db):
        self.db = db
        self.runQuery('''CREATE TABLE IF NOT EXISTS transactions
                    (item_num int, amount int, category text, date date, description text)''',())
        

    def addTransaction(self,item):
        self.runQuery('''INSERT INTO transactions VALUES(?,?,?,?,?)''', (item['item_num'],item['amount'],item['category'],item['date'],item['desc']))

    






    def runQuery(self,query,tuple):
        ''' return all of the uncompleted tasks as a list of dicts.'''
        con= sqlite3.connect(self.db)
        cur = con.cursor() 
        cur.execute(query,tuple)
        tuples = cur.fetchall()
        con.commit()
        con.close()
        return [t for t in tuples]
    
