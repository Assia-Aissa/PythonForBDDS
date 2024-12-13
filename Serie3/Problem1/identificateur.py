def identificateur(iden):
    ListMotsCles=['si','sinon','tantque','pour','definir']
    if iden[0].isdigit():
        return False
    if len(iden)< 80 and ' ' not in iden and iden not in ListMotsCles:
        return True
    return False 

        
print(identificateur('2hello'))
print(identificateur('variable'))
print(identificateur('si'))