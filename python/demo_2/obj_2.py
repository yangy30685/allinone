import obj_1
import sys

# check imported or not
if __name__ == '__main__':
    print('---> main <---')
else:
    s = 'obj_2'
    print('---> imported {} <---'.format(s))

# demo obj_1 import
obj_1.fib(20)
a = obj_1.fib2(20)
print(a)

# demo sys
for i in sys.path:
    print('--->>>',i,'<<<---')