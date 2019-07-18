c=int(input())
v=0
j=1
k=1
for a in range(c):
	print(k,end=' ')
	k=v+j
	v=j
	j=k          
