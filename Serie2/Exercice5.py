def identificateur(iden):
    ListMotsCles=['si','sinon','tantque','pour','definir']
    if iden[0].isdigit():
        return False
    if len(iden)< 80 and ' ' not in iden and iden not in ListMotsCles:
        return True
    return False
def analyserInstruction(inst):
    ListMotsCles=['si','sinon','tantque','pour','definir']
    inst = inst.strip() 
    if inst[0] =='#':
        return True
    parts=inst.split(" ",1)
    if len(parts) ==2:
        ident, rest = parts
        if identificateur(ident) and rest: 
            return True
        if ident in ListMotsCles and rest.endswith(':') and ' ' not in rest[:-1]:
            return True 
    return False     
inst1='si x<y:'
inst2='5=7'
inst3='alpha=5.55'
print(analyserInstruction(inst1))
print(analyserInstruction(inst2))
print(analyserInstruction(inst3))
        

