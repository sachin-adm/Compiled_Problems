for _ in range(int(input())):
    n=int(input())
    maxi=0
    mat=[[] for i in range(n)]
    for i in range(n):
        mat[i]=[int(x) for x in input().split()]
    trace=[0]*(2*n-1)
    for i in range(n):
        for j in range(n):
            trace[i-j+(n-1)]+=mat[i][j]
    print(max(trace))