## test_with_unittest.py
import unittest
import sqlite3
import transaction
import pandas as pd
import csv

''' create a table to store the Brandeis course data'''

con = sqlite3.connect('l.db')
cur = con.cursor()

cur.execute("DROP TABLE IF EXISTS transactions")
tra = transaction.Transaction("l.db")

cur.execute("SELECT * FROM transactions")
print(cur.fetchone())
con.close()

tra.modifyCategory(1, "retail")
x = tra.showTransactions()
print(x)





# creating interval objects

#i  = {'item_num': t[0], 'amount': t[1], 'category text': t[2], 'date': t[3], 'desc': t[4]}

# #(item_num,amount,category,date,description)
t = {"amount":23, "category":"food","day":5, "month": 12, "year":2023,"desc":"grocceries"}
t1= {"amount":500, "category":"travel", "day":31, "month": 7, "year":2023,"desc":"hotel"}
t2= {"amount":6700, "category":"rent", "day":16, "month": 3, "year":2023,"desc":"mortgage"}

x = tra.showTransactions()
print(x)

#testing the constructor
def test_addTransaction():
    """
    Testing the addTransaction
    :return: boolean
    """

    x = tra.addTransaction(t)
    x = tra.addTransaction(t1)
    x = tra.addTransaction(t2)
    con = sqlite3.connect('l.db')
    cur = con.cursor()
    cur.execute("SELECT * FROM transactions where amount=23")
    x= cur.fetchone()
    assert x == (23, 'food', 5, 12, 2023, 'grocceries')
    cur.execute("SELECT * FROM transactions where amount=500")
    x = cur.fetchone()
    assert x == (500, 'travel', 31, 7, 2023, 'hotel')
    cur.execute("SELECT * FROM transactions where amount=6700")
    x = cur.fetchone()
    assert x == (6700, 'rent', 16, 3, 2023, 'mortgage')
    con.close()


def test_showTransactions():
    x = tra.showTransactions()
    print(x)
    assert x[0] == {'amount': 23,
                         'category text': 'food',
                         'day': 5,
                         'desc': 'grocceries',
                         'item_num': 1,
                        'month': 12,
                        'year': 2023}

    assert x[1] == {'amount': 500,
                    'category text': 'travel',
                    'day': 31,
                    'desc': 'hotel','item_num': 2,
                    'month': 7,
                    'year': 2023}

#index out of bound error
def test_sum_by_day():
    x = tra.sum_by_day()
    assert x==[]

# # #index out of bound error
# def test_sum_by_month():
#     x = tra.sum_by_month()
#     assert x == []
# 
# #index out of bound error
# def test_sum_by_year():
#     x = tra.sum_by_year()
#     assert x == []



# def test_sum_by_catergory():
#     con = sqlite3.connect('l.db')
#     cur = con.cursor()
#     cur.execute("SELECT * FROM transactions where amount=23")
#     z = tra.showTransactions()
#
#     y = cur.fetchone()
#     x = tra.sum_by_catergory()
#     assert x=="k"

def test_modifyCategory():

    tra.modifyCategory(1, "retail")
    x = tra.showTransactions()
    assert x[0] ==   {'amount': 23,
                     'category text': 'retail',
                     'day': 5,
                     'desc': 'grocceries',
                     'item_num': 1,
                     'month': 12,
                     'year': 2023}

def test_delete_transaction():
    x = tra.delete_transaction(row_id=0)
    y = tra.showTransactions()
    unittest.assertFalsex=(x, y)