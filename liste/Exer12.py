def coversion(s):
    a=''
    for i in s:
        if i.isalpha():
            if i.isupper():
                a+=i.lower()
            else:
                a+=i.upper()
        else:
            a+=i
    return a
chaine = "Bonjour! Comment Ça Va? 123"
resultat = coversion(chaine)
print(resultat)          
        