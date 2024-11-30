def logarithme_binaire(a):
    i=0
    b= 1
    while b<=a:
        b=2**i
        i+=1
    return b 
print(logarithme_binaire(5))
