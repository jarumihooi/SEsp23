Version 1.0
Describe app ====
Authors: @Tim Hickey @Jeremy Huey @mengli yang @Ijeoma Igbogu @Chris Tighe

This app creates a database locally and then accounts for transactions that
the user has made in the past (apparently). The program accepts commands in a shell-esque manner. 
The categories/columns for the database are: (item_num,amount,category,day,month,year,description)
The add command automatically adds the item_num, which is the rowid by which sql stores the data. 

This is a sample interface: 
item #     amount     category   date                 description
----------------------------------------
1          3          food       8/23/2022            Food for the week
2          23         food       3/2/2022             ate fofofofofod
----------------------------------------

Usage:
To run you do: $ python3 tracker.py
("command> " means you should type the following text into the shell, don't literally type the text "command> ")
To start using, try to add a food transaction: Eg. You bought food:
command> add 3 food 03/02/2022 description of tasty food with spaces
Typing this will add this to your database. No printout of success is printed. 
Then type: 
command> showall 
to view the changes you've made. 
The usage of this app is printed each time a new loop is made. Use that to find the other commands, or run: command> usage

Background code ====
The background supporting code is in transaction.py. This acts as the ORM middle-stage between tracker.py and the database.
In this code, methods are called which return the sqlite3 queries that query/modify the database. 
We suspect that sqlite3 queries return tuples. 

run pylint ==== 
************* Module tracker
tracker.py:44:10: C0209: Formatting a regular string which could be a f-string (consider-using-f-string)
tracker.py:49:14: C0209: Formatting a regular string which could be a f-string (consider-using-f-string)
tracker.py:53:4: C0103: Variable name "t" doesn't conform to snake_case naming style (invalid-name)     
tracker.py:51:0: R0912: Too many branches (13/12) (too-many-branches)

------------------------------------------------------------------
Your code has been rated at 9.33/10 (previous run: 9.03/10, +0.30)
We did not wish to change the rest of these suggestions, as the code works as intended. 

************* Module transaction
transaction.py:12:12: C0103: Argument name "t" doesn't conform to snake_case naming style (invalid-name)
transaction.py:35:8: C0103: Attribute name "db" doesn't conform to snake_case naming style (invalid-name)
transaction.py:34:23: C0103: Argument name "db" doesn't conform to snake_case naming style (invalid-name)

------------------------------------------------------------------
Your code has been rated at 9.09/10 (previous run: 8.29/10, +0.81)
We did not wish to change the rest of these suggestions, as the code works as intended. 

run pytest ==================
Launching pytest with arguments /Users/jomogbogu/Desktop/lk/main.py --no-header --no-summary -q in /Users/jomogbogu/Desktop/lk

============================= test session starts ==============================
collecting ... collected 4 items

main.py::test_addTransaction PASSED                                      [ 25%]
main.py::test_showTransactions PASSED                                    [ 50%][{'item_num': 1, 'amount': 23, 'category text': 'food', 'day': 5, 'month': 12, 'year': 2023, 'desc': 'grocceries'}, {'item_num': 2, 'amount': 500, 'category text': 'travel', 'day': 31, 'month': 7, 'year': 2023, 'desc': 'hotel'}, {'item_num': 3, 'amount': 6700, 'category text': 'rent', 'day': 16, 'month': 3, 'year': 2023, 'desc': 'mortgage'}]

main.py::test_modifyCategory PASSED                                      [ 75%]
main.py::test_delete_transaction PASSED                                  [100%]

============================== 4 passed in 3.23s ===============================

Process finished with exit code 0

Launching pytest with arguments /Users/jomogbogu/Desktop/lk/main.py --no-header --no-summary -q in /Users/jomogbogu/Desktop/lk

============================= test session starts ==============================
collecting ... collected 4 items

main.py::test_addTransaction PASSED                                      [ 25%]
main.py::test_showTransactions PASSED                                    [ 50%]
main.py::test_modifyCategory PASSED                                      [ 75%]
main.py::test_delete_transaction PASSED                                  [100%]

============================== 4 passed in 1.46s ===============================

Process finished with exit code 0

kay@Zeffi:/mnt/c/Users/J/Documents/Classes/Class+Sp+2023/1_SE/SEsp23/pa03$ pytest test_transaction.py 
====================================================================================== test session starts =======================================================================================
platform linux -- Python 3.10.6, pytest-7.2.2, pluggy-1.0.0
rootdir: /mnt/c/Users/J/Documents/Classes/Class+Sp+2023/1_SE/SEsp23/pa03
plugins: anyio-3.6.2
collected 5 items

test_transaction.py .....                                                                                                                                                                  [100%]

======================================================================================= 5 passed in 0.46s ========================================================================================

run tracker.py ====
See transcript.txt 
