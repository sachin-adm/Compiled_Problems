for i in range(int(input())):
        n=input()
        mini=n[1:]
        for i in range(1,len(n)):
            s=n[:i]+n[i+1:]
            if(s<mini):
                mini=s
        print(int(mini))