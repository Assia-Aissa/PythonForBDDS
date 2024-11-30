# Suite de Syracuse 
def Syracuse(n,N):
    if n==0 or N==1:
        return [N]
    else:
        if  N%2==0 :
            return [N]+ Syracuse(n-1,N/2)
        else:
            return [N]+ Syracuse(n-1,3*N+1)
        

N_initial = 7
iterations = 20  # Limite pour éviter les calculs trop longs
resultat = Syracuse(iterations, N_initial)
print(f"Suite de Syracuse pour N={N_initial} : {resultat}")