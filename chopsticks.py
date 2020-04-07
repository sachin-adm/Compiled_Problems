n,d = map(int,input().split())
l = []
count = 0
i = 1
for _ in range(n):
    l.append(int(input()))
l.sort()
while i < n:
    if l[i] - l[i-1] <= d:
        i += 2
        count += 1
    else:
        i += 1
print(count)