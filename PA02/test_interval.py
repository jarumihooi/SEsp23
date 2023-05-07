from main import Interval
from math import isclose
import pytest

def test_interval():
    ''' test the +-*/ interval operators '''
    x1 = Interval(0.9, 1.1)
    x2 = Interval(1.999, 2.001)
    x3 = Interval(-1, 1)
    x4 = Interval(10, 10)
    print('x1=', x1)
    print('x2=', x2)
    print('x3=', x3)
    print('x4=', x4)
    print('x1+x2=', x1 + x2)
    print('x2*x3=', x2 * x3)
    print('x3/x4=', x3 / x4)
    # print('x4-x1*x2/(x4+x3)-(x1+x2)', x4 - x1 * x2 / (x4 + x3) - (x1 + x2))


    assert x1 + x2 == Interval(2.899, 3.101)
    assert x2 * x3 == Interval(-2.0010, 2.001)
    assert x3 / x4 == Interval(-0.1, 0.1)
    assert x4-x1*x2/(x4+x3)-(x1+x2) == Interval(6.6544333333333325,6.937445454545455)
    # print(f'{x1*x2=}')

def test_intersects():
    x1 = Interval(0.9, 1.1)
    x2 = Interval(1.999, 2.001)
    x3 = Interval(-1, 1)
    x4 = Interval(10, 10)
    print(f'x1.intersect(x3)={x1.intersect(x3)}')
    print(f'x1.intersects(x3)={x1.intersects(x3)}')
    print(f'x1.intersects(x2)={x1.intersects(x2)}')
    assert x1.intersect(x3) == Interval(0.9, 1.0)
    assert x1.intersects(x3)
    assert x1.intersects(x2) == False


def test_creation():
    x1 = Interval(0.9, 1.1)
    x2 = Interval(1.999, 2.001)
    x3 = Interval(-1, 1)
    x4 = Interval(10, 10)
    # x5 = Interval(0.0, 1.0)
    # x3 divide specs
    try:
        print(x4 / x3)
    except ZeroDivisionError as err1:
        print(f'exception: "interval division by zero"')
    except Exception as err:
        print(f'exception: "{err}"')
    try:
        a = Interval(2, -2)
    except AttributeError as err1:
        print(f'exception: "empty interval"')
    except Exception as err:
        print(f'exception: "{err}"')


    with pytest.raises(ZeroDivisionError):
        x_new1 = x4 / x3

    with pytest.raises(AttributeError):
        a = Interval(2, -2)

if __name__ == '__main__':
    # test_interval()
    # test_intersects()
    test_creation()
'''
# results...
x1 = [0.9, 1.1]
x2 = [1.999, 2.001]
x3 = [-1, 1]
x4 = [10, 10]
x1 + x2 = [2.899, 3.101]
x2 * x3 = [-2.001, 2.001]
x3 / x4 = [-0.1, 0.1]
x4 - x1 * x2 / (x4 + x3) - (x1 + x2)[6.6544333333333325, 6.937445454545455]
x1.intersect(x3) = [0.9, 1]
x1.intersects(x3) = True
x1.intersects(x2) = False
exception: "interval division by zero"
exception: "empty interval" '''

r'''pytest results
PS C:\Users\J\Documents\Classes\Class+Sp+2023\1_SE\SEsp23\PA02> pytest -v
============================================================================== test session starts 
===============================================================================
platform win32 -- Python 3.10.11, pytest-7.2.2, pluggy-1.0.0 -- 
C:\Users\J\AppData\Local\Microsoft\WindowsApps\PythonSoftwareFoundation.Python.3.10_qbz5n2kfra8p0\python.exe       
cachedir: .pytest_cache
rootdir: C:\Users\J\Documents\Classes\Class+Sp+2023\1_SE\SEsp23\PA02
collected 3 items

test_interval.py::test_interval PASSED                                                                                                                                      [ 33%] 
test_interval.py::test_intersects PASSED                                                                                                                                    [ 66%] 
test_interval.py::test_creation PASSED                                                                                                                                      [100%] 

=============================================================================== 3 passed in 0.03s
 ================================================================================ 
'''