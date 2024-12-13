def identificateur(iden):
    ListMotsCles=['si','sinon','tantque','pour','definir']
    if iden[0].isdigit():
        return False
    if len(iden)< 80 and ' ' not in iden and iden not in ListMotsCles:
        return True
    return False

def analyserInstruction(inst):
    ListMotsCles=['si','sinon','tantque','pour','definir']
    # if the inst start with a number 
    if inst[0].isdigit():
        return False 
    # strip it to delete white spaces 
    isnt= inst.strip()
    # check if it a comment 
    if isnt[0]=='#':
        return True
    # take just the first item of the isnt to analyse if it a key word
    parts=inst.split(" ",1)
    if len(parts)==2:
        first= parts[0]
        second = parts[1]
        if identificateur(first):
            return True
        if first in ListMotsCles and second.endswith(":") and ' ' not in second[:-1]:
            return True 
    return False
    

inst1='si x<y:'
inst2='5=7'
inst3='alpha=5.55'
print(analyserInstruction(inst1))
print(analyserInstruction(inst2))
print(analyserInstruction(inst3))