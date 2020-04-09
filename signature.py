for _ in range(int(input())):
  N,M=map(int,input().split())
  mask=(1<<M)-1
  arrA=[None]*N
  pixA=[None]*N
  for i in range(N):
    inp=input().strip()
    pixA[i]=inp.count('1')
    arrA[i]=int(inp,2)
  pixels=sum(pixA)
  arrB=[None]*N
  for i in range(N):
    inp=input().strip()
    arrB[i]=int(inp,2)
  bst=2*N*M
  for i in range(-N,N+1):
    for j in range(-M,M+1):
      res=pixels
      for k in range(N):
        if 0<=k+i<N:
          res-=pixA[k+i]
          brow=arrB[k]
          if j<0:
            brow<<=-j
            brow&=mask
          else:
            brow>>=j
          res+=bin(brow^arrA[k+i]).count('1')
      bst=min(bst,res)
  print(bst)