#!/opt/hts/bin/python
# -*- coding: utf-8 -*-

"""
    문제1
        num_1, num_2 의 변수를 가지고
        add_func(더하기), sub_func(빼기), div_func(나누기), multi_func(곱하기)를 한 값을
        view() 함수에서 출력하시요


    결과
        ***************
        더하기 : XXX
        빼기   : XXX
        나누기 : XXX
        곱하기 : XXX
        ***************

"""


def add_func(a,b):
    return a+b

def sub_func(a,b):
    if ((type(a)==int)and(type(b)==int)):
        if a>=b:
            return a-b
        else:
            return b-a
    return a-b

def div_func(a,b):
    return a/b

def multi_func(a,b):
    return a*b

def view(a,b):
    print("더하기:%d"%add_func(a,b))
    print("빼기%d"%sub_func(a,b))
    print("나누기:%d"%div_func(a,b))
    print("곱하기:%d"%multi_func(a,b))


def main():
    num_1 = 40
    num_2 = 20
    print 'default test'
    view(num_1,num_2)

if __name__ == "__main__":
    main()

#EOF
