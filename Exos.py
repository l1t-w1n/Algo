import itertools as it
from pylab import *
from random import *
from collections import deque
c=0
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
			
def incrnombin(a):
	i=0
	global c
	while i<len(a) and a[i]==1:
		a[i]=0
		i+=1
		c+=1
	if i<len(a):
		a[i]=1
		c+=1
	return a


def inc(l,k):
	for i in range(k):
		incrnombin(l)
	return l

def nbinvmoy(n):
	l=[0]*10
	nbinv=0
	for i in range(n):
		for j in range(len(inc(l,i))):
			if inc(l,i)[j]!=inc(l,i+1)[j]:
				nbinv+=1
	return nbinv/n



def afficherCourbe(maListeDeValeurs):
  plot(array(range(len(maListeDeValeurs))),array(maListeDeValeurs))
  show()

def bancEssai():
	global c
	data=[]
	for i in range(10):
		c=0
		a=[0]*i
		for f in range(2**i):
			incrnombin(a)
		data.append(c/2**i)
	afficherCourbe(data)

def pileVide():
	return []
def estVide(P):
	return not P
def empiler(P,n):
	return P.append(n)
def depiler(p):
	return p.pop()
def sommet(p):
	return p[-1]
def depiler2(p):
	q=deque(p)
	return q.popleft()

def inverse(p):
	res=pileVide()
	save=pileVide()
	if estVide(p):
		return res
	else:
		while not estVide(p):
			e=depiler(p)
			empiler(res,e)
			empiler(save,e)
		while not estVide(save):
			empiler(p,depiler(save))
		return res

def copie(p):
	res=pileVide()
	save=pileVide()
	save2=pileVide()
	if estVide(p):
		return p
	else:
		while not estVide(p):
			e=depiler(p)
			empiler(save,e)
			empiler(save2,e)
		inverse(save)
		while not estVide(save):
			e=depiler(save)
			empiler(res,e)
		while not estVide(save2):
			e=depiler(save2)
			empiler(res,e)
			empiler(p,e)	
		return res

def copieElem(p):
	res=pileVide()
	save=pileVide()
	save2=pileVide()
	save3=pileVide()
	if estVide(p):
		return p
	else:
		while not estVide(p):
			e=depiler(p)
			empiler(save,e)
			empiler(save2,e)
			empiler(save3,e)
		inverse(save)
		inverse(save2)
		while not estVide(save3):
			empiler(res,depiler(save))
			empiler(res,depiler(save2))
			empiler(p,depiler(save3))
		return res
		
def double(p):
	res=pileVide()
	save=pileVide()
	save2=pileVide()
	if estVide(p):
		return p
	else:
		while not estVide(p):
			e=depiler(p)
			empiler(save,e)
			empiler(save2,e)
		inverse(save)
		while not estVide(save):
			e=depiler(save)
			empiler(res,e*2)
			empiler(p,e)	
		return res
k=[1,2,3]
print(double(k))