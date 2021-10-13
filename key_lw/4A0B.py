import random
re=1
while(re==1):
    print("""欢迎来到猜数字游戏，电脑将随机生成一个四位的各位不重复的数字（可能以0开头）。对于玩家输入的每一个四位数，电脑将以XAYB的形式反馈。XA表示玩家输入的数字中有X个数字位置与数值均正确；YB表示玩家输入的数字中有Y个仅数值正确，但位置不正确。\n请输入数字:""")
    l=[]
    while(len(l)<4):
        a=random.randint(0,9)
        if (a not in l):
            l.append(a)
    #print(l)
    a=0
    b=0
    c=0
    while(a!=4):
        a=0
        b=0
        s=int(input())
        c=c+1
        li=[None]*4
        for i in range(0,4):
            li[i]=s//(10**(3-i))
            s=s%(10**(3-i))
        for i in li:
            if(i in l and li.index(i)==l.index(i)):
                a=a+1
            elif(i in l):
                b=b+1
        print(a,"A",b,"B","所用次数",c)
    print("游戏胜利","\n","输入1以再来一盘、0以结束游戏")
    re=int(input())