from random import *
from pylab import *


def afficherCourbe(maListeDeValeurs):
    plot(array(range(len(maListeDeValeurs))),array(maListeDeValeurs))
    show()


# Exercice 3 #

#def syracuse(n):
#    print(n)
#    if n==1:
#        return 1
#    if n%2==0:
#        return syracuse(n/2)
#    else:
#        return syracuse(3*n+1)
#print(syracuse(4))

#def syracuse2(n):
#    boucle=True
#    while n>1 or boucle==True:
#        print(n)
#        if n%2==0:
#            n=n/2
#        else:
#            n=3*n+1
#        if n==1:
#            n=int(input("une nouvelle valeur ?\n"))
#        if n==1:
#            boucle=False
#    print(1)
#print(syracuse2(4))
#
## Exercice 4 #
#
#def rech_seq(liste,n):
#    cpt=[]
#    for i in range(len(liste)):
#        if liste[i]==n:
#            cpt.append(i)
#            #afficherCourbe(cpt)
#            return True
#        cpt.append(i)
#
#    return False
#
#l=[randint(0,100) for i in range(1000)]
#l2=[1,3,4,5,1,3,4,5,1,3,4,5,1,3,4,5,1,3,4,5,1,3,4,5,1,3,4,5,1,3,4,5,1,3,4,5,1,3,4,5,7]
#print(rech_seq(l,7))
#
#cpt=[]
#def rech_dic(liste,n):
#    global cpt
#    mid=int(len(liste)/2)
#    cpt.append(mid)
#    if n==liste[mid]:
#    	return True,afficherCourbe(cpt)
#    elif len(liste)==1 and liste[0]==n:
#    	return True,afficherCourbe(cpt)
#    elif len(liste)==1 and liste[0]!=n:
#    	return False,afficherCourbe(cpt)
#    elif n>liste[mid]:
#    	return rech_dic(liste[mid:],n)
#    else:
#    	return rech_dic(liste[:mid],n)
#    
#print(rech_dic(l,7))
#    
#

# EXERCICE 5


def sous_l(l,i,j):
    r = 0
    for a in range(i,j):
        r += l[a]
    
    return r

def max_naive(l):
    meilleur=min(l)
    imin,jmin = -1,-1
    cpt=0
    for i in range(0,len(l)):
        for j in range(i+1,len(l)+1):
            s = sous_l(l,i,j)
            cpt+=1
            if s > meilleur:
                meilleur = s
                imin,jmin = i,j
            
    return meilleur,l[imin:jmin],cpt

cpt=0

def max_crossingSom(l):
    global cpt
    mid=int(len(l)/2)
    som1=l[mid-1]
    max1=som1
    som2=l[mid]
    max2=som2
    for i in range(mid-2,-1,-1):
        som1 += l[i]
        max1=max(max1,som1)
        cpt+=1
    for i in range(mid+1,len(l)):
        som2 += l[i]
        max2=max(max2,som2)
        cpt+=1
    return max1+max2









def max_divisetoconque(liste):
    global cpt
    cpt+=1
    if len(liste)==1:
        return liste[0]
    else:
        return max(max_divisetoconque(liste[:len(liste)//2]),max_divisetoconque(liste[len(liste)//2:]),max_crossingSom(liste))

def bancEssai():
  data=[]
  for i in range(1,100):
    liste=[randint(0,1000) for _ in range(i)]
    #liste.sort() # dans le cas de la recherche dichotomique
    meilleur,mb=max_divisetoconque(liste,cpt)
    data.append(mb)
  afficherCourbe(data)




l = [5,31,-41,59,26,-53,58,97,-93,-23,84,35,-98,-80,-72,-85]
l2 = [2,-349,4,4,8,5,3,-34,5,8]

print(max_divisetoconque(l),cpt)
print(bancEssai())


