ch1=input ("the first chaine: ")
ch2=input("the second chaine: ")
if ch1 > ch2 :
    print(f"{ch2} précède {ch1}")
elif ch1< ch2:
    print(f"{ch1} précède {ch2}")
else:
    print(f"{ch2}et {ch1} identiques")
#Si CH1 est "inférieure" à CH2 dans l’ordre lexicographique, 
# afficher que CH1 précède CH2.
#Si CH1 est "supérieure" à CH2, afficher que CH2
#  précède CH1.