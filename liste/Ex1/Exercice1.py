def chercher(x,T):
    for i in T:
        if i == x :
            return T.index(i)
    return -1
lista=[10,20,40,6,7]
a=10
print(chercher(a,lista))
            # Utiliser T.index(i) peut causer des problèmes 
            # si x est trouvé à un autre index que le premier
def chercherVersion2(x,T):
    for index in range(len(T)):
        if T[index]==x:
            return index
    return -1

listo = [10, 20, 10, 6, 7]
b= 10
print(chercher(b, listo))

### to return the last index of the element :
def chercher (x,T):
    last=-1
    for i in range(len(T)):
        if T[i]==x:
            last=i
    return last
listi= [10, 20, 10, 6, 7]
c = 10
print(chercher(c, listi)) 