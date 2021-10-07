def nbChifDec (n):
    if n < 10 :
        return (1)
    
    else :
        return nbChifDec(n//10)+1

print (nbChifDec(3249))