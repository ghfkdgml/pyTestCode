


def findPos(num):
    length=len(str(num))
    pass

def lenCount(num):
    ret=[]
    cnt=1
    for x in range(num):
        a=int((x*x+x)/2)
        if len(str(a))==cnt:
            ret.append(a)
            cnt+=1
    print(ret)


def test(num):
    ret=1
    n=1
    while 1:
        if num>ret:
            ret+=6*int((n*n+n)/2)
            n+=1
        else:
            print(n)
            break

def fraction(num):
    ret=0
    n=1
    while 1:
        if num>ret:
            ret+=int((n*n+n)/2)
            n+=1
        else:
            if n%2:
                down=n-(ret-num)
                print(n,ret,num,down)
                up=n+1-down
                print(up,'/',down)
                break
            else:
                up=n-(ret-num)
                down=n+1-up
                print(up,'/',down)
                break

fraction(12)
