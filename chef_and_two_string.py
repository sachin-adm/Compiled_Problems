for _ in range(int(input())):
    a=input()
    b=input()
    c=t=0
    for i in range(len(a)):
        if(a[i]=='?' or b[i]=='?'):
            t+=1
            continue
        elif(a[i]!=b[i]):
            c+=1
    print(c,c+t)     