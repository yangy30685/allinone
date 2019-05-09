#!/usr/bin/python3
# -*- coding:utf-8 -*-

# list
matrix = [[1, 2, 3, 4],
        [5, 6, 7, 8],    
        [9, 10, 11, 12]]

for i in range(3):
    for j in range(4):
        print(matrix[i][j])
    print('--------')

# tuples
u = 123, 13123, 'hello!'
print(u)

# set
basket = {'apple', 'orange', 'apple', 'pear', 'orange', 'banana'}
print(basket)

a = set('asdqwerfasdf')
b = set('asdfasdfasdfbabae')

print(a)
print(b)

print(a-b)
print(a|b)
print(a^b)

# dictionary
tel = {'jack': 4098, 'sape': 4139, 'guido': 4127, 'jack': 4098}

for m, n in tel.items():
    print(m, n)

for i in tel:
    print(i)

del tel['jack']

print('jack' in tel)

for m, n in enumerate(['tic', 'tac', 'toe']):
    print(m, n)

# reverse list
for i in reversed(range(1, 10, 1)):
    print(i)

print('---'*20)