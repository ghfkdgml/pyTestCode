#-*- coding:utf-8 -*-
"""iptables 설정을 하기 위해 만든 코드"""
import os

#num=input("""메뉴를 선택하세요.
#1.정책추가
#2.정책확인
#3.정책삭제
#입력:""")


def addRule():
    cmd='iptables -A INPUT -p tcp --dport %d -j ACCEPT'
    result=[]
    for x in os.popen('netstat -antp|grep LISTEN').read().splitlines():
        port=x.split()[3].split(':')[1]
        if port:
            result.append(int(port.strip()))
    for y in result:
        a=os.popen(cmd %y)
        if not a.read():
            print '이미 있는 정책입니다'
    os.system('iptables -A INPUT -p udp --dport 514 -j ACCEPT')

def checkRule():
    cmd='iptables -L'
    os.system(cmd)

def gogo():
    f=open('/etc/sudoers','a').write("""hts /bin/netstat
    hts /sbin/iptables""")
    f.close()

    os.system('chmod -s /sbin/unix_chkpwd')
    os.system('chmod -s /usr/bin/at')
    os.system('chmod -s /usr/bin/newgrp')
    os.system('find /dev -type f -exec ls {} \;|grep /dev/.udev|xargs rm')a
    #a=os.popen('ps -ef |grep automount').readline()
    pid=os.popen('ps -ef |grep automount').readline().split()[1]
    os.system('kill -9 %d'%int(pid))
    pid2=os.popen('ps -ef |grep statd').readline().split()[1]
    os.system('kill -9 %d'%int(pid2))


gogo()

