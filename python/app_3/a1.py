import re
import os 
import urllib
from urllib.request import urlopen
from urllib.parse import urlencode


print(os.path)
print('---'*20)

os.chdir('python/app_3/')

text_1 = open('text_1.txt', 'w', encoding='utf-8')

url = 'http://image.baidu.com/search/index?tn=baiduimage&ct=201326592&lm=-1&cl=2&ie=gb18030&word=%CD%BC%C6%AC&fr=ala&ala=1&alatpl=others&pos=0'
res = urlopen(url)

# read() returns bytes format
res = res.readlines()
for line in res:
    line = line.strip()
    text_1.write(line.decode('utf-8'))

text_read = open('text_1.txt', 'r+', encoding='utf-8').read()
# print(text_read)
text_1.close()

text_2 = open('text_2.txt', 'w', encoding='utf-8')

p_1 = r'https*://.+?\.jpg'
p_2 = re.compile(p_1)
x = p_2.findall(text_read)

for i in x:
    if len(i)>150:
        continue
    # print(i)
    text_2.write(i+'\n')
text_2.close()

p_a = r'url.+'
p_b = re.compile(p_a)
x = p_b.findall(text_read)

for i in x:
    print(i)
    if len(i) > 150:
        continue
    index = i.find('http')
    i = i[index:-1]
    i = i.replace('\\','')
    if i == '':
        continue
    print(i)
    with open('text_2.txt', 'a+') as f:
        f.write(i+'\n')  

