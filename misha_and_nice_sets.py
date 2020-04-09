T = int(input())
for z in range(T):
    L,R,G = map(int, input().split())
    mx = R//G
    mn = L//G
    if L%G == 0:
        mn -= 1
    ans = mx-mn
    if ans== 1:
        if G>= L and G<= R:
            print(1)
        else:
            print(0)
    else:
        print(ans)