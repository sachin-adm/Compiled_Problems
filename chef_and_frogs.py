n,k,p = list(map(int,input().split()))
a = list(map(int,input().split()))
so = sorted(a)
d = {}
start  =so[0]
d[start] = start
for i in range(1,n):
    if so[i]-so[i-1]<=k:
        d[so[i]] = start
    else:
        start = so[i]
        d[so[i]] = start
for i in range(p):
    x,y = list(map(int,input().split()))
    if d[a[x-1]] == d[a[y-1]]:
        print("Yes")
    else:
        print("No")