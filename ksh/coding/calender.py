#-*-coding:utf-8-*-

def dayofweek(mon,day):
    days=[31,29,31,30,31,30,31,31,30,31,30,31]
    week=["Sunday","Monday","Tuesday","Wednesday","Thursday","Friday","Saturday"]
    ret=0
    for x in range(mon-1):
        ret+=days[x]
    ret+=day
    print("%d월 %d일은 %s입니다."%(mon,day,week[ret%7]))


dayofweek(4,5)
