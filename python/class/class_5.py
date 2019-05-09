class point:
    def __init__(self, x=0,y=0):
        self.x = x
        self.y = y
    def __del__(self):
        class_name = self.__class__.__name__
        print(class_name+' '+'destoryed')

pt_1 = point()
pt_2 = point()
# pt_3 = pt_2
print(id(pt_1),id(pt_2))
# use delete twice as pt_3 and pt_2 are the same
del pt_1
del pt_2
# del pt_3  

class vector:
    def __init__(self, a, b):
        self.a = a
        self.b = b
    # let vecto to be readable by user
    def __str__(self):
        return f'vector is ({self.a}, {self.b})'

    def __add__(self, other):
        return vector(self.a+other.a, self.b+other.b)
v1 = vector(1,2)
v2 = vector(2,3)
print(v1+v2)