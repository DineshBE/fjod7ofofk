sd = input()
if((sd>='a' and sd<= 'z') or (sd>='A' and sd<='Z')):
    if(sd=='A' or sd=='a' or sd=='E' or sd =='e' or sd=='I' or sd=='i' or sd=='O' or sd=='o' or sd=='U' or sd=='u'):
        print("Vowel")
    else:
        print("Consonant")
else:
    print("Invalid")
