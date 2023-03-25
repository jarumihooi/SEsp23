''' 
Should be similar to todolist.py: 
  Acts as the ORM middle-stage between tracker.py and the database.
'''

import sqlite3
import os

def toDict(t):
    '''This method was reformatted with our 5 cols, we can print these dictts.
    t is a tuple (rowid,title, desc,completed)'''
    print('t='+str(t))
    dictt = {'item_num':t[0], 'amount':t[1], 'category text':t[2], 'date':t[3], 'description':t[4]}
    return dictt

class Transaction():
    def __init__(self,db):
        self.db = db
        self.runQuery('''CREATE TABLE IF NOT EXISTS transactions
                    (item_num int, amount int, category text, date date, description text)''',())

    # ==== J

    # ==== end J

    # ==== C

    def addTransaction(self,item):
        self.runQuery('''INSERT INTO transactions VALUES (?,?,?,?,?)''', (item['item_num'],item['amount'],item['category'],item['date'],item['desc']))

    # ==== end C

    # ==== I

    # ==== end I

    # ==== ML

    # ==== end ML

    # ==== The original given code ====
    def selectActive(self):
        ''' return all of the uncompleted tasks as a list of dicts.'''
        return self.runQuery("SELECT rowid,* from todo where completed=0",())

    def selectAll(self):
        ''' return all of the tasks as a list of dicts.'''
        return self.runQuery("SELECT rowid,* from todo",())

    def selectCompleted(self):
        ''' return all of the completed tasks as a list of dicts.'''
        return self.runQuery("SELECT rowid,* from todo where completed=1",())

    def add(self,item):
        ''' create a todo item and add it to the todo table '''
        return self.runQuery("INSERT INTO todo VALUES(?,?,?)",(item['title'],item['desc'],item['completed']))

    def delete(self,rowid):
        ''' delete a todo item '''
        return self.runQuery("DELETE FROM todo WHERE rowid=(?)",(rowid,))

    def setComplete(self,rowid):
        ''' mark a todo item as completed '''
        return self.runQuery("UPDATE todo SET completed=1 WHERE rowid=(?)",(rowid,))

    # ==== end orig code section.
    






    def runQuery(self,query,tuple):
        ''' return all of the uncompleted tasks as a list of dicts.'''
        con= sqlite3.connect(self.db)
        cur = con.cursor() 
        cur.execute(query,tuple)
        tuples = cur.fetchall()
        con.commit()
        con.close()
        return [t for t in tuples]
    
