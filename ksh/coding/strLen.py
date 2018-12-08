


def strLen(s):
    str_len=len(s)
    m=str_len/10
    n=str_len%10
    ret=[]
    num=0
    for x in range(m):
        ret.append(s[num:num+9])
        num+=10
    if not n:
        ret.append(s[num:]
    #print(ret)
    for x in ret:
        print(x)

strLen("aaaaaaaaaabbbbbbbbbbccccccccccddddd")
