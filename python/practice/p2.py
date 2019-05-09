def f_1(n):
    i = 1
    sum_i = 1
    while i < n:
        i+=1
        sum_i*=i
    return sum_i

print(f_1(4))

def f_2(n):
    sum_value = 0
    if n == 0:
        sum_value = 1
    else:
        sum_value = n*f_2(n-1)
    return sum_value

print(f'f_1={f_1(10)} f_2={f_1(10)}')

def output(s,l):
    if l == 0:
        return
    print(s[l-1])
    output(s,l-1)

# s = input('input a sring:\n')
s = 'this is a demo string'
l = len(s)
output(s,l)

mx = lambda x,y: x if x>y else y
print(mx(8,5))
