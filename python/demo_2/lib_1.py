import random
import math
import webbrowser

rads = math.radians(30.0)
print(rads)
print(math.sin(rads))

web_content = webbrowser.open('https://google.com')
print(web_content)

course = ['history', 'math',' physics', 'compsci']
c_c = random.choice(course)
print(c_c)