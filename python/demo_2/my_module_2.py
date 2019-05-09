from my_module import find_index, test
import my_module as mm
import sys
import random

print(sys.path)
course = ['history', 'math', 'physics','compsci']
index = mm.find_index(course, 'math')

print(index)
print(test)

ran_course = random.choice(course)
print(ran_course)

sys.path.append('C:\\Users\\lamborghni\\Documents\\GitHub\\allinone')

for i in sys.path:
    print(i)

