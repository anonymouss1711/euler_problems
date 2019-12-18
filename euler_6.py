i=1
tot=0
sums=0
while i<=100:
	tot=tot+i
	sums=sums+(i*i)
	i=i+1
sum=tot*tot
print(sum-sums)
