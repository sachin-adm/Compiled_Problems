for _ in  range(int(input())):
    a,b,c=map(int,input().split())
    t=(2*a)/c
    tt=(a*(2**0.5))/b
    if t>tt:
        print("Stairs")
    else:
        print("Elevator")