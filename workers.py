n = input()
costArray = list(map(int , raw_input().split()))
typeArray = list(map(int , raw_input().split()))
ans = [int(2e9)] * 10
for i in xrange(n):
	ans[typeArray[i]] = min(ans[typeArray[i]], costArray[i])
print(min(ans[3], ans[1] + ans[2]))