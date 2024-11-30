from typing import List

def somme_ventes(vente):
    somme=0
    L=vente.values()
    L=list(L)
    for e in L:
        somme+=e
    return somme

def somventes(D):
    return (sum(D.values()))

ventes={
    "Amine":14,
    "Rachid":19,
    "hamza":15,
    "Taha":21,
    "Aya":17}
print(somme_ventes(ventes))

print(somventes(ventes))


