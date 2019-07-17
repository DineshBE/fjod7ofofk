a1,b2 = map(int,input().split())
for i in range(a1,b2):
    temp = i
    m = 0
    while temp > 0:
        digit = temp % 10
        m += digit ** 3
        temp //= 10
    if m == l:
        print(m,end=" ")
