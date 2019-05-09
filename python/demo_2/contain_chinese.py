def contain_chinese(check_str):
    for ch in check_str:
        print(ch,end='')
        # chinese
        if u'\u4e00' <= str(ch) <= u'\u9fff':
            print()
            return True
    print()
    return False


def main():
    a = "123这是中文"
    a1 = "asdfb这是中文123abc"
    a2 = "no chinese"
    a_list = [a, a1, a2]
    
    for i in a_list:
        print(contain_chinese(i))


if __name__ == "__main__":
    main()