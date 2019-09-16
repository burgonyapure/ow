class Ido:
	def __init__(self, ora, perc, masodperc):
		self.ora = ora
		self.perc = perc
		self.masodperc = masodperc

print "Add meg a kezdo orat,percet, masodpercet!"
kezdo = Ido(input("Ora: "),input("Perc: "),input("Masodperc: "))

print "Add meg a vegzodo orat, percet, masodpercet!"
vegzo = Ido(input("Ora: "),input("Perc: "),input("Masodperc: "))

eredmeny = ((vegzo.ora * 3600) + (vegzo.perc * 60) + vegzo.masodperc) - ((kezdo.ora * 3600) + (kezdo.perc * 60) + kezdo.masodperc)
print "A megadott idointervallum kozott eltelt" ,eredmeny,"masodperc!"
