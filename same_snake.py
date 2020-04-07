T=input()
for i in range(T):
    s1=raw_input()
    s1=s1.split(' ')
    s2=raw_input()
    s2=s2.split(' ')
    a1,a2,a3,a4=map(int,s1)
    b1,b2,b3,b4=map(int,s2)
    s1=[(a1,a2),(a3,a4)]
    s2=[(b1,b2),(b3,b4)]

    if (a1==a3==b1==b3):
        if (max(a2,a4,b2,b4)-min(a2,a4,b2,b4))<(abs(a2-a4)+abs(b2-b4)+1):
            print 'yes'
        else:
            print 'no'
    elif (a2==a4==b2==b4):
        if (max(a1,a3,b1,b3)-min(a1,a3,b1,b3))<(abs(a1-a3)+abs(b1-b3)+1):
            print 'yes'
        else:
            print 'no'
    elif (a1==a3 and b2==b4) or (b1==b3 and a2==a4):
        a=1
        for i in s1:
            for j in s2:
                if i==j:
                    print 'yes'
                    a=0
        if a:
            print 'no'
    else:
        print 'no'