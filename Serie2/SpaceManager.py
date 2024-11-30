def suppEspaces(inst):
    new_inst=inst.replace(" ","")
    return new_inst

instruction='    x  =    21'
print(suppEspaces(instruction))