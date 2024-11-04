def count_non():
    t=input("Introduisez votre nom et votre prénom : ")
    newChaine=t.replace(" ","")
    print(newChaine)
    c=0
    for i in newChaine:
         c+=1
    print(f"Votre nom est composé de {c} lettres.")

count_non()