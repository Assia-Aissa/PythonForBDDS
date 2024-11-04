def calculer_moyenne(T):
    somme=0
    for i in range(len(T)):
        somme += T[i]
    return somme/ len(T)
myList=[1,2,3,4,5,6,7,8,9,10]
print(calculer_moyenne(myList))
