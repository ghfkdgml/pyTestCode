def decor(func):
    def deco():
        print("decorator!!!")
        print(func.__name__)
    return deco

@decor
def test():
    print("test")

if __name__=='__main__':
    test()
