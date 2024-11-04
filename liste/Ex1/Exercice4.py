def delete_occurrence(T,x):
    while x in T:
        T.remove(x)
    return T
a=45
A=[45,65,343,45,76,54,45,45,90,1,4,45]
print(delete_occurrence(A,a))
