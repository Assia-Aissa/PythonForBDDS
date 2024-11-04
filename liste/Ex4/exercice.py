def Mediane(T):
    T.sort()
    if len(T) % 2 ==1:
        b=len(T)//2
        return T[b]
    else:
        b1=len(T)//2-1
        b2=len(T)//2
        return (T[b1]+T[b2])/2
# Exemple d'utilisation
T1 = [3, 1, 2, 5, 4]  # Longueur impaire
T2 = [1, 3, 2, 5, 4, 6]  # Longueur paire

mediane_T1 = Mediane(T1)
mediane_T2 = Mediane(T2)

print("La médiane de T1 est :", mediane_T1)  # Devrait afficher 3
print("La médiane de T2 est :", mediane_T2) 