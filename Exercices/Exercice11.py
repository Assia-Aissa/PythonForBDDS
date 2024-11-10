while True:
    verbe=input("Enter the verbe :")
    print(verbe[-2:])
    if verbe[-2:]=="er": 
        break
pronon=['je','tu','il','nous','vous','ils']
verbe_conj=['e','es','e','ons','ez','ent']
radical_verb=verbe[:-2]
for i in range(6):
    print(f"{pronon[i]} {radical_verb}{verbe_conj[i]}")

