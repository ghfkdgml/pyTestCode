#N=int(input())
#nums=[]
#for a in range(N):
#    nums.append(int(input()))
    

def sorting(ss):
    ret=sorted(ss)
    for x in ret:
        print(x)

def compNum(front,back=None):
    ret=[]
    if not back:
        if type(front)!=list:
            ret.append(front)
            return ret
        return front
    if type(front)==int:
        if front<back:
            return [front,back]
        elif front>back:
            return [back,front]
    f=0
    b=0
    while 1:
        if front[f]>back[b]:
            ret.append(back[b])
            if b<len(back)-1:
                b+=1
            else:
                for x in front[f:]:
                    ret.append(x)
                break
        elif front[f]<back[b]:
            ret.append(front[f])
            if f<len(front)-1:
                f+=1
            else:
                for x in back[b:]:
                    ret.append(x)
                break
    return ret
    
def sortingss(ss):
    #ret=list(map(int,str(ss)))
    ret=ss
    result=[]
    #if not num:
    #    return
    while 1:
        num=len(ret)
        for x in range(0,num,2):
            if ret[x]==ret[-1]:
                result.append(compNum(ret[x]))
            else:
                part_ret=compNum(ret[x],ret[x+1])
                result.append(part_ret)
        if num==1:
            break
        ret=result
        result=[]
    #print(ret[0])
    if type(ret[0])==int:
        print(ret[0])
    else:
        for x in ret[0]:
            print(x)
import random
rannum=[x for x in range(100000)]
random.shuffle(rannum)

sortingss(rannum)
