# This function will make sure first Coordinate is less than the second Coordinate
def check_order(a, b):
    if a > b:
        a, b = b, a
    return a, b


# This function will receive 2 lines (x1,x2) and (x3,x4) and return True if they overlap, otherwise False
def check_overlap(x1, x2, x3, x4):
    x1, x2 = check_order(x1, x2)
    x3, x4 = check_order(x3, x4)

    if x1 <= x3 <= x2:
        return True

    if x3 <= x1 <= x4:
        return True

    return False


line1 = input('Enter x1 and x2 for the first line separated by a space')
line2 = input('Enter x1 and x2 for the first line separated by a space')

x1, x2 = line1.split(' ')
x3, x4 = line2.split(' ')

result = check_overlap(x1, x2, x3, x4)

if result:
    print('lines overlap')
else:
    print('lines do not overlap')
