def rec_ans(l):
    if l < 2:
        return 0
    elif l == 2:
        return 2
    elif l%2:
        return l + rec_ans(l//2) + rec_ans(l//2+1)
    else:
        return l + 2*rec_ans(l//2)
        
from sys import stdin
for _ in range(int(input())):
    n,m = list(map(int,stdin.readline().strip().split()))
    rw = rec_ans(n+1)
    ans = max(-1,m-rw)
    if ans != -1:
        ans = max(0,m-(n+1)*(n+2)//2+1)
    print(ans)