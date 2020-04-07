for i in range(int(input())):
    n=int(input())
    arr=list(map(int,input().split()))
    count=0
    for i in range(n-1):
        if(arr[i]>arr[i+1]):
            count+=1 
        if(count>1):
            break 
    if(count>1):
        print('NO')
    else:
        if(count==0):
            print('YES')
        elif(arr[0]<arr[-1]):
            print('NO')
        else:
            print('YES')
