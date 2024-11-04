def multiplier(p1,p2):
    p3=[0] * (len(p1) + len(p2)-1)
    for i in range (len (p1)):
        for j in range(len(p2)):
            p3[i+j] += p1[i]*p2[j] 
    return p3
  
P1 = [2, 4, -3]  # Représente 2x^2 + 4x - 3
P2 = [1, -1]     # Représente x - 1
produit = multiplier(P1, P2)
print("Le produit de P1 et P2 est :", produit)   