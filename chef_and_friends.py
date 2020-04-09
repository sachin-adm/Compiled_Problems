c=0
for i in range(int(input())):
    n=input()
    if ('ch' in n or 'he' in n or 'ef' in n):
        c+=1
print(c)