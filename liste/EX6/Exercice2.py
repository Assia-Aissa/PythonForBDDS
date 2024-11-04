def Complement(T1, N):
   
    compl = []

    # boucle pour chaque entier de 0 à N
    for i in range(N + 1): 
        
        if i not in T1:
            compl.append(i) 

    return compl

# Exemple d'utilisation
T1 = [0, 1, 2, 4, 6, 8, 9] 
N = 10
resultat = Complement(T1, N)
print(resultat) 
