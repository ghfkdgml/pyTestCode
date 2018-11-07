


def kakao():
    ret=[]
    n=int(input('input num'))
    arr1=map(int,raw_input("arr1:").split())
    arr2=map(int,raw_input("arr2:").split())

    for i in range(n):
        ret.append(bin(arr1[i]|arr2[i])[2:].replace('1','#').replace('0',' '))
    print ret

def strCheck(a):
    num=0
    if a[0]=='1' and a[1]=='0':
        num=10
        if a[2]=='D':
            num^=2
        elif a[2]=='T':
            num^=3

    else:
        num=a[0]
        if a[1]=='D':
            num^=2
        elif a[1]=='T':
            num^=3
    return num


def kakao2(test):
    num1=[]
    for i in range(2,len(test)):
        if test[i].isdigit():
            num1.append(i)

    a=test[:num1[0]]
    b=test[num1[0]:num1[1]]
    c=test[num1[1]:]
    print a,b,c
    print strCheck(a)


    #for i in range(len(test)):







if __name__=='__main__':
    kakao2('1S2D*3T')




