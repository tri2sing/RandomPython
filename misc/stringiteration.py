

def findlongestsubstring (inStr, checkStr):
    for size in range (len(inStr), 0, -1):  # generating larger to smaller substrings 
        for itr in range (len(inStr)): # loop to create the substring
            sub =  inStr[itr:itr+size]  
            val = checkStr.find (sub)
            if (val != -1):
                return sub  
    return None
  

if __name__ == '__main__':
  
    print "Hello", "Pillow", " = ", findlongestsubstring("Hello", "Pillow")
    print "Pillow", "Hello", " = ", findlongestsubstring("Pillow", "Hello")
    print "Hi", "Pillow", " = ", findlongestsubstring("Hi", "Pillow")
    print "Sameer", "Nazeem", " = ", findlongestsubstring("Sameer", "Nazeem")
    print "Amazo", "Itel", " = ", findlongestsubstring("Amazo", "Itel")
    print "Sameer", "Sameer", " = ", findlongestsubstring("Sameer", "Sameer")
