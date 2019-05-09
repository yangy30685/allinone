from urllib.request import urlopen
import os
import glob
import re

os.system('cls')

dir_1 = os.getcwd()
os.chdir('python/app_3/')
dir_2 = os.getcwd()

print('--'*3)
print(dir_1 + '\n' + dir_2)
print('--'*3)

print(glob.glob('*.py'))

re_str = 'which foot or hand fell fastest, which foot or hand fell fastest'
re_value = [r'\bf[a-e].', 
            r'\bf[a-e]*', 
            r'\bf[a-e]?', 
            r'\bf[a-e]+', 
            r'\bf[a-e].*',
            r'\bf[a-e].+',  
            r'\bf[a-e].?',    
            r'\bf[a-e].+?',
            r'\bf[a-e].+',
            r'\bf[a-e].*?',
            r'\bf[a-e]*.?', 
            r'\bf[a-e]*.+', 
            r'\bf[a-e]*?'] 

for i in range(len(re_value)):
    re_demo = re.findall(re_value[i], re_str)
    print(f'{re_value[i]:15}====>>>> {re_demo}')

