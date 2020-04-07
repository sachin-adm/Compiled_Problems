t = int(input())
for i in range(t):
    n = int(input())
    f = 1
    mat = list()
    for i in range(n):
        lis = list(map(int, input().split()))
        mat.append(lis)
    for l in mat:
        if 0 not in l:
            f = 0
    if f == 1:
        for i in range(n):
            k = 0
            for j in range(n):
                if mat[j][i] == 0:
                    k = 1
                    break
            if k == 0:
                f = 0
                break
    if f:
        print("YES")
    else:
        print("NO")