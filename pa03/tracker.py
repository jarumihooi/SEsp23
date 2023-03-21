'''
Should be similar to todo2.py - user input gets translated to ORM calls
'''

import sys
import os
from transaction import Transaction

def print_usage():
    ''' print an explanation of how to use this command '''
    print('''usage:
            transation show
            transation showall
            transation showcomplete
            transation add name description
            transation complete item_id
            transation delete item_id
            '''
            )

def print_tactions(tactions):
    ''' print the transaction items '''
    if len(tactions)==0:
        print('no transactions to print')
        return
    print('\n')
    print("%-10s %-10s %-30s %-10s"%('item #','title','desc','completed'))
    print('-'*40)
    for item in tactions:
        values = tuple(item.values()) #(rowid,title,desc,completed)
        print("%-10s %-10s %-30s %2d"%values)

def process_args(arglist):
    ''' examine args and make appropriate calls to Transaction'''
    t = Transaction('tracker.db')
    item = {'item_num': 2, 'amount': 5, 'category': 'food', 'date': 'Aug 5 2022', 'desc': 'Food for the week'}
    t.addTransaction(item)
    print(t.runQuery('SELECT * FROM transactions', ()))
    
    if arglist==[]:
        print_usage()
    # ==== J
    elif arglist[0]=="show":
        print_tactions(t.selectActive())
    elif arglist[0]=="showcat":
        print_tactions(tactions = t.selectAll())
    elif arglist[0]=="addcat":
        print_tactions(t.selectCompleted())
    # ==== end J

    # ==== C
    elif arglist[0]=="4":
        print_tactions(t.selectCompleted())
    elif arglist[0]=="5":
        print_tactions(t.selectCompleted())
    elif arglist[0]=="6":
        print_tactions(t.selectCompleted())

    # ==== end C

    # ==== I
    elif arglist[0] == "6":
        print_tactions(t.selectCompleted())
    elif arglist[0] == "10":
        print_tactions(t.selectCompleted())
    elif arglist[0] == "11":
        print_tactions(t.selectCompleted())

    # ==== end I

    # ==== ML
    elif arglist[0] == "7":
        print_tactions(t.selectCompleted())
    elif arglist[0] == "8":
        print_tactions(t.selectCompleted())
    elif arglist[0] == "9":
        print_tactions(t.selectCompleted())
    # else: #extra failed commands
    #     print(arglist,"is not implemented")
    #     print_usage()

    # ==== end ML

    # ==== this is exxtra code you can use.
    elif arglist[0]=='add':
        if len(arglist)!=3:
            print_usage()
        else:
            todo = {'title':arglist[1],'desc':arglist[2],'completed':0}
            t.add(todo)
    elif arglist[0]=='complete':
        if len(arglist)!= 2:
            print_usage()
        else:
            t.setComplete(arglist[1])
    elif arglist[0]=='delete':
        if len(arglist)!= 2:
            print_usage()
        else:
            t.delete(arglist[1])




    # ==== end extra code




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
                # join everyting after the name as a string
                args = ['add', args[1], " ".join(args[2:])]
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
