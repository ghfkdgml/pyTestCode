#!-*-coding:utf-8-*-
import os,re
"""리눅스에서 vi로 파일을 열어 원하는 위치에 원하는 값을 입력하도록 설계된 코드"""

def insertToFile(path,stc,inputStc,rs=1):
    if not os.path.exists(path):
        print('Wrong path!')
        return
    f=open(path,'a+')
    while 1:
        a=f.readline()
        if not a:
            break
        #if a.strip()==stc.strip():
        if a.strip().find(stc)==0:
            #rs=int(input('End or next line?(0/1)'))
            if rs:
                print '%s match!'%path
                num=f.tell()
                break
            else:
                print '%s match!'%path
                num=f.tell()-len(a)+len(stc)
                break
        else:
            num=0
    if rs:
        result=addText(f,num,inputStc)
    else:
        result=addTextEnd(f,num,inputStc)
    #result=addTextEnd(f,num,inputStc)
    reinputStc(f,result)

def addText(f,num,stc):#num 위치(stc위치)로 이동해서밑에 내용을 result에 넣은 후 지우고 stc 삽입
    result=[]
    f.seek(num)
    for line in f.readlines():
        result.append(line)
    f.seek(num)
    f.truncate()
    f.write(stc+'\n')
    return result

def addTextEnd(f,num,stc):#addText와 같지만 다음줄에 삽입하지 않고 마지막 줄 뒤에 삽입
    result=[]
    f.seek(num)
    f.readline()
    for line in f.readlines():
        result.append(line)
    f.seek(num)
    f.truncate()
    f.write(stc+'\n')
    return result

def reinputStc(f,result):#지운 내용 다시 삽입
    for line in result:
        f.write(line)






#path="/etc/sudoers"#sudo 추가
#stc="root\tALL=(ALL) \tALL\n"
#inputStc="hts  ALL=NOPASSWD: ALL"
#insertToFile(path,stc,inputStc)
#path='/etc/pam.d/system-auth'#비밀번호 횟수 추가
#stc='auth        required      pam_deny.so\n'
#inputStc='auth        required      /lib/security/pam_tally.so deny=5 unlock_time=5 no_magic_root'
#insertToFile(path,stc,inputStc)
#try:
#    os.system('chmod 640 /etc/hosts')
#    print '/etc/hosts 권한 변경 완료!'
#except:
#    print 'hosts 권한 변경 실패'
#
#os.system('chmod –s /sbin/unix_chkpwd')
#os.system('chmod –s /usr/bin/ata')
#os.system('chmod –s /usr/bin/newgrp')
#print 'suid,sgid,stickybit 설정 완료!')
#
#os.system('find /dev -type f -exec ls {} \;|grep /dev/.udev|xargs rm')
#print '/dev 제거 완료!'
#
#pid=os.popen('ps -ef|grep automount').read().splitlines()[0].split()[1]
#os.system('kill -9 %d'%int(pid))
#print 'automount 제거 완료'
#
#pid=os.popen('ps -ef|grep autofs').read().splitlines()[0].split()[1]
#os.system('kill -9 %d'%int(pid))
#
#temp=os.popen('ls /etc/rc.d/rc*.d/*|grep autofs*').read().splitlines()
#
#for i in range(len(temp)):
#    b=temp[i].split('/')
#    c='/'.join(b[:-1])+'/_'+b[-1]
#    try:
#        os.system('mv %s %s'%(temp[i],c))
#    except:
#        print 'mv failed!'
#
#print 'autofs 제거 완료'
#
#path='/etc/login.defs'
#stc='PASS_MAX_DAYS'
#inputStc='     90'
#rs=0
#insertToFile(path,stc,inputStc,rs)
#LIST=[('/etc/sudoers','root\tALL=(ALL) \tALL\n','hts  ALL=NOPASSWD: ALL',1),
#        ('/etc/pam.d/system-auth','auth        required      pam_deny.so\n','auth        required      /lib/security/pam_tally.so deny=5 unlock_time=5 no_magic_root',1),
#        ('/etc/login.defs','PASS_MAX_DAYS','     90',0),
#        ('/etc/login.defs','PASS_MIN_LEN','     8',0)
#        ]
#
#for x,y,z,f in LIST:
#    insertToFile(x,y,z,f)
#    print '%s success!'%z
#
#try:
#    os.system('chmod 640 /etc/hosts')
#    print '/etc/hosts 권한 변경 완료!'
#except:
#    print 'hosts 권한 변경 실패'
#os.system('chmod -s /sbin/unix_chkpwd')
#os.system('chmod -s /usr/bin/at')
#os.system('chmod -s /usr/bin/newgrp')
#print 'suid,sgid,stickybit 설정 완료!'
#
#os.system('find /dev -type f -exec ls {} \;|grep /dev/.udev|xargs rm')
#print '/dev 제거 완료!'
#
#pid=os.popen('ps -ef|grep automount').read().splitlines()[0].split()[1]
#os.system('kill -9 %d'%int(pid))
#print 'automount 제거 완료'
#
#pid=os.popen('ps -ef|grep autofs').read().splitlines()[0].split()[1]
#os.system('kill -9 %d'%int(pid))
#
#temp=os.popen('ls /etc/rc.d/rc*.d/*|grep autofs*').read().splitlines()
#
#for i in range(len(temp)):
#    b=temp[i].split('/')
#    c='/'.join(b[:-1])+'/_'+b[-1]
#    try:
#        os.system('mv %s %s'%(temp[i],c))
#    except:
#        print 'mv failed!'
#
#print 'autofs 제거 완료'

