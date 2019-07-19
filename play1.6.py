ab,yz=map(str,input().split())
for q in range(len(ab)):
    if(ab.count(ab[q])==yz.count(yz[q])):
        print("yes")
        break
    else:
        print("no")
        break
