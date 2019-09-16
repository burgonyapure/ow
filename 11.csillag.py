print("Adj meg egy számot")
a =int(input())
h = 2*a-2

for x in range(-1,a):
	for y in range(0,h):
		print(end=" ")
	h -= 1
	for y in range(0, x+1):
		print("* ",end="")
	print("\r")

