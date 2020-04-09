def readInt():
    return int(input())

def readInts():
    return [int(x) for x in input().split()]

def cases():
    numCases = readInt()
    for _ in range(numCases):
        n, m, x, y = readInts()
        yield n, m, x, y

def solve(n, m, x, y):
    total = 0
    for c in range(1, m+1):
        part = (m - c)*(n-1)*n - n*n + n
        if m - c < n - 1:
            t = n - 1 - m + c
            part += t*(t+1)
        total += part
    total -= (m - y)*(n - 1) - min(n - x, m - y) - min(x - 1, m - y)
    total -= (y - 1)*(n - 1) - min(n - x, y - 1) - min(x - 1, y - 1)
    total *= 2
    total += (n - x)*(x - 1)*2 + (m - y)*(y - 1)*2 + min(n - x, y - 1)*min(x - 1, m - y)*2
    total += min(x - 1, y - 1)*min(n - x, m - y)*2
    return total

for data in cases():
    print(solve(*data))