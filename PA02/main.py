'''Interval.class
Author: @Jeremy Huey
Description: This represents all real numbers betwee [x,y]
[low,high] = set {x in R| low<=x<=hi}

Version: 1.0
Known Bugs: see below for  testing incompleteness. See test_interval.py for one pytest version.
'''

from typing import Type
from math import isclose

import traceback
def p(v):
    '''This is just a cool tester function to see if we can get print('f{var=}') functionality to work faster. '''
    # import traceback
    stack = traceback.extract_stack()
    filename, lineno, function_name, name = stack[-2]
    print(name[2:-1]+'='+str(v))  # repr?
    # print( "{:<25}".format(name[2:-1]) ,  ':   ' , var)
    # end p(v)

class Interval:
    '''
    Intervals are defined as ll real numbers betweem [x,y], [low,high] = set {x in R| low<=x<=hi}.
    :raises AttributeError if given construction of an interval where y-high is smaller than x-low.
    '''
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
        return Interval(min(a*c,a*d,b*c,b*d), max(a*c,a*d,b*c,b*d) ) #fix: had divs lol.

    # in python 3 you need __truediv__ for float div
    def __truediv__(self, other: 'Interval') -> 'Interval':
        '''
        As requested in spec, if the second interval spans thru 0, it will
        :raise ZeroDivisionError
        :param other:
        :return:
        '''
        a = self.n1; b = self.n2; c = other.n1; d = other.n2
        if isclose(c,0) or isclose(d,0):
            raise ZeroDivisionError
        if c <= 0.0 and 0.0 <= d:
            raise ZeroDivisionError
        return Interval(min(a/c,a/d,b/c,b/d), max(a/c,a/d,b/c,b/d))

    def __eq__(self, other):
        '''This is required to do easy comparisons during pytest in test_interval.py
        :return boolean, True if values are equal, False if not.
        Notes: Does this need to use math.isclose()?
        '''
        return self.n1 == other.n1 and self.n2 == other.n2

    def intersect(self, other):
        '''
            This tests to see if there is an intersect between a.intersect(b)
        :raise AttributeError if there is an empty intersection, which is called via the constructor.
        :param other:
        :return:
        '''
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

    def intersects(self, other):
        '''This checks if an intersect was able to be made from the intersect function.
        :return boolean:
            True if able
            False if not
            '''
        try:
            new_int = self.intersect(other)
        except AttributeError as N:
            return False
        return True


    def union(self, other):
        '''
        The union function, called a.union(b), checks to see if the two intervals overlap, if so, it returns the union of it.
            [-2,0] [-1,1] = [-2, 1], venn if a<= c and b>= c
            [-2, 0] [1,1] = failure 2 circle, noncontinuous interval.
            [-2, 1] [0, 0.5] = inclusive X Y
            This code may require further testing for edge cases.
        :param other:
        :return: Interval
        '''

        '''
            
            '''
        new_interval = None
        a = self.n1; b = self.n2; c = other.n1; d = other.n2
        # fail:
        if not (  (a<=c<=b) or (c<=a<=d) ):
            print(f"No overlap during union of {self=} and {other=}")
            raise AttributeError
        else:
            new_n1 = min(self.n1, other.n1)
            new_n2 = max(self.n2, other.n2)


        try :
            # print(f'{new_n1=}, {new_n2=}')
            new_interval = Interval(new_n1, new_n2)
        except AttributeError as N:
            print("This was an empty union.")
            raise AttributeError
        return new_interval
    # place this into try except.
    # end def union

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

    # union testing ===========
    aa = Interval(-2.0, 0.0)
    bb = Interval(1, 1)
    try:
        print(f'{aa.union(bb)=}')
        print("This union succeeded.")
    except AttributeError as N:
        print("This union test task successfully failed.")
    try:
        print(f'{bb.union(aa)=}')
        print("This union succeeded.")
    except AttributeError as N:
        print("This union test task successfully failed.")

    cc = Interval(-2, 0)
    dd = Interval(-1, 1)
    print(f'{cc.union(dd)=}')
    print(f'{dd.union(cc)=}')

    ee = Interval(3, 6)
    ff = Interval(4,5)
    print(f'{ee.union(ff)=}')
    print(f'{ff.union(ee)=}')




