#!/usr/bin/python
#-*-coding:utf-8-*-

def get_max_min(data_list):
    return max(data_list),min(data_list)

def get_txt_list(path):
    import os
    print os.system('ls')

def BMI():
    name=raw_input("Name:")
    height=float(input("Height:"))
    weight=float(input("weight:"))
    bmi=height/(weight*weight)
    print name,"님"
    if bmi<18.5:
        print "마름"
    elif bmi>=18.5 and bmi<25.0:
        print "표준"
    elif bmi>=25 and bmi <30.0:
        print "비만"
    elif bmi>30.0:
        print "고도 비만"

def add_start(start,end):
    total_sum=0
    for i in range(start,end+1):
        total_sum+=i
    print total_sum

def listCut(list):
    for i in range(len(list)):
        list[i]=list[i][0:3]
    print list

def dictget(dic,dict_word,except_str):
    if type(dic)!=dict:
        print "not dict!!"
        return
    try:
        dic[dict_word]
    except KeyError:
        dic[dict_word]=except_str
    print dic[dict_word]

if __name__=='__main__':
    #a=[1,5,6,7,4,9]
    #print get_max_min(a)
    #et_txt_list('/opt/bigeye')
    BMI()
    #add_start(2,20)
    #listCut(['Seoul', 'Daegu', 'Kwangju', 'Jeju'])
    #a={'test':1,'test2':2,'test4':4}
    #print type(a)
    #dictget(a,'tes','nono')




