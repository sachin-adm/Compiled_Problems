for i in range(int(input())):
    n=int(input())
    s=input()
    count=s.count('1')
    x=(count*(count-1))//2
    print(count+x)
    