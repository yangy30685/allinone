# 3 digital number
for i in range(1,5):
    for j in range(1,5):
        for k in range(1,5):
            if (i !=k) and (i !=j) and (j != k):
                out_come = f'{i}{j}{k}'
                print(out_come)
# p2
tmp_value = input('input a number e.g. 1000000\n')
if tmp_value == '':
    tmp_value = 0
get_value = int(tmp_value)

del tmp_value

arr = [10e5, 6e5, 4e5, 2e5, 1e5, 0]
rate = [0.01, 0.015, 0.03, 0.05, 0.075, 0.1 ]
result = 0

# i>10e5 or 10e5>i>6e5 ...
for idx in range(0,6):
    if get_value > arr[idx]:
        result += (get_value-arr[idx])*rate[idx]
        get_value = arr[idx]
print(result)

# input x y z
my_list = []
for m in range(3):
    tmp_x = input('input: \n')
    if tmp_x == '':
        tmp_x = 0  
    x = int(tmp_x)
    my_list.append(x)

my_list.sort(reverse=True)
print(my_list)

my_list.sort()
print(my_list)

a = [1,2,3,4]
b = a
print(b)
b = a[:]
print(b)
b = a[:0]
print(b)
b = a[:1]
print(b)
b = a[:2]
print(b)
b = a[:3]
print(b)
b = a[:8]
print(b)

import time
print(time.time())
print(time.localtime())
print('--'*40)

t_0 = time.localtime()
t_1 = time.strftime('%Y-%m-%d %H:%M:%S',t_0)
print(t_1)
time.sleep(2)
print(time.strftime('%Y-%m-%d %H:%M:%S',time.localtime(time.time())))

for x in range(1,10):
    for y in range(0,10):
        for z in range(0,10):
            s1 = x*100 + y*10 + z
            s2 = pow(x,3) + pow(y,3) + pow(z,3)
            if s1 == s2:
                print(s1)

#count string
def counter_string(s):
    letters = 0
    space = 0
    digit = 0
    others = 0
    for c in s:
        if c.isalpha():
            letters += 1
        elif c.isspace():
            space += 1
        elif c.isdigit():
            digit += 1
        else:
            others +=1
    print(f'letters is:{letters} space is: {space} digit is: {digit} other is:{others}')

s = 'asdf asdf asdf as123123 %@#$!123 '
counter_string(s)

#calculate distance 
h_initial = 100
time = 10
height = [h_initial]

for i in range(1, 10):
    h_initial /= 2
    height.append(h_initial)

print(height)
print(sum(height) + height[-1])
print(min(height)/2)

