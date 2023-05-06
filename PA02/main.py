'''Interval.class
Author: @Jeremy Huey
Description: This represents all real numbers betwee [x,y]
[low,high] = set {x in R| low<=x<=hi}

Version: 1.0
Known Bugs: n/a
'''

from typing import Type
from math import isclose

import traceback
def p(v):
    stack = traceback.extract_stack()
    filename, lineno, function_name, name = stack[-2]
    print(name[2:-1]+'='+str(v))  # repr?
    # print( "{:<25}".format(name[2:-1]) ,  ':   ' , var)
    # end p(v)

class Interval:
    def __init__(self, _n1:float, _n2:float):
        if (_n1 > _n2):
            raise AttributeError
        self.n1 = _n1
        self.n2 = _n2

    def __str__(self) -> str:
        return f"[{self.n1:.3f}, {self.n2:.3f}]"

    def __repr__(self):
        return f"[{self.n1:.3f}, {self.n2:.3f}]"

    def __add__(self, other: 'Interval') -> 'Interval':
        return Interval(self.n1+other.n1, self.n2+other.n2)

    def __sub__(self, other: 'Interval') -> 'Interval':
        return Interval(self.n1-other.n2, self.n2-other.n1)

    def __mul__(self, other: 'Interval') -> 'Interval':
        a = self.n1; b = self.n2; c = other.n1; d = other.n2
        return Interval(min(a*c,a*d,b*c,b*d), max(a/c,a/d,b/c,b/d) )

    # in python 3 you need __truediv__ for float div
    def __truediv__(self, other: 'Interval') -> 'Interval':
        a = self.n1; b = self.n2; c = other.n1; d = other.n2
        if isclose(c,0) or isclose(d,0):
            raise ZeroDivisionError
        return Interval(min(a/c,a/d,b/c,b/d), max(a/c,a/d,b/c,b/d))

    def intersect(self, other):
        new_n1 = max(self.n1, other.n1)
        new_n2 = min(self.n2, other.n2)
        new_interval = None
        try :
            print(f'{new_n1=}, {new_n2=}')
            new_interval = Interval(new_n1, new_n2)
        except AttributeError as N:
            print("This was an empty intersection.")
            raise AttributeError
        return new_interval
    # place this into try except.
    # end def intersect

    def union(self, other):
        new_interval = None
        if (self.n1 <= other.n1) and (other.n1 <= self.n2):
            new_n1 = other.n1
            new_n2 = min(self.n2, )

        new_n1 = min(self.n1, other.n1)
        new_n2 = max(self.n2, other.n2)

        try :
            print(f'{new_n1=}, {new_n2=}')
            new_interval = Interval(new_n1, new_n2)
        except AttributeError as N:
            print("This was an empty intersection.")
            raise AttributeError
        return new_interval
    # place this into try except.
    # end def intersect

if __name__ == '__main__':
    print('starting main')
    x = Interval(0.0, 1.0)
    y = Interval(1.0, 2)
    print(f"{x=}")
    print("x",x)
    print("y",y)
    print(x+y, x-y, x*y, x/y)

    try:
        z = y / x
    except ZeroDivisionError as N:
        print("This line got ZeroDivisionError as expected")
    print(f'{x+y=}')
    p(x+y)
    p(x.n1)

    try:
        print(f'{x.intersect(y)=}')
        print("This intersect succeeded.")
    except AttributeError as N:
        print("This intersect test failed.")

    try:
        z = Interval(-2.0, -1.0)
        print(f'{x.intersect(z)=}')
        print("This intersect succeeded.")
    except AttributeError as N:
        print("This intersect test failed.")



