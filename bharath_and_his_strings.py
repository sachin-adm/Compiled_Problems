for _ in range(int(input())):
    a = list(input())
    l1 = []
    for i in a:
        if i not in l1:
            l1.append(i)
    print(str(''.join(l1)))