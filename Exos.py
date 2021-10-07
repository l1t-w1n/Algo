c=0
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

	