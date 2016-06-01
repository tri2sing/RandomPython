

def strlen (inStr):
    if not inStr: return 0
    else: return( 1 + strlen (inStr[1:]))

def strreverse (inStr):
    if not inStr: return ''
    else:
        first = inStr[0]
        last = inStr[-1]
        return last + strreverse (inStr[1:-1]) + first
        
def ispalindrome (inStr, ignoreSpaces=False, ignoreCase=True):
    if len(inStr) == 1: return True
    else:
        if ignoreSpaces: inStr = inStr.replace(' ', '')
        if ignoreCase: inStr = inStr.lower()
        if inStr[0] != inStr[-1]: return False
        else: return ispalindrome (inStr[1:-1], ignoreSpaces, ignoreCase)

def strpermutations (word):
    if len(word) <=1: 
        return word
    
    # get all strpermutations of length N-1
    result = []
    char = word [0]
    perms = strpermutations (word[1:])
    
    #insert chat at different place in the strpermutations for N-1 to generate strpermutations for N
    for perm in perms:
        for i in range (len(perm)+1):
            result.append (perm[:i] + char + perm[i:])
    
    return result

if __name__ == '__main__':

    print "Sameer", strreverse("Sameer")
    print ''

    print ispalindrome ('madam i m adam')
    print ispalindrome ('madam i m adam', ignoreSpaces=True)
    print ispalindrome ('Madam i m adam', ignoreSpaces=True, ignoreCase=True)
    print ''
    
    perms = strpermutations ('abcd')
    for perm in perms:
        print (perm)



    