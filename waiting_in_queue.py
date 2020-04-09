while T>0:
    m,n,k,l=map(int,input().split())
    a=list(map(int,input().split()))
    a.append(k)
    a=sorted(a)
    b=list([])
    time=0
    n=n*l
    for i in range(len(a)):
        if a[i]<=k:
            time=time+l
            b.append(n-a[i]+time)
    print(min(b))
    T=T-1