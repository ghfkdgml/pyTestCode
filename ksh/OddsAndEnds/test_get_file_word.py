#-*-coding:utf-8-*-

def file_get_word():
    with open('test.txt','r') as f:

        a=f.readlines()
        for x in a:
            if len(x.strip())>=10:
                print x
exceptList=[',','.',"'","\"",'/','`']
def findWordInFile():
    with open('test.txt','r') as f:
        for x in f.readlines():
            for y in x.split():
                if 'c' in y:
                    for k in exceptList:
                        if k in y:
                            y=y.strip(k)
                    print y




if __name__=='__main__':
    #file_get_word()
    findWordInFile()
