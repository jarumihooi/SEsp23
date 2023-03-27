'''
Should be similar to todolist.py:
  Acts as the ORM middle-stage between tracker.py and the database.
  Authors: @Tim Hickey @Jeremy Huey @mengli yang @Ijeoma @Igbogu @Chris Tighe
  @Jeremy Huey did the pylint-ing.
  Version: 1.0
'''

import sqlite3


def to_dict(t):
    '''This method was reformatted with our 5 cols, we can print these dictts.
    t is a tuple (item_num,amount,category,date,description)
    @Jeremy Huey added the starter code.
    @Chris Tighe modified this to work with our dictionary structure.
   '''
    # print('t='+str(t))
    dictt = {'item_num': t[0], 'amount': t[1], 'category text': t[2], 'day': t[3],
             'month': t[4], 'year': t[5], 'desc': t[6]}
    return dictt


class Transaction:  # lmao did you know you dont need a () after this? i didnt!
    '''
    This class creates the code that runs the transaction account tracker.
    The initializer creates a db file.
    All of the functional methods for the project are here and called by tracker.py
    The self.runQuery returns a tuple. Then we send it into to_dict(t) and gets reformatted
    into a dictionary for printing. 
    This information is then fed into tracker.print_tactions(tactions) to print.
    '''

    def __init__(self, db):
        self.db = db
        self.run_query('''CREATE TABLE IF NOT EXISTS transactions
                    (amount int, category text, day int, month int,
                     year int, description text)''', ())

    # ==== C

    def add_transaction(self, item):
        '''Chris wrote this- adds a transaction to the database'''
        return self.run_query("INSERT INTO transactions VALUES (?,?,?,?,?,?)",
                              (item['amount'], item['category'], item['day'],
                               item['month'], item['year'], item['desc']))

    # This doesn't match the original planned technique for categories being pre-defined;
    # instead they are strings, so being able to update them would make sense.
    def modify_category(self, row_id, new_cat):
        '''Chris wrote this- modifies the category of a transaction'''
        return self.run_query(
            "UPDATE transactions SET category=(?) WHERE rowid=(?)", (new_cat, row_id))

    def show_transactions(self):
        '''Chris wrote this- shows all transactions in the database'''
        return self.run_query("SELECT rowid,* FROM transactions", ())

    # ==== end C

    # ==== I and J
    def delete_transaction(self, row_id):
        '''This deletes an entry in the database via row.
        written by @Ijeoma Igbogu'''
        return self.run_query("DELETE FROM transactions WHERE rowid=(?)", (row_id,))

    def sum_by_category(self):
        '''This should categorize by category but does not work with the version we have.
        written by @Ijeoma Igbogu
        edited by @Jeremy Huey'''
        print("WARNING: Sum by Category is non-implemented")
        # return self.runQuery("SELECT rowid SUM(amount) FROM transactions GROUP BY category",())

    def print_menu(self):
        '''edited by @Jeremy Huey'''
        # not implemented
        # pass

    # ==== end I

    # ==== ML

    def sum_by_day(self):
        '''summarize transactions by date @mengli yang
        edited by @Jeremy Huey'''
        print("WARNING: Sum by Category is non-implemented")
        # return self.runQuery("SELECT * FROM transactions WHERE date = 26", ())

    def sum_by_month(self):
        '''summarize transactions by month @mengli yang
        edited by @Jeremy Huey'''
        print("WARNING: Sum by Category is non-implemented")
        # return self.runQuery("SELECT * FROM transactions WHERE date = 03",())

    def sum_by_year(self):
        '''summarize transactions by year @mengli yang
        edited by @Jeremy Huey'''
        print("WARNING: Sum by Category is non-implemented")
        # return self.runQuery("SELECT * FROM transactions WHERE date = 2023",())

    # ==== end ML

    def run_query(self, query: object, tuplee: object) -> object:
        ''' return all of the uncompleted tasks as a list of dicts.
            Chris modified to make the dictionary structure work with transactions.'''
        con = sqlite3.connect(self.db)
        cur = con.cursor()
        cur.execute(query, tuplee)
        tuples = cur.fetchall()
        con.commit()
        con.close()
        return [to_dict(t) for t in tuples]
