a=1
flag=0
while a<=1000//3 and flag==0:
	b=a+1
	while b<=1000//2 and flag==0:
		c=1000-a-b
		if a*a + b*b == c*c:
			flag=1
			break
		b=b+1
	if flag==1:
		break
	a=a+1
print(a*b*c)