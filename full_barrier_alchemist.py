for _ in range(int(input())):
    N,H,Y1,Y2,L=map(int,input().split())
    l=[]
    for i in range(N):
        T,Y=map(int,input().split())
        l.append((T,Y))
    p=0
    for i in range(N):
        if l[i][0]==1:
            if (H-Y1)>l[i][1]:
                L-=1
        else:
            if Y2<l[i][1]:
                L-=1
        if L==0:
            break
        p+=1
    print(p)