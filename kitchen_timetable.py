t=input()
while t:
    n=input()
    a=raw_input().split()
    b=raw_input().split()

    ans = 0

    if(int(a[0]) >= int(b[0])):
        ans = 1

    for i in range(1, n):
        if int(a[i]) - int(a[i-1]) >= int(b[i]):
            ans += 1
    print ans
    t-=1