from pylab import *

def afficherCourbe(maListeDeValeurs):
    plot(array(range(len(maListeDeValeurs))),array(maListeDeValeurs))
    show()
import random
#1

def recherche(l,x):
    c=[]
    for i in range(len(l)) :
        if l[i] ==x:
            c.append(i)
            afficherCourbe(c)
            return True, c
        



#2
c=[]
def rechdic(l, x):
    global c
    mid=int(len(l)/2)
    c.append(mid)
    if x==l[mid]:
    	return True, #afficherCourbe(c)
    elif len(l)==1 and l[0]==x:
    	return True, #afficherCourbe(c)
    elif len(l)==1 and l[0]!=x:
    	return False, #afficherCourbe(c)
    elif x>l[mid]:
    	return rechdic(l[mid:],x)
    else:
    	return rechdic(l[:mid],x)
r = random.sample(range(10000), 10000)
print (recherche(r,3445))
print (rechdic(r, 3445))