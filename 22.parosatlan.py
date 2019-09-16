a=int(input("Meddig?"))
paros = 0
paratlan = 0
sumparatlan = 0
for x in range(1,a+1):
	if x % 2 == 0:
		paros = paros + 1
	else:
		paratlan = paratlan + 1
		sumparatlan += x

print("A páros számok darabszáma:",paros,"\nA páratlan számok darabszáma:",paratlan,"\nA páratlan számok összege:",sumparatlan)
