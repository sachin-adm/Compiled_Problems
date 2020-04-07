def binary_search(arr, l, r, k):
    while l <= r:
        m = (r + l) // 2
        if arr[m] >= k:
            r = m
        else:
            l = m + 1
        if l == r:
            if arr[l] >= k:
                return l
            else:
                return l + 1
    return l

for _ in range(int(input().strip())):
    n, q = map(int, input().strip().split())
    arr = list(map(int, input().strip().split()))
    arr.sort()
    cumm_sum = [0]
    for i in range(1, n + 1):
        cumm_sum.append(cumm_sum[i -1] + arr[i - 1])
    for i in range(q):
        k = int(input().strip())
        curr = binary_search(arr, 0, n - 1, k)
        l, r, prev = 0, curr - 1, curr
        while l <= r:
            m = (l + r) // 2
            if (k * (curr - m - 1)) - (cumm_sum[curr] - cumm_sum[m + 1]) <= m + 1:
                prev = m + 1
                r = m - 1
            else:
                l = m + 1
        print(n - prev)