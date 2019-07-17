p1,q2 = map(int,input().split())
for j in range(p1,q2):
    temp = j
    s = 0
    while temp > 0:
        digit = temp % 10
        s += digit ** 3
        temp //= 10
    if j == s:
        print(j,end=" ")
