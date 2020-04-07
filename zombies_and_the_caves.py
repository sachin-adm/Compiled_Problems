from sys import stdin

def func(arr):
    n = len(arr)
    ans = [0 for i in range(n)]
    for i in range(n):
        ans[max(0,i-arr[i])]+=1
        if (arr[i] + i + 1) < n:
            ans[arr[i] + i + 1]-=1
    for i in range(1,n):
        ans[i]+=ans[i-1]
    return ans    
for _ in range(int(stdin.readline())):
    n = int(stdin.readline())
    arr_c = list(map(int,stdin.readline().split()))
    arr_h = sorted(list(map(int,stdin.readline().split())))
    ans = func(arr_c)
    ans = sorted(ans)
    if ans == arr_h:
        print("YES")
    else:
        print("NO")