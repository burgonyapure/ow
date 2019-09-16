a = int(input("Add meg a keret magasságát: "))
b = int(input("Add meg a keret szélességét: "))
c = input("Adj egy karaktert amivel rajzolok: ")

print(c * b)
for x in range(1, a - 1):
	print(c," " * (b - 2),c, sep="")
print(c * b)

