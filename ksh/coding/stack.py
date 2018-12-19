

def validPS(msg):
    ret=list(msg)
    cnt=0
    for x in ret:
        if cnt<0:
            break
        if x =='(':
            cnt+=1
        elif x==')':
            cnt-=1
    if cnt==0:
        print('YES')
    else:
        print('NO')

#def multiPS(msg):
#    ret=list(msg)
#    stack=[]
#    tmp=1
#    tmptotal=0
#    total=0
#    subcheck=False
#    cnt=0
#    for x in ret:
#        if x in ['(','[']:
#            if subcheck:
#                tmptotal+=tmp
#                tmp=1
#                subcheck=False
#                cnt+=1
#            stack.append(x)
#        elif x ==')':
#            if len(stack)>1:
#                if stack[-1]=='(':
#                    if cnt:
#                        stack.pop()
#                        subcheck=True
#                        tmp*=2
#                        cnt-=1
#                    else:
#                        
#                else:
#                    total=0
#                    break
#            elif len(stack)==1:
#                if stack[0]=='(':
#                    stack.pop()
#                    subcheck=False
#                    tmptotal+=tmp
#                    total+=tmptotal*2
#                    tmptotal=0
#                    tmp=1
#                else:
#                    total=0
#                    break
#            else:
#                total=0
#                break
#                    
#                
#        elif x==']':
#            if len(stack)>1:
#                if stack[-1]=='[':
#		    subcheck=True
#                    stack.pop()
#                    tmp*=3
#                else:
#                    total=0
#                    break
#            elif len(stack)==1:
#                if stack[0]=='[':
#                    stack.pop()
#                    subcheck=False
#                    tmptotal+=tmp
#                    total+=tmptotal*3
#                    tmptotal=0
#                    tmp=1
#                else:
#                    total=0
#                    break
#            else:
#                total=0
#                break
#    print(total)

def test(msg):
    ret=list(msg)
    stack=[]
    total=0
    add_check=False
    for x in ret:
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
                            stack=[]
                            total=0
                            break
                        else:
                            stack[-2]=stack[-1]*2
                            stack.pop()
                            
                    elif len(stack)>1 and stack[-2]=='(':
                        stack[-2]=stack[-1]*2
                        stack.pop()
                    else:
                        total=0
                        stack=[]
                        break
                else:
                    total=0
                    stack=[]
                    break
            else:
                total=0
                stack=[]
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
                            stack=[]
                            break
                        else:
                            stack[-2]=stack[-1]*3
                            stack.pop()
                    elif len(stack)>1 and stack[-2]=='[':
                        stack[-2]=stack[-1]*3
                        stack.pop()
                    else:
                        total=0
                        stack=[]
                        break
                else:
                    total=0
                    stack=[]
                    break
            else:
                total=0
                stack=[]
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

test('([)])')
