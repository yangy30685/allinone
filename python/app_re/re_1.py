import re

s = '<html><body><h1>hello world<h1></body></html>'
start_index = s.find('<h1>')
for i in range(start_index, len(s)):
    print(s[i], end='')
print()
print()

key_1 = r'<html><body><h1>hello world<h1></body></html>'
p_1 = r'(?<=<h1>).+?(?=<h1>)'
pattern_1 = re.compile(p_1)
match_1 = re.search(pattern_1, key_1)
print(match_1)
print(match_1.group(0))

key_2 = r'javapythonhtmlvhdl'
p_2 = r'python'
pattern_2 = re.compile(p_2)
match_2 = re.search(pattern_2,key_2)
print(match_2)
print(match_2.group(0))

key_3 = r'<h1>hello world<h1>'
p_3 = r'<h1>.+<h1>'
pattern_3 = re.compile(p_3)
print(pattern_3.findall(key_3))

key_4 = r'afiouwehrfuilamborghni30685@live.co.ukaskdjhfiosueh'
p_4 = r'yangy30685@live.co.uk'
pattern_4 = re.compile(p_4)
print(pattern_4.findall(key_4)[0])

key_5 = r'http://www.nsfbuhwe.com and https://www.auhfisna.com or http://www.123.com'
p_all = [r'http*://', r'https*://',r'http.://',r'http.+://',r'http.+?://',r'http.?://',r'http+://',r'https+://']

for i in range(0, len(p_all)):
    pattern = re.compile(p_all[i])
    print(f'reg is {p_all[i]} and result is {pattern.findall(key_5)}')

key_6 = r'chuxiuhong@hit.edu.cn'
p_6 = r'@.+\.'
pattern_6 = re.compile(p_6)
print(pattern_6.findall(key_6))

key_6 = r'chuxiuhong@hit.edu.cn'
p_6 = r'@.+?\.'
pattern_6 = re.compile(p_6)
print(pattern_6.findall(key_6))

key_7 = r"saas and sas and saaas"
p_7 = r"sa{1,2}s"
pattern_7 = re.compile(p_7)
print(pattern_7.findall(key_7))

print(re.match('www','www.123.com'))
print(re.match('com','www.123.com'))
print(re.search('com','www.123.com').span())