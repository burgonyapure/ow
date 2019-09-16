t = int(input("add meg az évet"))

a=t%19
b=t%4
c=t%7
d=(19 * a + 24) % 30
e=(2 * b + 4 * c + 6 * d + 5) % 7

h=22 + d + e

if e == 6 and d == 29:
	h=50
	print("Április",h-31,"-ik napja húsvét vasárnap")
elif e == 6 and d == 28 and a > 10:
	h=49
	print("Április",h-31,"-ik napja húsvét vasárnap")
elif h <= 31:
	print("Március",h,"-ik napja húsvét vasárnap")
else:
	print("Április",h-31,"-ik napja húsvét vasárnap")
