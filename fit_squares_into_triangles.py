import sys 
sys.setrecursionlimit(10**9) 
input = sys.stdin.readline

def solve(b):
    if b<=2: 
        return 0
    return (b//2 - 1) + solve(b-2)

t=int(input())
for _ in range(t):
    base=int(input())
    print( solve(base) )