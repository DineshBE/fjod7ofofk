a,z=map(int,input().split())
for p in range (a+1,z):
    for q in range(2,p):
        if (p%q==0):
            break
    else:
        print(p, end=' ')
