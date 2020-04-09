n1, n2, n3 = [int(i) for i in input().split()]
voters_list = {}

for _ in range(n1+n2+n3):
    id = int(input())
    if id not in voters_list:
        voters_list[id] = 0 
    voters_list[id] += 1

voters = []
for id, freq in voters_list.items():
    if freq>=2:
        voters.append(id)

print(len(voters))
voters.sort()
for id in voters:
    print(id)