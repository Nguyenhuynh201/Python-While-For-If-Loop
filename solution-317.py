#This is for the first pattern (a)
print('(a)')
for row in range(1, 11):
    for collumn in range(1, row + 1 ):
        print('*', end='')
    print()
print()

#This is for the second pattern (b)
print('(b)')
for row in range (10, 0, -1):
    for column in range (1, row + 1):
        print('*',end = '')
    print()
print()

#This is for the third pattern (c)
print('(c)')
for row in range(10, 0, -1):
    for space in range(10, row, -1):
        print(' ', end='')
    for column in range(1, row + 1):
        print('*', end='')
    print()
print()

#This is for the fourth pattern (d)
print('(d)')
for row in range(10, 0, -1):
    for space in range(1, row):
        print(' ', end='')
    for column in range(10, row - 1, -1):
        print('*', end='')
    print()
print()



