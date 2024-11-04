def est_Premier(p):
    if p < 2:
        return False
    for i in range(2, int(p ** 0.5) + 1):
        if p % i == 0:
            return False
    return True

def trouver_premiers(n):
    # Liste pour stocker les nombres premiers trouvés
    nombres_premiers = []
    for p in range(2, n):
        # On utilise est_Premier pour vérifier si p est un nombre premier
        if est_Premier(p):
            nombres_premiers.append(p)
    return nombres_premiers

# Exemple d'utilisation
n = 30
print(f"Les nombres premiers inférieurs à {n} sont : {trouver_premiers(n)}")
###################################333

# version 2:

def crible_eratosthene(n):
# On commence par créer une liste de booléens où chaque élément est initialisé à True
# (True signifie que le nombre est considéré comme premier).
 # On suppose que tous les nombres de 2 à n sont premiers, donc tous à True
    Liste=[True]*(n+1)
    p=2
 # On commence à partir de 2 (le premier nombre premier) et on élimine les multiples
    while (p * p <=n):
  # si Liste[p] est True , donc p est nombre premier
        if Liste[p]:
            for i in range(p*p, n+1,p):
                Liste[i] = False
        p +=1
    
    result= []
    for p in range(2,n):
        if Liste[p]:
            result.append(p)
    return result
n = 50
print(crible_eratosthene(n))