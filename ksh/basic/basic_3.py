#!/opt/hts/bin/python
# -*- coding: utf-8 -*-

"""
    문제3
        다음 list데이터를 조건에 맞추어 출력하시요

        ex) 'A,15,seoul' >> '이름,나이,지역'

        3-1 : 나이가 14 이상이고 지역이 seoul인 것들만 출력
        3-2 : 나이가 큰순서데로 리스트를 다시 출력하시요

    결과
        A,15,seoul
        E,19,seoul
        ********************
        E,19,seoul
        F,18,busan
        G,17,anyang
        D,16,busan
        A,15,seoul
        B,14,busan
        C,11,sungnam
        ********************


"""
LIST_DATA = [
        'A,15,seoul'
        ,'B,14,busan'
        ,'C,11,sungnam'
        ,'D,16,busan'
        ,'E,19,seoul'
        ,'F,18,busan'
        ,'G,17,anyang'
        ]
def parse(txt):
    ret=txt.split(',')
    if ret[1]>14 and ret[2]=='seoul':
        return txt,1
    else:
        return txt,0


def main():
    print 'default test'
    data=LIST_DATA
    list_in=[]
    for text in LIST_DATA:
        msg,ret=parse(text)
        if ret==1:
            list_in.append(msg)
            data.remove(msg)

    print '*******************'
    for i in range(0,len(list_in)):
        print list_in[i]
    print '*******************'
    for i in range(0,len(data)):
        print data[i]






if __name__ == "__main__":
    main()

#EOF
