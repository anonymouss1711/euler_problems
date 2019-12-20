def prime(n):
	i=2
	while i<=n//2:
		if n%i==0:
			return 0
		i=i+1
	return 1

n=2
sum=0
while n<=2000000:
	x=prime(n)
	if x==1:
		sum=sum+n
	n=n+1
