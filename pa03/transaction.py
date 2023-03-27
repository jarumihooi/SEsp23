''' 
Should be similar to todolist.py: 
  Acts as the ORM middle-stage between tracker.py and the database.
  Authors: @Tim Hickey @Jeremy Huey @mengli yang @Ijeoma @Igbogu @Chris Tighe
'''

import sqlite3
import os

def toDict(t):
    '''This method was reformatted with our 5 cols, we can print these dictts.
    t is a tuple (item_num,amount,category,date,description)
    @Jeremy Huey added the starter code.
    @Chris Tighe modified this to work with our dictionary structure.
   '''
    # print('t='+str(t))
    dictt = {'item_num':t[0], 'amount':t[1], 'category text':t[2], 'day':t[3],
             'month':t[4], 'year':t[5], 'desc':t[6]}
    return dictt

class Transaction():
    '''

    '''
    def __init__(self,db):
        self.db = db
        self.runQuery('''CREATE TABLE IF NOT EXISTS transactions
                    (amount int, category text, day int, month int, year int, description text)''',())

    # ==== C

    def addTransaction(self,item):
        '''Chris wrote this- adds a transaction to the database'''
        return self.runQuery("INSERT INTO transactions VALUES (?,?,?,?,?,?)", 
                             (item['amount'],item['category'],item['day'],item['month'],item['year'],item['desc']))

    # This doesn't match the original planned technique for categories being pre-defined; instead they are strings, so being able to update them would make sense.
    def modifyCategory(self,row_id,new_cat):
        '''Chris wrote this- modifies the category of a transaction'''
        return self.runQuery("UPDATE transactions SET category=(?) WHERE rowid=(?)",(new_cat,row_id))
    
    def showTransactions(self):
        '''Chris wrote this- shows all transactions in the database'''
        return self.runQuery("SELECT rowid,* FROM transactions",())

    # ==== end C

    # ==== I and J
    def delete_transaction(self, row_id):
        return self.runQuery("DELETE FROM transactions WHERE rowid=(?)", (row_id,))

    def sum_by_catergory(self):
        return self.runQuery("SELECT rowid SUM(amount) FROM transactions GROUP BY category",())

    def print_menu(self):
        print("""
        (Note <> show what to type, do not actually type these in the command request.)
        To use in bash, run as: $ ./tracker.py <add a command from below here>
        1. add < - pass a transaction to insert
        2. modifyCategory- use row id, category
        3. showTransactions
        4. delete_transaction - use row id
        5. sum_by_category
        6. sum_by_date
        7. sum_by_month
        8. sum_by_year
        9. quit
        """)


    # ==== end I

    # ==== ML
    def sum_by_day(self):
        '''summarize transactions by date @mengli yang'''
        return self.runQuery("SELECT * FROM transactions WHERE date = 26", ())

    def sum_by_month(self):
        '''summarize transactions by month @mengli yang'''
        return self.runQuery("SELECT * FROM transactions WHERE date = 03",())

    def sum_by_year(self):
        '''summarize transactions by year @mengli yang'''
        return self.runQuery("SELECT * FROM transactions WHERE date = 2023",())
    # ==== end ML


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
    
