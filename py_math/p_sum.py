def python_sum(n):
    a = list(range(n))
    b = list(range(n))
    c = []

    for i in range(0, len(a)):
        a[i] = i**2
        b[i] = i**3
        c.append(a[i]+b[i])
    return c 


if __name__ == '__main__':  
    n = 10
    print(f'python_sum({n})',python_sum(n))
