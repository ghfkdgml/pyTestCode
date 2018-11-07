#-*-coding:utf-8-*-

def ngram():
    n=int(input("input num!"))
    text='Python is a programming language that lets you work quickly'
    words=text.split()

    if len(words)<n:
        print "wrong text and num!"
    else:
        for i in range(len(words)-n+1):
            print ' '.join(words[i:i+n])

def wordChecker(word):
    checkList=['.',',',"'"]
    for x in checkList:
        if x in word:
            word=word.replace(x,'')
    return word

def palindrom(word):
    wordChecker(word)
    check=True
    for i in range(len(word)/2):
        if word[i]!=word[-1-i]:
            check=False
    return check





if __name__=='__main__':
    test=['apache','decal','did','neep','noon','refer','river']
    for x in test:
        if palindrom(x):
            print x


