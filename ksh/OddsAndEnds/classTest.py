#-*-coding:utf-8-*-

class Point():
    def __init__(self,_x,_y):
        self.x=_x
        self.y=_y

    def setx(self,x):
        self.x=x
    def sety(self,y):
        self.y=y

    def get(self):
        return self.x,self.y

    def move(self,dx,dy):
        self.x+=dx
        self.y+=dy



if __name__=="__main__":
    a=Point(4,5)
    a.move(2,-4)
    print a.get()


