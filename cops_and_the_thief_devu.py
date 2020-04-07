t=int(input())
for i in range(t):
    m,x,y=map(int,input().split())
    M=list(map(int,input().split()))
    l=[]
    for i in M:
        if i<=x*y:
            m=1
            c=((x*y)+i)
            for j in range(m,c+1):
                if j not in l:
                  l.append(j)
        else:
            m=i-(x*y)
            c=(i+(x*y))
            for j in range(m,c+1):
                if j not in l:
                  l.append(j)
    l.sort()
    z=0
    for i in range(1,101):
            if i not in l:
                z+=1
    print(z)