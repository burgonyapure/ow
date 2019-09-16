a = int(input("Adj egy számot: "))
b = 1
if a<0:
	print("Ne negatívat pls")
elif a==0:
	print("0 faktorialisa = 1")
else:
	for x in range(1,a+1):
		b = b * x
print("A(z)",a,"szám fatoriálisa:",b)
