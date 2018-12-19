

class Deck():
    def __init__(self):
        self.ret=[]

    def push_back(self,num):
        self.ret.append(num)
        print(num)
    
    def push_front(self,num):
        self.ret.insert(0,num)
        print(num)
    
    def pop_front(self,num):
        if self.ret:
            print(self.ret.pop(0))
        else:
            print(-1)

    def pop_back(self,num):
        if self.ret:
            print(self.ret.pop())
        else:
            print(1)

    def size(self):
        print(len(self.ret))

    def empty(self):
        if ret:
            print(0)
        else:
            print(1)

    def front(self):
        if self.ret:
            print(self.ret[0])
        else:
            print(-1)

    def back(self):
        if self.ret:
            print(self.ret[-1])
        else:
            print(-1)

a=Deck()
b="push_back"
a.b(3)
