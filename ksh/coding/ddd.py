msg=str(input())
def test(msg):
    ret=list(msg)
    stack=[]
    total=0
    add_check=False
    for x in ret:
        print(stack)
        if x in ['(','[']:
            if len(stack)>=1 and type(stack[-1])==int:
                add_check=True
            stack.append(x)
        elif x==')':
            if stack:
                if stack[-1]=='(':
                    stack[-1]=2
                elif type(stack[-1])==int:
                    if add_check and type(stack[-2])==int:
                        while type(stack[-2])==int:
                            stack[-2]=stack[-1]+stack[-2]
                            stack.pop()
                        add_check=False
                        if len(stack)==1 or stack[-2]!='(':
                            total=0
                            break
                        else:
                            stack[-2]=stack[-1]*2
                            stack.pop()

                    elif stack[-2]=='(':
                        stack[-2]=stack[-1]*2
                        stack.pop()
                    else:
                        total=0
                        break
                else:
                    total=0
                    break
            else:
                total=0
                break
        elif x==']':
            if stack:
                if stack[-1]=='[':
                    stack[-1]=3
                elif type(stack[-1])==int:
                    if add_check and type(stack[-2])==int:
                        while type(stack[-2])==int:
                            stack[-2]=stack[-1]+stack[-2]
                            stack.pop()
                        add_check=False
                        if len(stack)==1 or stack[-1]!='[':
                            total=0
                            break
                        else:
                            stack[-2]=stack[-1]*2
                            stack.pop()    
                    elif stack[-2]=='[':
                        stack[-2]=stack[-1]*3
                        stack.pop()
                    else:
                        total=0
                        break
                else:
                    total=0
                    break
            else:
                total=0
                break
    if len(stack)>1:
        for x in stack:
            if x in [')','(','[',']']:
                total=0
                break
            else:
                total+=x
    elif len(stack)==1 and type(stack[0])==int:
        total=stack[0]
    print(total)
test(msg)
