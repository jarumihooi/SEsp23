'''
Should be similar to todo2.py - user input gets translated to ORM calls
'''

import sys
import os
from transaction import Transaction

def print_usage():
    ''' print an explanation of how to use this command '''
    print('''usage:
            todo show
            todo showall
            todo showcomplete
            todo add name description
            todo complete item_id
            todo delete item_id
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
    elif arglist[0]=="quit":

    elif arglist[0]=="show":
        print_tactions(t.selectActive())
    elif arglist[0]=="showcat":
        print_tactions(tactions = t.selectAll())
    elif arglist[0]=="showcomplete":
        print_tactions(t.selectCompleted())
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
    else:
        print(arglist,"is not implemented")
        print_usage()


def toplevel():
    ''' read the command args and process them'''
    if len(sys.argv) == 1:
        # they didn't pass any arguments,
        # so prompt for them in a loop
        print_usage()
        args = []
        while args != ['']:
            args = input("command> ").split(' ')
            if args[0] == 'add':
                # join everyting after the name as a string
                args = ['add', args[1], " ".join(args[2:])]
            process_args(args)
            print('-' * 40 + '\n' * 3)
    else:
        # read the args and process them
        args = sys.argv[1:]
        process_args(args)
        print('-' * 40 + '\n' * 3)


toplevel()
