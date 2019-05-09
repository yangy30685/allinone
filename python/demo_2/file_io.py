import os
import sys

pwd_1 = os.getcwd()
print('working dircetory is {}'.format(pwd_1))
work_dir = './python/demo_2'
os.chdir(work_dir)
pwd_2 = os.getcwd()

# print(pwd_1+'\n'+pwd_2)
# os.remove('foo.txt')


def file_demo_1():
    fo = open('foo.txt','w+')
    print('file_name: ', fo.name)
    print('check if closed: ', fo.closed)
    print('mode : ', fo.mode)
    print('encoding : ', fo.encoding)
    
    fo.write('this is dryang\'s python demo')
    fo.close()

def main():
    file_demo_1()
    print('='*80)

    try:
        with open('foo.txt', 'a+') as fo_1:
            pos_1 = fo_1.tell()
            
            print('-->', pos_1, '<--') 
            fo_1.write('\nthis another line')
            
            pos_2 = fo_1.tell()
            print('-->', pos_2, '<--')
            
            fo_1.close()

            a = open('foo.txt', 'r+')
            for xx in a.readlines():
                print(xx)
                # print(xx.replace('\n',''))
    except Exception:
        print('------->error<--------')
    finally:
        print('END')

if __name__ == '__main__':
    main()
