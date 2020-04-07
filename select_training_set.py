T=int(input())
for i in range(T):
    N=int(input())
    d=dict()
    for j in range(N):
        i=input().split()
        w=i[0]
        b=int(i[1])
        if w in d:
            d[w][b]+=1
        else:
            d[w]=[0,0]
            d[w][b]+=1
    S=0
    for i in d.values():
        S+=max(i)
    print(S)