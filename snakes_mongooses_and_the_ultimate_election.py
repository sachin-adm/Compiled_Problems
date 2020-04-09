T = int(raw_input())

for case in range(T):
    S = raw_input()
    eat = 0
    snake = 0
    mon = 0
    for i in S:
        if i == "m":
            mon += 1
        else:
            snake += 1
    sls = list(S)
    for i in range(snake+mon):
        if sls[i] == "m":
            if i > 0 and sls[i-1] == "s":
                eat += 1
            elif i+1 < snake + mon and sls[i+1] == "s":
                sls[i+1] = "."
                eat += 1
    if mon == snake - eat:
        print "tie"
    elif mon > snake - eat:
        print "mongooses"
    elif mon < snake - eat:
        print "snakes"