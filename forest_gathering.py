n, w, l = map(int, input().split())
tr = []


def check(t):
    rem = w
    for (h, r) in tr:
        temp = h + r * t
        if temp >= l:
            rem -= temp
        if rem <= 0:
            return True
    return False


for it in range(n):
    h, r = map(int, input().split())
    tr.append((h, r))
low = 0; high = 10**18; ans = 0
while low <= high:
    mid = low + high >> 1
    if check(mid):
        high = mid - 1
        ans = mid
    else:
        low = mid + 1
print(ans)