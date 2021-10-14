import math as m
import itertools as it
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

###Exercice 5###
def naif(t):
    som=0
    i=sum([list(map(list, it.combinations(t, i))) for i in range(len(t) + 1)], [])
    for el in i:
    	s1=0
    	for n in el:
    		s1+=n
    	if s1>som:
    		som=s1
    return som
def naif2(t):
	max=t[0]
	d, f, iter=0,0,0
	for i in range(len(t)):
		s=0
		for n in range(i, len(t)):
			s+=t[n]
			iter+=1
			if s>max:
				max=s
				d=i
				f=n
	return max, iter
def kadane(t):
    best_sum = 0
    current_sum = 0
    iter=0
    for x in t:
    	iter+=1
    	current_sum = max(0, current_sum + x)
    	best_sum = max(best_sum, current_sum)
    return best_sum, iter