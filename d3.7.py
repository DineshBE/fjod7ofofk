y=input()
x=y.lstrip('-').replace('.','',1).isdigit()
if(x==True):
  print("Yes")
else:
  print("No")
