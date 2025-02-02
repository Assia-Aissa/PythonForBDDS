def binaire (N):
      #MyList=[]
      if N ==0:
            return 0
      
      else:
            return N%2 + 10*binaire(N//2)

#print(binaire(9))
#------------------------------
def binairee(N,MyLisst):
    while True:
            a=N // 2
            r=N%2
            MyLisst.append(r)
            if a==1:
                  MyLisst.append(a)
                  return list(reversed(MyLisst)) 
            else:         
                  N=a
    return list(reversed(MyLisst))   
    
#print(binairee(8,[]))
def binaire3(N, MyLisst):
    while N > 0:
        a = N // 2
        r = N % 2
        MyLisst.append(r)
        N = a
    return list(reversed(MyLisst))
    #return ''.join(map(str, reversed(MyLisst)))
print(binaire3(8, []))
#----------------------

