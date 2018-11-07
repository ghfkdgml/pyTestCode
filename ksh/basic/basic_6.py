#!/opt/hts/bin/python
# -*- coding: utf-8 -*-

"""
    문제6
        은하수벅스는 이번 여름에 고객들을 대상으로 사은품 프로모션을 진행하고 있습니다. 프로모션은 음료를 구매할 때마다 고객에게 스티커를 적립해줍니다.
        스티커는 음료의 종류에 따라 여름 음료 스티커와 일반 음료 스티커로 나뉘며, 5개 이상의 여름 음료 스티커를 포함한, 총 12개의 스티커를 모으면
        이를 하나의 텀블러로 교환할 수 있습니다.  연재는 현재 S 개의 여름 음료 스티커와 N 개의 일반음료 스티커를 가지고있는데, 이를 통해 받을 수 있는
        최대 텀블러의 수를 알고 싶어 합니다. 워낙 많은 스티커를 가지고 있으므로, 계산이 어렵다고 느낀 연재는 당신에게 이를 계산하는 프로그램을 작성해달라는
        요청을 받았습니다.

        스티커의 개수가 주어졌을 때 이를 통해 얻을 수 있는 최대 텀블러의 수를 출력하는 프로그램을 작성하세요

    입력
        입력은 여러 개의 테스트 케이스로 주어지며, 첫 줄에 테스트 케이스의 개수 T (1 ≤ T ≤ 10,000)가 입력됩니다.
        하나의 테스트 케이스는 0이상 260 − 1이하의 정수 S 와 N 이 입력되며, 두 숫자 사이에는 공백이 주어집니다.
        ex) 입력
        4
        12 0
        10 14
        4 20
        5 2147483648

    출력
        1
        2
        0
        1

"""
def couponCount():
    total_num=input("total test:")
    result=[]
    for i in range(total_num):
        summer_num=input("summer:")
        gen_num=input("general:")
        result.append(countMax(summer_num,gen_num))

    for j in range(len(result)):
        print("result:%d"% result[j])


def countMax(a,b):
    ret1=(a+b)/12
    if ret1==0 or a<5 or b<7:
        return 0
    ret3=1
    for i in range(5,12):
        ret2=min((a/i),(b/(12-i)))
        ret3=max(ret3,ret2)

    if ret1>ret3:
            ret1=ret3
    return ret1




def main():
    print 'default test'
    couponCount()

if __name__ == "__main__":
    main()


#EOF
