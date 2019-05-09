# demo setter and getter
class A():
    name = 'dana'
    age = 18


for i in A.__dict__:
    print(i)
    
print()
print(A.__weakref__)
print()
print(A.__module__)

print()
print('--'*30)
print()


class A:
    def __init__(self, first, last):
        self.first = first
        self.last = last
        self.email = first +'.' + last + '@email.com'

    def full_name(self):
        return f'{self.first} {self.last}'


emp_1 = A('tom', 'smith')

print(emp_1.first)
print('--->' + emp_1.email)
print(emp_1.full_name())

print()
print('--'*30)
print()

# change 1st name
emp_1.first = 'Jim'

print(emp_1.first)
print('--->' + emp_1.email)
print(emp_1.full_name())

print()
print('--'*30)
print()


class B:
    def __init__(self, first, last):
        self.first = first
        self.last = last

    @property
    def email(self):
        return f'{self.first}.{self.last}@email.com'
    
    @property
    def full_name(self):
        return f'{self.first}-{self.last}'

    @full_name.setter
    def full_name(self, name):
        first, last = name.split(' ')
        self.first = first
        self.last = last
    
    @full_name.deleter
    def full_name(self):
        print()
        print('delete name')
        print()
        self.first = None
        self.last = None


emp_1 = B('tom', 'smith')

print(emp_1.first)
print('--->' + emp_1.email)
print(emp_1.full_name)

print()
print('--'*30)
print()

# change 1st name
emp_1.first = 'Jim'

print(emp_1.first)
print('--->' + emp_1.email)
print(emp_1.full_name)
