
def stockCount(a):
    while 1:
        name=raw_input('what\'s the name of stock?:')
        value=int(input("how much?:"))
        num=int(input("how much stock do you have?:"))
        total_v=value*num
        a[name]=(name,value,num,total_v)
        chk=raw_input("Do you have stock left?(y/n)")
        if chk=='n':
            break
    return a

def lossCheck(value):
    percent=int(input("how many percent do you loss or get?:"))
    loss_get=raw_input("loss or get:?(loss/get)")
    if loss_get=='loss':
        total_v=value*(100-percent)/100
    else:
        total_v=value*(100+percent)/100
    return total_v


def main():
    total_stock={}
    total=0

    stockCount(total_stock)
    for x in total_stock.keys():
        name,value,num,total_v= total_stock[x]
        print("name:{},value:{},num:{},total_v:{}".format(name,value,num,total_v))
        checker=raw_input("Do your stock's value change?(y/n)")
        if checker=='y':
            total_v=lossCheck(total_v)
        total+=total_v
    print"total:{}".format(total)


if __name__=="__main__":
    main()
