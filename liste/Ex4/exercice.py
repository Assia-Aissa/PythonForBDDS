def Mediane(T):
    T.sort()
    if len(T) % 2 ==1:
        b=len(T)//2
        return T[b]
    else:
        b1=len(T)//2-1
        b2=len(T)//2
        return (T[b1]+T[b2])/2

T1 = [3, 1, 2, 5, 4] 
mediane_T1 = Mediane(T1)
print("La médiane de T1 est :", mediane_T1)  # Devrait afficher 3
 