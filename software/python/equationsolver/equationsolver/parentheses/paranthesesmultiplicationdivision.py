import equationsolver.signsolvers.multiplication as m1

def solver(parantheses, multiplication, division, xtrue = False):
	if multiplication == True and division == False:
		print('There is multiplication in the parantheses')
		parantheses = m1.producter(parantheses)
		print(parantheses)
		

	elif division == True and multiplication == False:
		print('There is division in the parantheses')

	elif multiplication == True and division == True:
		print('There is multiplication and division in the parantheses')

	if xtrue == False:
		paranthesesfinal = float(parantheses[0])
	elif xtrue == True:
		paranthesesfinal = parantheses[0]
	return paranthesesfinal