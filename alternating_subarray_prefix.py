t = int(input())
for _ in range(t):
    n = int(input())
    l = list(map(int,input().split()))
    ans = [None]*n 
    ans[n-1] = 1 
    for i in range(n-2,-1,-1):
        if l[i]*l[i+1]<0:
            ans[i] = ans[i+1]+1 
        else:
            ans[i] = 1
    for i in ans:
        print(i,end = " ")
    print()