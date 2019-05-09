
import os

# check imported or not
if __name__ == '__main__':
    print('---> main <---')
else:
    s = 'obj_2'
    print('---> imported {} <---'.format(s))

work_dir = 'C:\\Users\\lamborghni\\Documents\\GitHub\\allinone\\python\\demo'
os.chdir(work_dir)
print(os.getcwd())

# i = 1
for f in os.listdir():
    file_name, file_ext = os.path.splitext(f)
    print(file_name, file_ext)
    
    f_title, f_num = file_name.split('_')
    new_name = f_title+'_'+f_num.zfill(3)+file_ext
    print(new_name)
    os.rename(f, new_name)

    # new_name = 'py_'+str(i)+'.py'
    # print(new_name)
    # int(i)
    # i+=1
    # os.rename(f, new_name)

