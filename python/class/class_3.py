class parent:
    def __init__(self):
        print('class parent __init__')

    def parent_method(self):
        print('class parent method')

    def set_attr(self, attr = 0):
        parent.parent_attr = attr

    def get_attr(self):
        print(f'get parent attr: {parent.parent_attr}')


# inheriate from parent
class child(parent):
    def __init__(self):
        print('child __init__')

    def child_method(self):
        print('child method')


def main():
    # create an child obj
    c = child()
    # use child method
    c.child_method()

    # use parent method directly
    c.parent_method()
    # use parent set
    c.set_attr()
    # get parent attr
    c.get_attr()

if __name__ == '__main__':
    main()