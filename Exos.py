import itertools as it
from pylab import *
from random import *
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

bancEssai()