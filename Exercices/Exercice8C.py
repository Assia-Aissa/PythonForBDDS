def Function():
    my_chaine= input("Enter somthing : ")
    new_chaine=my_chaine.replace(" ","")
    for i in range((len(new_chaine)//2)):
        print(f"{new_chaine[i]} || {new_chaine[-i-1]}")
       
        if new_chaine[-i-1]!=new_chaine[i] :
            return False
    return True
        
a = Function()
if a :
    print("is palindrome")
else:
    print("is not palindrome")