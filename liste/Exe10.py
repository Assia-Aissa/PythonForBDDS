def lexicograph(s,t):
    if s<t:
        print(f"{s} precede(before) {t}")
    elif s>t:
        print(f"{s} suit(after) {t}")
    else:
        print(f"{s} same as {t}")
lexicograph('ABC','abc')
lexicograph('A','a')
lexicograph("hello",'bye')