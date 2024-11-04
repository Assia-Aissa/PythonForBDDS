def derive_polynome(p1):
    p2=[]

    for i in range(1,len(p1)):
        p2.append(i*p1[i])
     

    return p2
derive_polynome([4,7,8])