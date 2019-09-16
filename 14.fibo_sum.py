a = 0
b = 1
d = 0
n = int(input("Add meg az első n-db fibonacci számot amit összeadjak: "))
print("Fibonacci számok",n,"-ig: ")
print("1 :",b)
for x in range(2,n+1):
	c = a+b
	a = b
	b = c
	d += b
	print(x,":",b)
print("Összegük:",d+1)
