pq,yz=list(map(str,input().split()))
count=0
for v in range(0,len(pq)):
    if(pq[v]!=yz[v]):
        count+=1
if(count==1):
     print("yes")
else:
    print("no")
