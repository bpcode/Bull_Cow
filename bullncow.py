import random

r=['0','0','0','0']
for i in range(4):
	r[i]=str(random.randrange(1,10))
	j=0
	while j<i:
		if r[i]==r[j]:
			j=0
			r[i]=str(random.randrange(1,10))
			continue
		j+=1	
			
f=r[0]+r[1]+r[2]+r[3]

bull=cow=0
#print(r)
n =0 
while n!=f:
	bull=cow=0
	n= input('enter the number: ')
	for i in range(4):
		if n[i]==f[i]:
			bull +=1
		for j in f:
			if j==n[i]:
				cow +=1
	print ('Bull: ',bull, '  Cow: ',cow-bull)

print("you are right this time") 
