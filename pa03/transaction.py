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
    def delete_transaction(self, row_id):
        return self.runQuery("DELETE FROM transactions WHERE rowid=(?)", (row_id,))

    def sum_by_catergory(self):
        return self.runQuery("SELECT rowid SUM(amount) FROM transactions GROUP BY category",())

    def print_menu(self):
        """
        1. addTransaction - pass a transaction to insert
        2. modifyCategory- use row id, category
        3. showTransactions
        4. delete_transaction - use row id
        5. sum_by_category
        6. sum_by_date
        7. sum_by_month
        8. sum_by_year
        """


    # ==== end I

    # ==== ML
    def sum_by_date(self):
        '''summarize transactions by date @mengli yang'''
        return self.runQuery("SELECT * FROM transactions WHERE DATE(date) = '2023-03-26'", ())

    def sum_by_month(self):
        '''summarize transactions by month @mengli yang'''
        return self.runQuery("SELECT * FROM transactions WHERE strftime('%m', date) = '03'",())

    def sum_by_year(self):
        '''summarize transactions by year @mengli yang'''
        return self.runQuery("SELECT * FROM transactions WHERE strftime('%Y', date) = '2023'",())
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
    
