for _ in range(int(input())):
    c,d,l=[int(c) for c in input().split()]
    nl=(c+d)*4
    if(c<=(2*d)):
        k=d*4
    else:
        k=(c-d)*4
    if(l%4==0 and (l>=k and l<=nl)):
        print('yes')
    else:
        print('no')