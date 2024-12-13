def fibo(n):
    if n==1 or n==0:
        return 1
    else :
        return fibo(n-1)+ fibo(n-2)
    

#n=10
# print(f"le {n} ieme de fibonacci est : {fibo(n)}")

def SuiteFibo(n):
    my_list=[[],[]]
    i = 1 
    while True:
       numb= fibo(i)
       print(f"-->{numb}")
       if numb >=n:
           break
       my_list[0].append(numb)
       my_list[1].append(0)
       i +=1
    return my_list
#print(SuiteFibo(10))


def coder(n):
    my_list=[[],[]]
    i = 1 
    while True:
       numb= fibo(i)
       print(f"-->{numb}")
       if numb >=n:
           break
       my_list[0].append(numb)
       my_list[1].append(0)
       i +=1
    for i in range(len(my_list[0])-1, -1,-1):
        if my_list[0][i] <= n:
            my_list[1][i]=1
            n -= my_list[0][i]
    return my_list

#n=10
#print(coder(n))

def decoder(n):
    my_list=[[],[]]
    i = 1 
    while True:
       numb= fibo(i)
       print(f"-->{numb}")
       if numb >=n:
           break
       my_list[0].append(numb)
       my_list[1].append(0)
       i +=1
    for i in range(len(my_list[0])-1, -1,-1):
        if my_list[0][i] <= n:
            my_list[1][i]=1
            n -= my_list[0][i]
    S=0
    for i in range(len(my_list[1])):
        if my_list[1][i]==1:
            S +=my_list[0][i]
    print("finally ")
    return S


print(decoder(10))

