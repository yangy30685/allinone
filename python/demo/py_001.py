import os
import sys
import numpy as np
import matplotlib.pyplot as plt

y = [1,2,3,4]
x = [3,4,5,6]
plt.plot(x,y)
plt.show()

def line(n):
    i = 0
    while i < n:
        print("-", end="")
        i+=1
    print("\n")
    return
line(50)

str_1 = "hello"
str_2 = "dryang"
var_1 = "this is a demo"
var_2 = "for string"

print(str_1+str_2)
print(str_1*2)
print(str_1[1])
print(str_1[1:5])
print("var1[0]", var_1[0])
print("var2[1:-3]", var_2[1:5])

def judnge(input_character,input_string):          
    
    if(input_character in input_string):
        print("%s is in \'%s\'" % (input_character,input_string))
    else:
        print('{0} is not in \"{1}\"'.format(input_character, input_string))

judnge("a", var_1)
judnge("a", var_2)

# r and R is the same 
print(r'\n')
print(R'\n')

# format print out
print("my name is %s\nmy weight is %s\n"% ("dryang",21))

# bell sound
print("you should hear a tone %c" %(7))

# print out alphabet 
def alphabet():
    for i in range(65,122):
        print("ascii - " + str(i) + " is %c" %(i))
    return

multi_demo = '''this is two
lines
'''
print(multi_demo)

# unicode 0020 is a space
unicode_demo =  u'H\u0020e\u0020l\u0020l\u0020o\u0020World !'
print(unicode_demo)

print(sys.getdefaultencoding())