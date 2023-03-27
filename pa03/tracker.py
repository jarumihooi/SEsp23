#!/usr/bin/python3
'''
Should be similar to todo2.py - user input gets translated to ORM calls
This is the main executable for the transaction project.
It creates the interface shell which calls ORM sqlite3 calls in transaction.py.
It has been modified from todo2.py. There are new options.
Most of the summarize by date/category do not work,
as this implementation style was considered too difficult
by the two team members investigating this issue.
Known issues: summarize methods are not implemented. Commented code is kept to show progress.
Providing unexpected input may cause an error.
Authors: @Tim Hickey @Jeremy Huey @mengli yang @Ijeoma @Igbogu @Chris Tighe
@Jeremy Huey did the pylint-ing.
Version: 1.0
'''

import sys

# import transaction
from transaction import Transaction

def print_usage():
    ''' print an explanation of how to use this command
    @Jeremy Huey edited this to match our project'''
    # transaction.print_menu()
    print('''usage:
            transaction quit
            transaction modcat item_id new_category - eg. modcat 1 bills
            transaction showall
            transaction day
            transaction month
            transaction year
            transaction add amount category mm/dd/yyyy description - eg. add 23 food 03/02/2022 ate food spaces ok
            transaction delete item_id
            transaction sumcat
            transaction usage
            '''
            )

def print_tactions(tactions):
    ''' print the transaction items - Chris modified to work with transactions'''
    if len(tactions)==0:
        # print('no transactions to print')
        return
    # print('\n')
    print("%-10s %-10s %-10s %-20s %-30s"%('item #','amount','category','date', 'description'))
    print('-'*40)
    for item in tactions:
        values = tuple(item.values()) #(item_num,amount,category,day,month,year,description)
        date = str(values[4])+"/"+str(values[3])+"/"+str(values[5])
        print("%-10s %-10s %-10s %-20s %-30s"%(values[0],values[1],values[2],date,values[6]))

def process_args(arglist):
    ''' examine args and make appropriate calls to Transaction'''
    t = Transaction('tracker.db')

    # Quit is added by @Jeremy Huey, but done in the main loop in toplevel()
    if arglist==[]:
        print_usage()
    # ==== Chris
    elif arglist[0]=="modcat":
        # Assuming that modify means modify category of a transaction
        # (may change if we swap to addtl table for categories)
        t.modify_category(arglist[1], arglist[2])
    elif arglist[0]=="showall":
        print_tactions(t.show_transactions())
    elif arglist[0]=="add":
        if len(arglist) != 5:
            # print(arglist)
            # print("ERROR: ")
            print_usage()
        else:
            date = arglist[3].split("/")
            item = {'amount':arglist[1],'category':arglist[2],'day':date[1],
                    'month':date[0],'year':date[2],'desc':arglist[4]}
            t.add_transaction(item)
    # ==== end Chris

    # ==== I and J @Jeremy Huey @Ijeoma Igbogu
    elif arglist[0] == "delete":
        print_tactions(t.delete_transaction(int(arglist[1])))
    elif arglist[0] == "sumcat":
        t.sum_by_category()
        #print_tactions(t.sum_by_category())
    elif arglist[0] == "usage":
        print_usage()
    # ==== end I and J

    # ==== ML
    elif arglist[0] == "day":
        t.sum_by_day()
        # print_tactions(t.sum_by_day())
    elif arglist[0] == "month":
        t.sum_by_month()
        # print_tactions(t.sum_by_month())
    elif arglist[0] == "year":
        t.sum_by_year()
        # print_tactions(t.sum_by_year())
    else:
        print(arglist,"is not implemented")
        print_usage()
    # ==== end ML
    # end method

def toplevel():
    '''read the command args and process them
    @Jeremy Huey added quit.'''
    if len(sys.argv) == 1:
        # they didn't pass any arguments,
        # so prompt for them in a loop
        print_usage()
        args = []
        quitt = False
        while args != [''] and not quitt:
            args = input("command> ").split(' ')
            if args[0] == 'add':
                # join everyting after the amt,category,date as a string
                args = ['add', args[1], args[2], args[3], " ".join(args[4:])] #bf: changed.
            elif args[0] == 'quit':
                quitt = True
                print("Quitting the transcation shell.")
                continue
            process_args(args)
            print('-' * 40 + '\n' * 1)
    else:
        # read the args and process them
        args = sys.argv[1:]
        process_args(args)
        print('-' * 40 + '\n' * 1)
toplevel()
