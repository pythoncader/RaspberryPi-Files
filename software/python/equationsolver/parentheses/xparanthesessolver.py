import equationsolver.parantheses.paranthesesmultiplicationdivision as paranthesesmultiplicationdivision
import equationsolver.signsolvers.multiplication as multiplication
def xparantheses(termslist, paranthesesterms, parantheses, firsthalftermslist, oldparanthesesterms, paranthesesstar):
	xmultiply = False
	xdivide = False
	xaddorsubtract = False
	multiplicationlist = []
	paranthesesfinallist = []
	toputonotherside = []

	print(parantheses, 'line 12 in xparanthesessolver')
	for i in range(0, len(oldparanthesesterms)):
		if oldparanthesesterms[i] in termslist:
			index = termslist.index(oldparanthesesterms[i])
			break

	for i in range(0, len(parantheses)):
		if 'x' in parantheses[i]:
			if '*' in parantheses[i]:
				xmultiply = True
			elif '/' in parantheses[i]:
				xdivide = True
			elif '+' in parantheses[i] or '-' in parantheses[i]:
				xaddorsubtract = True
			elif '*' in parantheses[i+1]:
				xmultiply = True
			elif '/' in parantheses[i+1]:
				xdivide = True
			elif '+' in parantheses[i+1] or '-' in parantheses[i]:
				xaddorsubtract = True
			
	if xmultiply == True:
		paranthesesfinallist = paranthesesmultiplicationdivision.solver(parantheses, xmultiply, xdivide, True)
		print('line 35 in xparanthesessolver', paranthesesfinallist)

	elif xaddorsubtract == True: #if x is being added to something in the parantheses
		print('line 37 in xparanthesessolver: ', xaddorsubtract)
		if paranthesesstar == True: #if something is multiplying the parantheses from the front
			if index != 0: #if the parantheses are not the first thing in the termslist
				multiplier = index - 1
				print('line 42 in xparanthesessolver', termslist[multiplier])
				for a in range(0, len(parantheses)): #use distributive property
					multiplicationlist.append(termslist[multiplier])
					multiplicationlist.append('*' + parantheses[a])
					print('line 46: in xparanthesessolver', multiplicationlist)
					newlist = multiplication.producter(multiplicationlist)
					paranthesesfinallist.append(newlist[0])
					print('line 49 in xparanthesessolver', paranthesesfinallist)
					multiplicationlist.clear()
				del termslist[multiplier] #delete the multiplier
							
		if "/" == oldparanthesesterms[0]: #if the parantheses are the denominator of the fraction
			print('The parantheses are being divided')
			
		else:
			print('line 56 in xparanthesessolver', paranthesesfinallist)

		if len(termslist) > index:
			if '/' in termslist[index + 1]: #if the parantheses are the numerator of the fraction
				termslist[index + 1] = termslist[index + 1].replace('/', '', 1)
				print('The parantheses,', termslist[index], ', are being divided by', termslist[index + 1])
				toputonotherside.append('*' + termslist[index + 1])
				del termslist[index]
	return paranthesesfinallist, toputonotherside