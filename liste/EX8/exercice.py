
def Fusion_f(T1,T2):
    A=T1+T2
    return sorted(list(set(A)))


T1=[4,7,8,6,5,3,4,9]
T2=[7,9,23,5,77,65]
print(Fusion_f(T1,T2))