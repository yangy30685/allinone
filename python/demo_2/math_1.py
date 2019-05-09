#!/usr/bin/python3
import math

a = pow(3, 2)
print(a)

a = round(2.4)
print(a)

b = math.ceil(2.1)
print(b)

c = math.log(9,3)
print(c)

name = input('name:\n')
age = input('age:\n')
print('hi ' + name + ' ur ' + age + ' old')

num_1 = input('a number')
num_2 = input('another number')
# print(float(num_1)+float(num_2))

plural_noun = input('input a plural noun:\n')
celebrity = input('input a name:\n')

print('roses are {}'.format('red'))
print(plural_noun + 'are blue')
print('i love' + celebrity)
