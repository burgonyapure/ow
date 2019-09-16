print "Ora 1:"
kezdora = input()
print "Perc 1:"
kezdperc = input()
print "Masodperc:"
kezdmp = input()

kezdomp = (kezdora * 3600) + (kezdperc * 60) + kezdmp

print "Ora 2:"
vegora = input()
print "Perc 2:"
vegperc = input()
print "Masodperc:"
vegmp = input()

vegsomp = (vegora * 3600) + (vegperc * 60) + vegmp

print "Eltelt masodpercek: " , vegsomp-kezdomp
