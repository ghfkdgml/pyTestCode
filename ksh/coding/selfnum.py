

def selfNum(num):
    pos=len(str(num))
    ret=num
    for x in range(pos):
        ret+=int(str(num)[x])
    print("result:",ret)

selfNum(75)
selfNum(39)
    
