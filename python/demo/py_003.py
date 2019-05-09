class employee:
    # constructor
    def __init__ (self, first, last, pay):
        self.first_name = first
        self.last_name = last
        self.pay = pay
        self.email = first+'.'+last+'@company.com'
    def full_name(self):
        return '{}<--->{}'.format(self.first_name, self.last_name)


def main():
    emp_1 = employee('dryang', 'yang', 40000)
    emp_2 = employee('test', 'user', 10000)

    # 2 ways with the same results
    print(emp_1.full_name())
    print(employee.full_name(emp_1))

if __name__ == "__main__":
    pass
    main()



