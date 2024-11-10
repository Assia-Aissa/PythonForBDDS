def Occurence():
    chaine=input("enter your string: ")
    char=input("enter the char that you looking for: ")
    n_Occurnce=chaine.count(char)
    return n_Occurnce

print(f"{Occurence()}")