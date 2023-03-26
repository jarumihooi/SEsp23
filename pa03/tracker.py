'''
Should be similar to todo2.py - user input gets translated to ORM calls
'''

import sys
import os
from transaction import Transaction

def print_usage():
    ''' print an explanation of how to use this command '''
    print('''usage:
            transaction show
            transaction showall
            transactions by date
            transactions by month
            transactions by year
            transaction showcomplete
            transaction add amount category date description
            transaction complete item_id
            transaction delete item_id
            '''
            )

def print_tactions(tactions):
    ''' print the transaction items - Chris modified to work with transactions'''
    if len(tactions)==0:
        # print('no transactions to print')
        return
    print('\n')
    print("%-10s %-10s %-10s %-20s %-30s"%('item #','amount','category','date', 'description'))
    print('-'*40)
    for item in tactions:
        values = tuple(item.values()) #(item_num,amount,category,date,description)
        print("%-10s %-10s %-10s %-20s %-30s"%values)

def process_args(arglist):
    ''' examine args and make appropriate calls to Transaction'''
    t = Transaction('tracker.db')
    
    if arglist==[]:
        print_usage()
    # ==== Chris
    elif arglist[0]=="modcat":
        # Assuming that modify means modify category of a transaction (may change if we swap to addtl table for categories)
        t.modifyCategory(arglist[1],arglist[2])
    elif arglist[0]=="showall":
        print_tactions(t.showTransactions())
    elif arglist[0]=="add":
        if len(arglist) != 5:
            print_usage()
        else:
            item = {'amount':arglist[1],'category':arglist[2],'date':arglist[3],'desc':arglist[4]}
            t.addTransaction(item)

    # ==== end Chris

    # ==== I
    elif arglist[0] == "6":
        print_tactions(t.selectCompleted())
    elif arglist[0] == "10":
        print_tactions(t.selectCompleted())
    elif arglist[0] == "11":
        print_tactions(t.selectCompleted())

    # ==== end I

    # ==== ML
    elif arglist[0] == "date":
        print_tactions(t.sum_by_date())
    elif arglist[0] == "month":
        print_tactions(t.sum_by_month())
    elif arglist[0] == "year":
        print_tactions(t.sum_by_year())
    else:
        print(arglist,"is not implemented")
        print_usage()
    # ==== end ML


def toplevel():
    ''' read the command args and process them'''
    if len(sys.argv) == 1:
        # they didn't pass any arguments,
        # so prompt for them in a loop
        print_usage()
        args = []
        quitt = False;
        while args != [''] and not quitt:
            args = input("command> ").split(' ')
            if args[0] == 'add':
                # join everyting after the amt,category,date as a string
                args = ['add', args[1], args[2], args[3], " ".join(args[4:])]
            elif args[0] == 'quit':
                quitt = True
                print("Quitting the transcation shell.")
                continue
            process_args(args)
            print('-' * 40 + '\n' * 3)


    else:
        # read the args and process them
        args = sys.argv[1:]
        process_args(args)
        print('-' * 40 + '\n' * 3)


toplevel()
