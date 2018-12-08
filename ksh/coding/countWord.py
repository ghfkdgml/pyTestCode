

def wordCount(s):
    if not len(s):
        return "Not exist string"
    ret=0
    for x in s.split(' '):
        if x:
            ret+=1
    print(ret)
    return ret

def OXcount(s):
    con=0
    ret=0
    for x in list(s):
        if x in ['o','O']:
            if con:
                ret+=con+1
                con+=1
            else:
                ret+=1
                con+=1
        else:
            if con:
                con=0
    print(ret)


OXcount('OOOOOOOOOO')
OXcount('OXOXOXOXOXOXOX')
OXcount('OOOOXOOOOXOOOOX')
