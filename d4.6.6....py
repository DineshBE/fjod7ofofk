p=input()
w=0
for word in p:
  
  if word=='.'or word=='@'or word=='%'or word=='&'or word=='*'or word=='6'or word=='#'or word=='!'or word=='$' or word=='_':
    w+=1
  
print(w) 
