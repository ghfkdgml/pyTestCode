#-*-coding:utf-8-*-
from random import *
import datetime

class LottoNum():
    totalNum=[]
    #def __init__(self,args):
    #    self.totalNum.append(args)

    def addNum(self,args):
        self.totalNum=self.totalNum+args

    def choiceNum(self):
        ret=[]
        for i in range(6):
            num=choice(self.totalNum)
            ret.append(num)
            for j in range(self.totalNum.count(num)):
                self.totalNum.remove(num)
        Day=checkSaturday()
        print Day.year,'년 ',Day.month,'월 ',Day.day,'일 ','로또 번호->',sorted(ret)



def checkSaturday():#실행하는 시간 기준 그 주 토요일 날짜 생성
    today=datetime.datetime.now()
    num=today.weekday()
    if num!=5:
        if num==6:
            retDay=today+datetime.timedelta(days=6)
        else:
            retDay=today+datetime.timedelta(days=5-num)

    else:
        retDay=today

    return retDay.date()




TOTALNUM={1:[1]*144,2:[2]*132,3:[3]*128,4:[4]*136,5:[5]*127,6:[6]*128,7:[7]*131,8:[8]*131,9:[9]*100,10:[10]*137,11:[11]*133,12:[12]*135,13:[13]*136,14:[14]*131,15:[15]*128,16:[16]*125,17:[17]*139,18:[18]*126,19:[19]*127,20:[20]*139,21:[21]*130,22:[22]*101,23:[23]*111,24:[24]*127,25:[25]*124,26:[26]*128,27:[27]*147,28:[28]*111,29:[29]*108,30:[30]*120,31:[31]*131,32:[32]*112,33:[33]*135,34:[34]*144,35:[35]*122,36:[36]*124,37:[37]*133,38:[38]*123,39:[39]*127,40:[40]*136,41:[41]*114,42:[42]*120,43:[43]*147,44:[44]*124,45:[45]*128}#지금까지의 로또 번호별 추첨횟수를 하드코드함 -->크롤링하여 받아오는 형태로 수정

test=LottoNum()
for i in range(len(TOTALNUM)):
    test.addNum(TOTALNUM[i+1])

test.choiceNum()
