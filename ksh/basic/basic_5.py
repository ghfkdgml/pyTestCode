#!/opt/hts/bin/python
# -*- coding: utf-8 -*-

"""
    문제5
        아래 fruit_store 의 값을 fruit_list의 내용을 읽어 fruit_store에 반영하시요.

    결과
        {'strwberry': 11, 'grape': 22, 'apple': 7, 'banana': 11}

"""

fruit_store = {'apple':5, 'banana':3, 'grape':10}
fruit_list = [
    'apple count 2',
    'banana count 8',
    'grape count 12',
    'strwberry count 11'
    ]


class FruitStore(object):
    def __init__(self,fruit_store):
        self.fruit_store=fruit_store

    def buy_fruit(self,list):
        print 'start!'
        print list
        for i in range(len(list)):
            fruit,_,num=list[i].split()
            if fruit in self.fruit_store:
                self.fruit_store[fruit]+=int(num)
            else:
                self.fruit_store[fruit]=int(num)
        print fruit_store

    def run(self,list):
        self.buy_fruit(list)

def main():
    FS = FruitStore(fruit_store)
    FS.run(fruit_list)

if __name__ == "__main__":
    main()

#EOF
