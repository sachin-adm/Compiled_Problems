t=int(input())

while t:
    n,m,k,l,r=map(int,input().split())
    sol=-1
    for i in range(n):
        c,p=map(int,input().split())
        for j in range(m):
            if c>k+1:
                c-=1
            elif c<k-1:
                c+=1
            else:
                c=k
        if c>=l and c<=r:
            if sol==-1 or sol>p:
                sol=p
    print(sol)        
    t-=1