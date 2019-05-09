class MyClass:
    """a class demo"""
    i = 12345
    def f(self):
        return 'hello world'

# create a class x
x = MyClass()

# print my_class
print("MyClass attributes i：", x.i)
print("MyClass function f：", x.f())


class Complex:
    # __init__ is a constructor
    def __init__(self, realpart, imagpart):
        self.r = realpart
        self.i = imagpart

x = Complex(3.0, -4.5)

# print output：3.0 -4.5
print(x.r, x.i)   


class Test:
    def prt(self):
        print(self)
        print(self.__class__)
 
t = Test()
t.prt()

class people:
    name = ''
    age = 0
    __weight = 0
    def __init__(self,n,a,w):
        self.name = n
        self.age = a
        self.__weight = w
    def speak(self):
        print('%s says im %d years old and weight is %f kg'%(self.name, self.age, self.__weight))
p = people('dryang',1,2)
p.speak()
