import itertools as it
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
			

print(naif([1,-1,5]))


	