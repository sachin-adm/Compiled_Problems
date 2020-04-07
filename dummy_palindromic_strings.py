for _ in range (int(input())):
    x=input()
    se=[0]*125
    l=len(x)
    c=0
    if l%2==0:
        for i in range (l):
            se[ord(x[i])]+=1
        for i in range (97,124):
            if se[i]%2!=0:
                c+=1
        if c==2:
            print("DPS")
        else:
            print("!DPS")
    elif l%2!=0:
        for i in range (l):
            se[ord(x[i])]+=1
        for i in range (97,124):
            if se[i]%2!=0:
                c+=1
        if c==3 or c==1:
            print("DPS")
        else:
            print("!DPS")