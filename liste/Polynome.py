

from copy import deepcopy


def polynome(T):
    Coeffic=[]
    degree=[]
    for i in range(len(T)):
        Coeffic.append(i*T[i])
        degree.append(i)
        
    for i in range(len(T)):
        print(f"{Coeffic[i]},{degree[i]}",end="")
    
        

t=[3,3,5,2,7,1]
print(polynome(t))
###########################
# indice est l'index
def derive(p):
    return [p[i]*i for i in range(1,len(p))]

##########################
# [[co,deg]]
def deriver(p1):
    p= deepcopy(p1)
    for i in range(0,len(p)):
        p[i][0] *=p[i][1]
        p[i][1] -=1