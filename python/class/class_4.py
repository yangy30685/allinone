class People:
    '''
    this is helpful info
    author@dryang
    yangspot.com
    '''
    number = 100

    def __init__(self, name, age):
        self.name = name
        self.age = age
    
    def display(self):
        print(self.name)
        print(self.age)
        print(self.__doc__)


class student(People):
    def __init__(self):
        print('this is a student')

    def student_method(self):
        print('student method')

    def new_method(self):
        print('this is a new method')


def main():
    p1 = People('tom', 99)
    p1.display()
    
    a = hasattr(p1, 'name')
    b = getattr(p1, 'name')
    
    print(type(a))
    print(type(b),b)

    # c1 = student('jack',888)
    c1 = student()
    print('parent attr', c1.number)
    
    c1.student_method()
    c1.new_method()


if __name__ == "__main__":
    main()
