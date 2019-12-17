m=999
l=0
while m>99:
	n=999
	while n>99:
		a=m*n
		x=a
		p=0
		while x!=0:
			p=(p*10)+x%10
			x=x//10
		if p==a:
			if p>l:
				l=p
		n=n-1
	m=m-1
print(l)
