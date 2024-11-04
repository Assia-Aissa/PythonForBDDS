def Intersection(T1,T2):
    T=[]
    for i in T1:
        if i in T2:
            T.append(i)
    return T
T1 = [1, 2, 3, 4, 5]
T2 = [4, 5, 6, 7, 8]
resultat = Intersection(T1, T2)
print(resultat)