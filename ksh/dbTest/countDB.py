#-*-coding:utf-8-*-
import sqlite3
import os
#다른 날짜 지정해서 확인 필요
def countDBRow(path):
    con=sqlite3.connect(path)
    result=con.execute('select count(*) from(select * from "LOGS");').fetchone()[0]
    con.close()
    return result

def dirExistCheck():
    d=raw_input('input directory want to check!')
    if not os.path.exists(d):
        print 'not exist!'
        dirExistCheck()
    else:
        path=d
        sum=0
        froms,tos=raw_input('input year,day(ex-2018-08-01 2018-08-08):').split()
        toY,toM,toD=map(int,tos.split('-'))
        fromY,fromM,fromD=map(int,froms.split('-'))
        if toY-fromY==0:                #같은 해일때
            gap=toM-fromM
            if gap>1:                   #다른 달일때(2달이상 차이)
                for x in dayCheck(fromM,fromD):
                    path=d+'/'+str(fromY)+'-'+str(fromM).zfill(2)+'-'+str(x).zfill(2)
                    for z in os.popen('cd %s;ls *.logsee'%path).read().splitlines():
                        sum=sum+countDBRow(path+'/'+z)
                for x in rdayCheck(toM,toD):
                    path=d+'/'+str(toY)+'-'+str(toM).zfill(2)+'-'+str(x).zfill(2)
                    for z in os.popen('cd %s;ls *.logsee'%path).read().splitlines():
                        sum=sum+countDBRow(path+'/'+z)

                for y in range(fromM+1,toM):
                    for x in dayCheck(y):
                        path=d+'/'+str(fromY)+'-'+str(y).zfill(2)+'-'+str(x).zfill(2)
                        for z in os.popen('cd %s;ls *.logsee'%path).read().splitlines():
                            sum=sum+countDBRow(path+'/'+z)

            elif gap==1:#1달 차이
                for x in dayCheck(fromM,fromD):
                    path=d+'/'+str(fromY)+'-'+str(fromM).zfill(2)+'-'+str(x).zfill(2)
                    for z in os.popen('cd %s;ls *.logsee'%path).read().splitlines():
                        sum=sum+countDBRow(path+'/'+z)
                for x in rdayCheck(toM,toD):
                    path=d+'/'+str(toY)+'-'+str(toM).zfill(2)+'-'+str(x).zfill(2)
                    for z in os.popen('cd %s;ls *.logsee'%path).read().splitlines():
                        sum=sum+countDBRow(path+'/'+z)

            else:#같은 달
                for x in range(fromD,toD+1):
                    path=d+'/'+str(fromY)+'-'+str(fromM).zfill(2)+'-'+str(x).zfill(2)
                    for z in os.popen('cd %s;ls *.logsee'%path).read().splitlines():
                        sum=sum+countDBRow(path+'/'+z)
        elif toY-fromY<0:
            print 'wrong year!'
        else:
            if int(fromM)!=12:#12월 아닐때 fromMonth
                for x in dayCheck(fromM,fromD):
                    path=d+'/'+str(fromY)+'-'+str(fromM).zfill(2)+'-'+str(x).zfill(2)
                    for z in os.popen('cd %s;ls *.logsee'%path).read().splitlines():
                        print z
                        sum=sum+countDBRow(path+'/'+z)
                for x in range(fromM+1,13):#fromMonth 이후 Month 계산
                    for y in dayCheck(x):
                        path=d+'/'+str(fromY)+'-'+str(x).zfill(2)+'-'+str(y).zfill(2)
                        for z in os.popen('cd %s;ls *.logsee'%path).read().splitlines():
                            print z
                            sum=sum+countDBRow(path+'/'+z)
            else:
                for x in dayCheck(fromM,fromD):
                    path=d+'/'+str(fromY)+'-'+str(fromM).zfill(2)+'-'+str(x).zfill(2)
                    for z in os.popen('cd %s;ls *.logsee'%path).read().splitlines():
                        sum=sum+countDBRow(path+'/'+z)


            if int(toM)!=1:
                for x in range(1,toM):#toMonth 이전 Month 계산
                    for y in dayCheck(x):
                        path=d+'/'+str(fromY)+'-'+str(x).zfill(2)+'-'+str(y).zfill(2)
                        for z in os.popen('cd %s;ls *.logsee'%path).read().splitlines():
                            sum=sum+countDBRow(path+'/'+z)
                for x in rdayCheck(toM,toD):#toMonth 계산
                    path=d+'/'+str(toY)+'-'+str(toM).zfill(2)+'-'+str(x).zfill(2)
                    for z in os.popen('cd %s;ls *.logsee'%path).read().splitlines():
                        sum=sum+countDBRow(path+'/'+z)
            else:
                for x in rdayCheck(toM,toD):#toMonth 계산
                    path=d+'/'+str(toY)+'-'+str(toM).zfill(2)+'-'+str(x).zfill(2)
                    for z in os.popen('cd %s;ls *.logsee'%path).read().splitlines():
                        sum=sum+countDBRow(path+'/'+z)

        print sum






def rdayCheck(m,d):
    Day_res=[]
    Day_res.append(range(1,d+1))
    return Day_res





def dayCheck(m,d=1):
    Month_31=[1,3,5,7,8,10,12]
    Month_30=[4,6,9,11]
    Day_res=[]
    if m in Month_31:
        Day_res=range(d,32)
    elif m in Month_30:
        Day_res=range(d,31)
    else:
        Day_res=range(d,28)
    return Day_res

if __name__=='__main__':
    dirExistCheck()
