for h in range(int(input())):
    s = input()
    overlap = [0 for i in range(len(s))]
    for i in range(len(s)):
        if s[i] != '.':
            ini = i-int(s[i])
            fin = i+int(s[i])
            if ini < 0:
                ini = 0
            if fin > len(s)-1:
                fin = len(s)-1
            for i in range(ini, fin+1):
                overlap[i] += 1
    for i in overlap:
        if i > 1:
            print("unsafe")
            break
    else:
        print("safe")
