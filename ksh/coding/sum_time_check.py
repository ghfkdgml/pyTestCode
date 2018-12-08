import time

def time_check(func):
    def check(num):
        bef=time.time()
        func(num)
        aft=time.time()
        print(aft-bef,"was taken")
    return check



@time_check
def sumnum(num):
    ret=0
    for x in range(num):
        ret+=x+1
    print("num1",ret)
@time_check
def sum2(num):
    print("num2",num*(num+1)/2)

sumnum(10000)
sum2(10000)
