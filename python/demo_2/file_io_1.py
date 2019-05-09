def demo_1():
    try:
        fh = open('test_file', 'w')
        fh.write('this is a test file!!!')
    except IOError:
        print('Error: no file or read file')
    else:
        print('successfully writting in!!')
        fh.close()
    finally:
        print('Finally \n---END---')

def demo_2():
    try: 
        fh = open('test_file','r')
        fh.write('this is a test file for exception!!!')
    except IOError:
        print('Error： no file found or read or wirte faile !!!')
    else:
        print('successful!!!!')
    
    finally:
        print('Finally \n---END---')

def demo_3(): 
    def mye(level):
        if level < 1:
            raise Exception('Invalid level!')
    try:
        mye(0)
    except Exception as err:
        print(0, err.args)
    finally:
        print('Finally \n---END---')


if __name__ == '__main__':
    demo_1()
    demo_2()
    demo_3()
    