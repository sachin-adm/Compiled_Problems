def f(n):

	s = map(int, raw_input().split())
	low = []
	high = []

	for i in xrange(n - 1):
		low.append(min(s[i], s[i+1]))
		high.append(max(s[i], s[i+1]))
	low.sort()
	high.sort()
	curr = mx = 0
	i = j = 0
	n -= 1
	while i < n and j < n:
		if low[i] < high[j]:
			i += 1
			curr += 1
		else:
			j += 1
			curr -= 1
		mx = max(mx, curr)

	return mx	
 
n = int(raw_input())
print f(n)