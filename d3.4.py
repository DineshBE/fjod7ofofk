x = int(input())
y = list(map(int,input().split()[:x]))
z = sorted(y)
for k in z:
    print(k,end=" ")
