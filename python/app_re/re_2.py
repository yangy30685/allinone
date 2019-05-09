import re

# ignore the position
print(re.search('www', 'www.123.com').span())
print(re.search('ww', 'www.123.com'))
print(re.search('com', 'www.123.com')) 

# only from the beginnning
print(re.match('www', 'www.123.com').span())
print(re.match('ww', 'www.123.com'))
print(re.match('com', 'www.123.com')) 

phone = '123-123-123 # this is a number comment'
print(phone)

# subsitute
num = re.sub(r'#.*$', '', phone)
print('the new number is: ', num)

num_1 = re.sub(r'\D', '', num)
print('the new 1 num is : ', num_1)

