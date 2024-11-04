def Fusion(T1,T2):
    T3=[]
    i,j=0,0

    while i<len(T1) and j<len(T2):
        if T1[i]<T2[j]:
            if T3[-1] != T1[i]: 
                T3.append(T1[i]) 
            i +=1
        elif T1[i] > T2[j]:
            if  T3[-1] != T2[j]:
                T3.append(T2[j]) 
            i +=1
        else:  # Si T1[i] == T2[j], ajouter une seule fois
            if  T3[-1] != T1[i]:  
                T3.append(T1[i])
            i += 1
            j += 1
            #Ajouter le reste T1
    while i < len(T1):
        if T3[-1] != T1[i]:
            T3.append(T1[i])
        i += 1

    # Ajouter le reste  T2
    while j < len(T2):
        if T3[-1] != T2[j]:  
            T3.append(T2[j])
        j += 1

    return T3
        
#########################################
















