def solve(s):
    ar = [c for c in s] 
    n = len(s)
    mid = (n - 1) // 2
    for i in range(mid+1):
        if ar[i] == '.' and ar[n-i-1] == '.':
            ar[i] = ar[n-i-1] = 'a'
        elif ar[i] == '.':
            ar[i] = ar[n-i-1]
        elif ar[n-i-1] == '.':
            ar[n-i-1] = ar[i]
        elif ar[i] != ar[n-i-1]:
            return -1
    return ''.join(ar)

for _ in range(int(input())):
    s = input()
    print(solve(s))