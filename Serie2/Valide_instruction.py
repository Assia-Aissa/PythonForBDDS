def identificateur(iden):
    ListMotsCles=['si','sinon','tantque','pour','definir']
    if iden[0].isdigit():
        return False
    if len(iden)< 80 and ' ' not in iden and iden not in ListMotsCles:
        return True
    return False
def analyserInstruction(inst):
    ListMotsCles=['si','sinon','tantque','pour','definir']
    if inst[0] =='#':
        return True
    elif identificateur(inst[0]) and inst[1]==' ' and isinstance(inst[2:],str) :
        return True
    elif inst[0] in ListMotsCles and isinstance(inst[1:],str) and inst[-1]==':' and " " not in inst:
        return True
    else:
        return False
inst1='si x<y:'
inst2='5=7'
inst3='alpha=5.55'
print(analyserInstruction(inst1))
        

