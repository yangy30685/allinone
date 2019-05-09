from bs4 import BeautifulSoup
import os

# dir = 'C:\\Users\\lamborghni\\Documents\\GitHub\\allinone\\python\\app_1\\simple.html'
dir = 'C:\\Users\\yangy\\Documents\\GitHub\\allinone\\python\\app_1\\simple.html'
    
with open(dir) as h_f:
    soup = BeautifulSoup(h_f, 'lxml')

print('-><-'*20)
print(soup.prettify())

# only return 1st match
match_1 = soup.div.text
print('-><-'*20)
print(match_1)
print('-><-'*20)

# only return the 1st match
match_2 = soup.find('div')
print(match_2)
print('--'*20)

for i in soup.find_all('div', class_ = 'article'):
    headline = i.h2.a.text
    print(headline)
    paragraph = i.p.text
    print(paragraph)