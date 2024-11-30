def factoriel(n):
    r=1
    for i in range(1,n):
        r=n*i
    return r
print(factoriel(3))

#fonction recursive :)
def factoriel2(n):
    if n==0 :
        return 1
    else:
        return n*factoriel2(n-1)
print (factoriel2(3)) 