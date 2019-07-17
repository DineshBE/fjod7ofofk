q2=int(input())
z=q2
sum=0
while q2>0:
    sum+=((q2%10)**3)
    q2=q2//10
if (sum==z):
    print('yes')
else:
    print('no')
