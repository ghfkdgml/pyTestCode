from math import sqrt

def findprime(num):
    if num==1:
        return 0
    if num==2:
        return 1
    a=int(sqrt(num))
    for x in range(2,a+1):
        if num%x==0:
            return 0
    return 1

def totalprime(m,n):
    total=0
    min_num=0
    for x in range(m,n+1):
        if findprime(x):
            total+=x
            if not min_num or min_num>x:
                min_num=x
    if not total:
        print(-1)
    else:
        print(total)
        print(min_num)

def totalprime_x(m,n):
    total=[]
    min_num=0
    for x in range(m,n+1):
        if findprime(x):
            total.append(x)
            if not min_num or min_num>x:
                min_num=x
    if not total:
        print(-1)
    else:
        #print(total)
        for x in total:
            print(x)

