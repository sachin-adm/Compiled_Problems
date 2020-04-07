for _ in range(int(input())):
    n, k = (int(i) for i in input().split())
    s = [int(i) for i in input().split()]
    a = sorted(s)
    s.sort(reverse = True)
    x = a.index(s[k-1])
    print(len(a[x:]))