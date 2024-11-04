def conjuger(verbe):
    if verbe.endswith('er'):
        radical=verbe[:-2]
        print(radical)
        personnes = ['je', 'tu', 'il/elle/on', 'nous', 'vous', 'ils/elles']
        terminaisons = ['e', 'es', 'e', 'ons', 'ez', 'ent']
         
        for i in range(len(personnes)):
            print(f"{personnes[i]} {radical}{terminaisons[i]}")
    else:
        print("Ce n'est pas un verbe régulier en 'er'.")
verbe = input("Entrez un verbe régulier en 'er' : ")
conjuger(verbe)