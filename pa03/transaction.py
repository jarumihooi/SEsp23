''' 
Should be similar to todolist.py: 
  Acts as the ORM middle-stage between tracker.py and the database.
'''

import sqlite3
import os

def toDict(t):
    '''This method was reformatted with our 5 cols, we can print these dictts.
    t is a tuple (item_num,amount,category,date,description)
    Chris modified this to work with our dictionary structure.'''
    # print('t='+str(t))
    dictt = {'item_num':t[0], 'amount':t[1], 'category text':t[2], 'date':t[3], 'desc':t[4]}
    return dictt

class Transaction():
    def __init__(self,db):
        self.db = db
        self.runQuery('''CREATE TABLE IF NOT EXISTS transactions
                    (amount int, category text, date text, description text)''',())

    # ==== J

    # ==== end J

    # ==== C

    def addTransaction(self,item):
        '''Chris wrote this- adds a transaction to the database'''
        return self.runQuery("INSERT INTO transactions VALUES (?,?,?,?)", (item['amount'],item['category'],item['date'],item['desc']))

    # This doesn't match the original planned technique for categories being pre-defined; instead they are strings, so being able to update them would make sense.
    def modifyCategory(self,row_id,new_cat):
        '''Chris wrote this- modifies the category of a transaction'''
        return self.runQuery("UPDATE transactions SET category=(?) WHERE rowid=(?)",(new_cat,row_id))
    
    def showTransactions(self):
        '''Chris wrote this- shows all transactions in the database'''
        return self.runQuery("SELECT rowid,* FROM transactions",())

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
        ''' return all of the uncompleted tasks as a list of dicts. 
            Chris modified to make the dictionary structure work with transactions.'''
        con= sqlite3.connect(self.db)
        cur = con.cursor() 
        cur.execute(query,tuple)
        tuples = cur.fetchall()
        con.commit()
        con.close()
        return [toDict(t) for t in tuples]
    
