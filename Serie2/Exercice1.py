def convert_binaire(num):
    if num==0:
        return [0,0,0,0]
    else:
        a=num//2
        b=num%2
        
        return convert_binaire(a)+[b]
while True:
    num= int(input("enter number: "))
    if num <=255:
        break
if num==0:
    print([0,0,0,0,0,0,0,0])
else:
    print(convert_binaire(num))
   




