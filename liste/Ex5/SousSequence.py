def AfficheSousSequences(T):
    first = []          
    current = []         
    for i in range(len(T)):
       
        if not current or T[i] > current[-1]:
            current.append(T[i])  
        else:
            
            if current:
                first.append(current) 
            current = [T[i]]  
    if current:
        first.append(current) 
    for seq in first:
        result = '<' + ', '.join(str(num) for num in seq) + '>'
        print(result)
T = [1, 2, 5, 3, 12, 25, 13, 8, 4, 7, 24, 28, 32, 11, 14]
AfficheSousSequences(T)
