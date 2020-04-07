for i in xrange(int(raw_input())):
	n = int(raw_input())
	s = map(int, raw_input().split(' '))
	h = 0
	x = 1
	for i in s:
		if x is i:
			h += 1
			x += 1
		else:
			h -= 1
	if h is 1:
		print 'yes'
	else:
		print 'no'