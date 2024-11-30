import random
from typing import List


ventes={
    "Amine":14,
    "Rachid":19,
    "hamza":15,
    "Assia":21,
    "Rokia":21,
    "Taha":21,
    "Aya":17}
def function(v):
    L=v.values()
    s=max(L)
    for i in v:
        if v[i] ==s:
            return i
        
def max_v(v):
    max=max(v.values)
    vend=v.keys(max)
    vend=List(vend)
    return vend.random()


print(function(ventes))
print(max_v(ventes))