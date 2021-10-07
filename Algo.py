import math as m
c=0

###Exercice 1###
def binome (a,b):
    global c
    c+=1
    if b==0 or b==a:
        return 1
    else:
        return (a/b)*binome(a-1,b-1)

###Exercice 2###
def nbchif (a):
    global c
    c+=1
    if a<10:
        return 1
    else: 
        return nbchif(a//10)+1
def somchif (a):
    global c
    c+=1
    if a<10:
        return a
    else:
        return a%10+somchif(a//10)
def racnum(a):
    global c
    c+=1
    if a<10:
        return a
    else:
        return racnum(somchif(a))

###Exercice 3###
def syracuse(n):
	global c
	c+=1
	if n==1:
		return 
	elif n%2==0:
		n=n/2
		print(n)
		return syracuse(n)
	else:
		n=3*n+1
		print(n)
		return syracuse(n)
while True:
	n=int(input("eneter n "))
	syracuse(n)
	print(c)
	c=0

###Exercice 4###
def recherche(l,x):
    global c
    for i in l:
        c+=1
        if i==x:
            return True, c
        else:
            return False,c			
def rechdic(l, x):
    global c
    c+=1
    mid=int(len(l)/2)
    if x==l[mid]:
    	return True, c
    elif len(l)==1:
    	return l[0]==x, c
    elif x>l[mid]:
    	return rechdic(l[mid:],x)
    else:
    	return rechdic(l[:mid],x)