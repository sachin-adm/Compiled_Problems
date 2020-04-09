t=int(input())
for _ in range(t):
	N=int(input())
	A=[int(a) for a in input().split()]
	print( len(A) - len(set(A)) )