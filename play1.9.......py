gire,arun=map(int,input().split())
count=0
for z in range(gire,arun+1):
  if z>1:

    for b in range(2,z):
      if z%b==0:
        break
    else:
      count=count+1
print(count)
