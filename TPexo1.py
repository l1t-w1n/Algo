
cpt = 0

def binome (n,p) :
    global cpt  
    cpt = cpt + 1
    if p == 0 or n == p :
        return (1)
    else :
        return n/p * binome(n-1,p-1)
            

print(binome(20,10))
print(cpt) 

