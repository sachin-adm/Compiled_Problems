for i in range(input()):
    n = input()
    a = list(raw_input())
    ans,f=0,0
    for j in a:
        if j=='H':
            ans+=1
        elif j=='T':
            ans-=1
        if ans<0 or ans>1:
            f=1
            print "Invalid"
            break
    if f==0:
        if ans==0:
            print 'Valid'
        else:
            print 'Invalid'