#!/opt/hts/bin/python
# -*- coding: utf-8 -*-

"""
    문제2
        특정문자열을 parsing 해보시요

        Tasks 에서는 zombie의 값만
        Cpu 에서는 idle 값만
        Mem 에서는 total 값만
        Swap 에서는 used 값만 출력을 하시요

    결과
        ********************
        2015-07-24 17:12:22
        ********************
        Task : 0 zombie
        Cpu  : 95.8%id
        Mem  : 1020348k total
        Swap : 1003708k used

"""
TEXT = """
Tasks: 182 total,   1 running, 181 sleeping,   0 stopped,   0 zombie
Cpu(s):  3.1%us,  0.7%sy,  0.0%ni, 95.8%id,  0.3%wa,  0.0%hi,  0.0%si,  0.0%st
Mam:   1020348k total,   902540k used,   117808k free,    35768k buffers
Swap:  2064376k total,  1003708k used,  1060668k free,   157344k cached
"""
import time


def view(msg):
    print msg


def parsing(msg,delimit=','):
    ret=msg.split(delimit)
    if ret[0].startswith('Task'):
        result=ret[4].strip()
        return 'Task',result
    elif ret[0].strip().startswith('Cpu'):
        result=ret[3].strip()
        return 'Cpu',result
    elif ret[0].strip().startswith('Mam'):
        result=ret[0].split(':')[1].strip()
        return 'Mam',result
    elif ret[0].strip().startswith('Swap'):
        result=ret[1].strip()
        return 'Swap',result
    else:
        return 'no','no'


def read(TEXT):
    #result={}
    for line in TEXT.split('\n'):
        x,y=parsing(line)
        print("%s:%s"%(x,y))
        #result.append(parsing(line))


def main():
    now = time.strftime("%Y:%m:%d")
    print '###########'
    print now
    print '###########'
    text="""Tasks: 182 total,   1 running, 181 sleeping,   0 stopped,   0 zombie
    Cpu(s):  3.1%us,  0.7%sy,  0.0%ni, 95.8%id,  0.3%wa,  0.0%hi,  0.0%si,  0.0%st
    Mam:   1020348k total,   902540k used,   117808k free,    35768k buffers
    Swap:  2064376k total,  1003708k used,  1060668k free,   157344k cached"""
    read(text)

if __name__ == "__main__":
    main()

#EOF
