#!/opt/hts/bin/python
# -*- coding: utf-8 -*-

"""
    문제4
        다음 list데이터를 조작하시요

        4-1 list데이터를 dict형태로 변경하시요
        4-2 list데이터를 list형식으로 바꾸면서 데이터를 조작하시요
        4-3 list데이터를 list안에 dict형태로 변경하시요
        4-4 4-1의 결과에 특이한점을 찾으시요

    결과
        4-1 결과 (dict 출력)
            {'blue': '10', 'gray': '12', 'apple': '10', 'fineapple': '3', 'green': '15', 'banana': '5', 'red': '11'}
        4-2 결과 (list출력 및 중복제거된 list출력)
            ['apple', 'banana', 'fineapple', 'red', 'blue', 'green', 'gray', 'apple']
            ['blue', 'gray', 'apple', 'fineapple', 'green', 'banana', 'red']
        4-3 결과 (list안에 dict출력)
            [{'apple': '10'}, {'banana': '5'}, {'fineapple': '3'}, {'red': '11'}, {'blue': '10'}, {'green': '15'}, {'gray': '12'}]


"""
LIST_DATA = [ 'apple,10', 'banana,5', 'fineapple,3', 'red,11', 'blue,10', 'green,15', 'gray,12', 'apple,12' ]

def view():
    temp = {}
    new_list = []
    temp_list = []
    text=LIST_DATA
    xdict=listTodict(text)
    print xdict
    listChange(text)

    #print temp
    #print new_list
    #print new_list
    #print temp_list

def listTodict(list):
    result={}
    for i in range(len(list)):
        fruit,num=list[i].split(',')
        result[fruit]=num
    return result

def listChange(list):
    result=[]
    #for i in range(len(list)):
    #    fruit=list[i].split(',')[0]
    #    result.append(fruit)
    a=listTodict(list)
    result=a.keys()
    print result
    print set(result)



def main():
    view()
    print 'default test'

if __name__ == "__main__":
    main()

#EOF
