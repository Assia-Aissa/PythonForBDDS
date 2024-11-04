def est_palindrome(s):
    if len(s)<=1:
        return True
    if s[0]==s[-1]:
        return est_palindrome(s[1:-1])
    return False
print(est_palindrome('ojko'))
print(est_palindrome('OMO'))  # True
print(est_palindrome('LAVAL'))  # True
print(est_palindrome('engagelejeuquejelegagne'))  # True
print(est_palindrome('Soulane'))