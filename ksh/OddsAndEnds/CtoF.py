#-*-coding:utf-8-*-

def CtoF(cel):
    print "섭씨:{}->화씨:{}".format(cel,(cel*1.8)+32)
def FtoC(f):
    print "화씨:{}->섭씨:{}".format(f,(f-32)/1.8)

def main():
    a=40
    CtoF(40)
    FtoC(40)

if __name__=='__main__':
    main()

