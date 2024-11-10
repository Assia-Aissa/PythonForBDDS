def delete_caractere(ch,x):
    while x in ch:
        ch.remove(x)
    return ch
ch=[7,9,0,7,5,40,0,0,3,0]
print(delete_caractere(ch,0))
