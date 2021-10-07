from math import *
cpt=0

def binome(n,p):
    global cpt
    cpt+=1
    if p==0 or p==n:
        return 1
    else:
        return binome(n-1,p)+binome(n-1,p-1)

def binomeSimp(n,p):
    global cpt
    cpt+=1
    if p==0 or p==n:
        return 1
    else:
        return (p/n)*binomeSimp(n-1,p-1)

def binomeUltraSimp(n,p):
    global cpt
    cpt+=1
    return factorial(n)/(factorial(p)*factorial(n-p))


def nbNb(n):
    global cpt
    cpt+=1
    if n==0:
        return cpt-1
    else:
        n=n//10
        return nbNb(n)


def nbRank(u,o):
    while o > 1:
        u=u//10
        o=o-1
    return u%10

def nbRankRecursive(u,o):
    if u==0:
        return 0
    elif o==1:
        return u%10
    else:
        o=o-1
        u=u//10
        return nbRankRecursive(u,o)




print(nbNb(589987))