'''
Should be similar to todo2.py - user input gets translated to ORM calls
'''

import sys
import os
from transaction import Transaction

t = Transaction('tracker.db')
item = {'item_num':2,'amount':5,'category':'food','date':'Aug 5 2022','desc':'Food for the week'}
t.addTransaction(item)
print(t.runQuery('SELECT * FROM transactions', ()))