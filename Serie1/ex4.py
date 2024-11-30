def Est_premier(n):
    if n<=1 :
        return False
    if n==2 : 
        return True
    if n % 2 ==0:
        return False
    else :
        for i in range(3,int(n**0.5+1),2):
            if n %i ==0:
                return False
            
    return True
print(Est_premier(7))  
print(Est_premier(10))
print(Est_premier(2))  
print(Est_premier(1))