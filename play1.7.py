int = input()
widt = len(int)
mylist = []
for k in range(0,widt,2):
    mylist.append(int[k:k+2][::-1])
print("".join(mylist))
