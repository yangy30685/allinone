class employee:
    num_of_employee = 0
    raise_amt = 1.04

    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.email = first + '.'+ last+'@email.com'
        self.pay = pay
    # counter by init 
        employee.num_of_employee += 1
    
    def full_name(self):
        return '{} {}'.format(self.first, self.last)
    
    def apply_raise(self):
        self.pay = int(self.pay * self.raise_amt)
    
    # definei a class method
    @classmethod
    def set_raise_amt(cls, amount):
        cls.raise_amt = amount

#inheriant from employee
class developer(employee):
    raise_amt = 1.20

    def __init__(self, first, last, pay, prog_lang):
        # inheritance
        super().__init__(first, last, pay)
        
        self.prog_lang = prog_lang 


class manager(employee):
    def __init__(self, first, last, pay, employees = None):
        # inheritance
        super().__init__(first, last, pay)

        # employees(list type)
        if employees.num_of_employee is None:
            self.employees = []
        else:
            self.employees = employees

    def add_emp(self, emp):
        if emp not in self.employees:
            self.employees.append(emp)

emp_1 = employee('corey', 'schafer', 50000)
emp_2 = employee('test', 'employee', 60000)

print(emp_1.first,emp_1.num_of_employee,emp_1.pay)
print(emp_2.first,emp_2.num_of_employee,emp_2.pay)

emp_1.apply_raise()
print(emp_1.first, emp_1.num_of_employee, emp_1.pay)

print(employee.raise_amt)
employee.set_raise_amt(1.1)
print(employee.raise_amt)

emp_1.apply_raise()
print(emp_1.first, emp_1.num_of_employee, emp_1.pay)

