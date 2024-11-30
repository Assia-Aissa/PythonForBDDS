
def motCle(mot,ListMotsCles):
    if mot in ListMotsCles:
        return True
    return False


mot1="si"
mot2='entier'
ListMotsCles=['si','sinon','tantque','pour','definir']
print(motCle(mot1,ListMotsCles))
print(motCle(mot2,ListMotsCles))