# Exo 1
from math import sqrt
#1

# Si n=0, l'algorithme r'envoie 0, sinon l'algorithme multiplie n par n et rappelle la fonction avec n-1, jusqu'à que n=1 (c'est une sorte de factoriel)
#

#2

def somme(n):
    if n==0:
        return 0
    else:
        return n+somme(n-1)

print(somme(5))

#3

def somme2(a,b):
    if a==b:
        return b
    
    return a+somme2(a+1,b)

print(somme2(2,6))

#4

def carre(n):
    if n==0:
        return 0
    else:
        return n+n-1+carre(n-1)

print(carre(5))

#5

def estPair(n):
    if n==1:
        return False
    elif n==0:
        return True
    else:
        return estPair(n-2)
print(estPair(0))

#6

def sommeImpair(n):
    if n==0:
        return None
    if n%2==0:
        return sommeImpair(n-1)
    elif n==1:
        return 1
    else:
        return n+sommeImpair(n-2)

print(sommeImpair(7))

#7.1

def PPD(a,b):
    if b==0 or a>b:
        return None
    elif b%a==0:
        return a
    else:
        return PPD(a+1,b)

#7.2

def estPremier(n):
    if n==1:
        return None
    elif PPD(2,n)==n:
        return True
    else:
        return False
print(estPremier(11))

# EXO 2

#1
def somme5(n):
    if n==0:
        return 0
    else:
        return n**5 + (somme5(n-1))
    

#2
def Catalan(n):
    if n==0:
        return 1
    else:
        somme=0
        for i in range(n):
            somme=somme+Catalan(i)*Catalan(n-1-i)
        return somme

print(Catalan(9))


#3
def récu(n):
    if n==0:
        return 5
    else:
        return sqrt(1+récu(n-1))
print(récu(500))

#4
somme=0
def sommeC(u,v):
    global somme
    if u==0 and v==0:
        return 0
    elif u==0:
        return 1+sommeC(u,v-1)
    else:
        return 1+sommeC(u-1,v)

def sommeCm(u,v):
    if u==0:
        return v
    else:
        return sommeCm(u-1,v+1)
print(sommeCm(12,0))





