def entier(b):
    # Remove spaces or extra characters
    b = b.strip()
    
    # Validate the input
    if not all(c in '01' for c in b):
        raise ValueError("Input must be a binary")
    R = 0
    for i in b:
        R = R * 2 + int(i)
    print(R)


entier("0")  
