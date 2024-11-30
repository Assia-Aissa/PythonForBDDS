# Key words 
def motCle(mot,ListMotCles):
    if mot in ListMotCles:
        return True
    return False
a='si'
b='hello'
ListMotCles=['si','sinon','tantque','pour','definir']
print(motCle(a,ListMotCles))
print(motCle(b,ListMotCles))
