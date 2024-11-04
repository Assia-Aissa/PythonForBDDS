def reverse_text(T):
    return T [::-1]
print(reverse_text('assia el boussanni'))
###############
def inverser(s):
    if len (s) <=1:
        return s
    return s[-1]+inverser(s[:-1])
phrase = "voici une petite phrase !"
print(inverser(phrase))