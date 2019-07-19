xyz,88=map(int,input().split())
count=0
for l in range(xyz,88+1):
    if l>1:
        for p in range(2,l):
            if(l%p==0):
                break
        else:
            count=count+1
print(count)
