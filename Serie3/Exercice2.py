# gestion des commentaires :
def comment(com):
    if com[0]=='#':
        return True
    return False
print(comment("hello"))
print(comment("#hello comment"))
#gestion d'espaces :
def suppEspaces(inst):
    # here replace method you have t asing the rusult to another variable 
    inst1=inst.replace(" ","")
    return inst1
print(suppEspaces('x   =    21'))