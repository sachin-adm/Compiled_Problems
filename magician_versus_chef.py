t=int(input())
while(t):
    n,x,s=[int(n) for n in input().split()]
    while(s):
        a,b=[int(a) for a in input().split()]
        if(a==x):
            x=b
        elif(b==x):
            x=a
        s-=1
    print(x)
    t-=1