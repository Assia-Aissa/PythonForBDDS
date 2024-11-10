def reverse_String():
    chaine = input("Enter your string: ")
    new_chaine=chaine.split()
    print(new_chaine)
    for char in new_chaine[::-1]:  
        print(f"{char[::-1]} ",end=" ")
    
reverse_String()