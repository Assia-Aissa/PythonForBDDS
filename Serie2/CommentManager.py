def comment(com):
    if com[0]=='#':
        return True
    else:
        return False
    
c='#hello there'
notc='hello there'
print(comment(notc))