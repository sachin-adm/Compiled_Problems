N=int(input())
input_func=dict()
output_type=dict()
for i in range(N):
	a,b,c=input().split()
	input_func[b]=a
	output_type[a]=c
res=input_func["inp"]
next_type=output_type[res]
for i in range(N-2):
	res= input_func[next_type] +"." +  res
	next_type=output_type[input_func[next_type]]
if(N>1):
	res=input_func[next_type]+"." + res
print(res)