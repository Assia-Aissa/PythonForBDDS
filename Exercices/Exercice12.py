def Convert(chaine):
    ch=""
    for i in chaine:
        if i.isupper():
            ch+=i.lower()
            
        else:
            ch+=i.upper()
    return ch
ch="Hello I am Here To Say Hi"
print(Convert(ch))
