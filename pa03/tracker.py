'''
Should be similar to todo2.py - user input gets translated to ORM calls
'''

import sys
import os
from transaction import Transaction

t = Transaction('tracker.db')