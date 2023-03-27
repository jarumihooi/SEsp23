Describe app ====
Authors: @Tim Hickey @Jeremy Huey @mengli yang @Ijeoma @Igbogu @Chris Tighe

This app creates a database locally and then accounts for transactions that
the user has made in the past (apparently). 

USAGE =====
To run you do: $ python3 tracker.py
This will open the program to start accepting commands in a shell-esque manner. 
Eg. You bought food:
("command> " means you should type the following text into the shell, don't literally type the text "command> ")
command> add 3 food 03/02/2022 description of tasty food with spaces
Typing this will add this to your database. No printout of success is printed. 
Then type: 
command> showall 
to view the changes you've made. 
The usage of this app is printed each time a new loop is made. Use that to find the other commands, or run: command> usage

Background code ====
The background supporting code is in transaction.py. This acts as the ORM middle-stage between tracker.py and the database.
In this code, methods are called which return the sqlite3 queries that query/modify the database. 


run pylint ==== 

************* Module tracker
tracker.py:47:0: C0303: Trailing whitespace (trailing-whitespace)
tracker.py:52:0: C0301: Line too long (123/100) (line-too-long)
tracker.py:63:0: C0301: Line too long (125/100) (line-too-long)
tracker.py:121:0: C0304: Final newline missing (missing-final-newline)
tracker.py:37:10: C0209: Formatting a regular string which could be a f-string (consider-using-f-string)
tracker.py:42:14: C0209: Formatting a regular string which could be a f-string (consider-using-f-string)
tracker.py:46:4: C0103: Variable name "t" doesn't conform to snake_case naming style (invalid-name)
tracker.py:44:0: R0912: Too many branches (13/12) (too-many-branches)
tracker.py:8:0: W0611: Unused import os (unused-import)
tracker.py:10:0: W0611: Unused import transaction (unused-import)

-----------------------------------
Your code has been rated at 8.39/10

************* Module transaction
transaction.py:31:0: C0301: Line too long (103/100) (line-too-long)
transaction.py:38:0: C0301: Line too long (120/100) (line-too-long)
transaction.py:40:0: C0301: Line too long (162/100) (line-too-long)
transaction.py:43:0: C0301: Line too long (103/100) (line-too-long)
transaction.py:64:0: W0301: Unnecessary semicolon (unnecessary-semicolon)
transaction.py:11:0: C0103: Function name "toDict" doesn't conform to snake_case naming style (invalid-name)
transaction.py:11:11: C0103: Argument name "t" doesn't conform to snake_case naming style (invalid-name)
transaction.py:23:0: C0112: Empty class docstring (empty-docstring)
transaction.py:29:8: C0103: Attribute name "db" doesn't conform to snake_case naming style (invalid-name)
transaction.py:28:23: C0103: Argument name "db" doesn't conform to snake_case naming style (invalid-name)
transaction.py:35:4: C0103: Method name "addTransaction" doesn't conform to snake_case naming style (invalid-name)
transaction.py:41:4: C0103: Method name "modifyCategory" doesn't conform to snake_case naming style (invalid-name)
transaction.py:45:4: C0103: Method name "showTransactions" doesn't conform to snake_case naming style (invalid-name)
transaction.py:52:4: C0116: Missing function or method docstring (missing-function-docstring)
transaction.py:64:8: W0107: Unnecessary pass statement (unnecessary-pass)
transaction.py:90:4: C0103: Method name "runQuery" doesn't conform to snake_case naming style (invalid-name)
transaction.py:90:30: W0622: Redefining built-in 'tuple' (redefined-builtin)
transaction.py:8:0: W0611: Unused import os (unused-import)

-----------------------------------
Your code has been rated at 4.86/10



run pytest ====
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

run tracker.py ====
transcript of trying things. 