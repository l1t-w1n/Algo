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



def afficherCourbe(maListeDeValeurs,name):
  plot(array(range(len(maListeDeValeurs))),array(maListeDeValeurs),label=name)

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

def tri_ins(t):
	for k in range(1,len(t)):
		temp=t[k]
		j=k
		while j>0 and temp<t[j-1]:
			t[j]=t[j-1]
			j-=1
		t[j]=temp
	return t


def triinsertion(L):
	def dichot(L,i,j,X):
		while i!=j:
			k=(i+j)//2
			if X<=L[k]:
				j=k
			else:
				i=k+1
		return i
	for i in range(1,len(L)):
		if L[i]<L[i-1]:
			k=dichot(L,0,i-1,L[i])
			X=L.pop(i)
			L.insert(k,X)
	return L

def tribulle(l):
	for i in range(len(l),0,-1):
		for j in range(i-1):
			if l[j+1]<l[j]:
				l[j+1],l[j]=l[j],l[j+1]
	return l

def tri_selection(tab):
   for i in range(len(tab)):
       min = i
       for j in range(i+1, len(tab)):
           if tab[min] > tab[j]:
               min = j                
       tab[i],tab[min]=tab[min],tab[i]
   return tab


def fusion(left,right):
	res = []
	index_left, index_right = 0, 0
	while index_left < len(left) and index_right < len(right):        
		if left[index_left] <= right[index_right]:
			res.append(left[index_left])
			index_left += 1
		else:
			res.append(right[index_right])
			index_right += 1
	if left:
		res.extend(left[index_left:])
	if right:
		res.extend(right[index_right:])
	return res
     
def tri_fusion(m):
    if len(m) <= 1:
        return m
    mid = len(m) // 2
    left = m[:mid]
    right = m[mid:]
    left = tri_fusion(left)
    right = tri_fusion(right)
    return list(fusion(left, right))

k=[1,2,3,5,1,2,8,53,84,12,35,8,7]
def tempsMoyen(fonction,liste,nbRep=50):
	start=time.time()
	for i in range(nbRep):
		shuffle(liste)
		fonction(liste)
	end=time.time()
	return (end-start)/nbRep

def bancEssai():
	n=900
	data1,data2,data3,data4,data5=[],[],[],[],[]
	for i in range(2,n+1):
		liste=[randint(1,n) for _ in range(i)]
		data1.append(tempsMoyen(tri_ins,liste))
		data2.append(tempsMoyen(triinsertion,liste))
		data3.append(tempsMoyen(tribulle,liste))
		data4.append(tempsMoyen(tri_selection,liste))
		data5.append(tempsMoyen(tri_fusion,liste))
	afficherCourbe(data1,"tri seq")
	afficherCourbe(data2, "tri dich")
	afficherCourbe(data2, "tri bulle")
	afficherCourbe(data2, "tri selection")
	afficherCourbe(data2, "tri fusion")
	legend(loc='upper right')
	show()

bancEssai()
#print(triinsertion(k))