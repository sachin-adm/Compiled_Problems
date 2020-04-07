t=int(input())
for i in range(t):
    n,k=[int(x) for x in input().split()]
    m=[int(x) for x in input().split()]
    m = [x + k for x in m]
    count=0
    for i in m:
        if(i%7==0):
            count+=1
    print(count)