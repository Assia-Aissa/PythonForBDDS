def convert_to_binaire_8_bits(x):
    if x == 0:
        return [0]*8
    else:
        a = x // 2
        binaire = convert_to_binaire_8_bits(a)
        b = x % 2
        binaire.append(b)
        return binaire[-8:]



print(convert_to_binaire_8_bits(23))

def convert_to_binaire(x):
    binary_rep = []
    for i in range(8):
        binary_rep.insert(0, x % 2)  # Add the least significant bit at the beginning of the list
        x = x // 2 
    return binary_rep
print(convert_to_binaire(23))