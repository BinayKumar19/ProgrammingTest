# qsA.py
# Binay Kumar
# May 12, 2019

"""
==========
qsA
==========
This module contains functions to check if two lines overlap or not

Contents
--------
* check_order()  - This function will make sure first Coordinate is less than the second Coordinate
* check_overlap()- This function will check if 2 lines overlap or not

"""


def check_order(a, b):
    """
    Returns: Coordinates of a point in increasing order.
    ===========
    Description
    ===========
    This function will make sure first Coordinate is less than the second Coordinate
    """
    if a > b:
        a, b = b, a
    return a, b


def check_overlap(x1, x2, x3, x4):
    """
    Returns: True if lines overlap, otherwise False
    ===========
    Description
    ===========
    This function will receive 2 lines (x1,x2) and (x3,x4)
    """
    x1, x2 = check_order(x1, x2)
    x3, x4 = check_order(x3, x4)

    if x1 <= x3 <= x2:
        return True

    if x3 <= x1 <= x4:
        return True

    return False


if __name__ == '__main__':
    line1 = input('Enter x1 and x2 for the first line separated by a space:')
    line2 = input('Enter x1 and x2 for the first line separated by a space:')

    x1, x2 = line1.split(' ')
    x3, x4 = line2.split(' ')

    result = check_overlap(x1, x2, x3, x4)

    if result:
        print('lines overlap')
    else:
        print('lines do not overlap')
