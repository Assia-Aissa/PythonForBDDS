def Char_number():
    name= input("Enter a description about you: ")
    new_name=name.replace(" ","")
    print(new_name)
    n=len(new_name)
    return n
print(f"your name contain {Char_number()} letter")

