import sys
import math


def pass_demo():
    pass
print(pass_demo())

def demo_1():
    for letter in 'Python':
        if letter == 'h':
            pass
            print('this pass section')
        print ('the curret letter is : ', letter)
    return

print('-x-'*40)
demo_1()

print('-x-'*40)
radius = 5
print('the area is : %.4f' % (math.pi*radius**2))
print(math.pi)
print('the sin(pi/6) = : %f' % math.sin(math.pi/6))
print('-x-'*40)

sys_array = sys.path
for i in sys_array:
    print(i)

print('-x-'*30)

language = 'abc'
if language == 'python':
    print('python')
elif language == 'java':
    print('java')
else:
    print('no match')

user = 'admin'
logged_in = True

if logged_in:
    print(f'welcom {user}')
else:
    print('plz log in')

nums = [1, 2, 3, 4, 5]

for i in nums:
    if i == 3:
        print('found!')
        break
    print(i)

print('-x-'*30)

for i in nums:
    if i == 3:
        print('found!')
        continue
    print(i)

print('-x-'*30)

# range() not include 10
for n in range(1, 10):
    print(n)

def hello_fun(greeting = 'hi', name = 'you'):
    return '{} from {}'.format(greeting, name)

print(hello_fun())
print(len(hello_fun()))

print(hello_fun().upper())
print(hello_fun().replace('hi','good morning'))
print(hello_fun('yo bro','dryang'))
print(len(hello_fun()))

def student_info(*args, **kwargs):
    print(args)
    print(kwargs)

student_info('math', 'art', name = 'tom', age = '22')


courses = ['math', 'art','physics']
info = {'name':'tom', 'age':'22','gender':'male'}

def student_info_2(*args, **kwargs):
    print(args)
    print(kwargs)

student_info_2(*courses, **info)

print('-x-'*30)

month_days = [0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

def is_leap(year):
    '''
    return true for leap years
    '''
    return year % 4 == 0 and (year % 100 !=0 or year % 400 == 0)

def days_in_month(y, m):
    '''
    return number of days in that month in that year
    '''

    if not 1 <= m <= 12:
        return 'invalid month'
    '''
    feburary in leap years
    '''
    if m == 2 and is_leap(y):
        return 29
    
    return month_days[m]

print(is_leap(2020))

print(days_in_month(2019,1))

print('-x-'*30)



