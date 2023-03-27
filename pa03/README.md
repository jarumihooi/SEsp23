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