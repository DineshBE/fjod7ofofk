y1=input()
if((y1>='a' and y1<='z') or (y1>='A' and y1<='Z')):
  y1=y1.lower()
  if(y1=='a' or y1=='e' or y1=='i' or y1=='o' or y1=='u'):
     print("Vowel")
  else:
     print("Consonant")
else:
    print("Special Characters")
