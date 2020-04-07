t=int(input())
for i in range(t):
    s=list(str(input()))
    n=len(s)
    if(len(s)%2==0):
        a=s[0:len(s)//2]
        b=s[len(s)//2:len(s)]
    else:
        a=s[0:len(s)//2]
        b=s[(len(s)//2)+1:len(s)]
    a.sort()
    b.sort()
    if(a==b):
        print("YES")
    else:
        print("NO")