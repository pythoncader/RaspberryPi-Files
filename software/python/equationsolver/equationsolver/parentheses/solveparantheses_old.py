import equationsolver.parantheses.xparanthesessolver as xparanthesessolver
import equationsolver.reused.blankstringremover as blankstringremover
import equationsolver.parantheses.paranthesesmultiplicationdivision as paranthesesmultiplicationdivision
import equationsolver.terms.terms as terms

def parantheses(termslist):
	oldparanthesesterms = []
	oldparanthesesterms.extend(paranthesesterms)
	paranthesesfinallist = []
	paranthesesfinal = ''
	for i in range(0, len(paranthesesterms)):
		newlist = []
		floatparantheses = []
		paranthesesstar = False
		multiplication = False
		division = False
		xinparantheses = False
		paranthesesterms = blankstringremover.remover(paranthesesterms)
		newlist = list(paranthesesterms[i])
		
		if "*" == newlist[0]:
			newlist[0] = newlist[0].replace('*', '', 1)
			paranthesesterms[i] = paranthesesterms[i].replace('*', '', 1)
			paranthesesstar = True

	
		del newlist
		newlist = list(paranthesesterms[i])
		index = newlist.index('(')
		del newlist[index]
		del newlist[len(newlist) - 1]
		paranthesesterms[i] = ''.join(newlist)

		paranthesesterms = blankstringremover.remover(paranthesesterms)
		newlist = list(paranthesesterms[i])
		parantheses = terms.termer(newlist)[0]

		for a in range(0, len(parantheses)):
			if '*' in parantheses[a]:
				multiplication = True
			if '/' in parantheses[a]:
				division = True
			if '(' in parantheses[a]:
				sys.exit('Error - There are parantheses in parantheses')

		for b in range(0, len(parantheses)):
			if 'x' in parantheses[b]:
				print('x is in the parantheses')
				xinparantheses = True
				break
			else:
				xinparantheses = False

		if xinparantheses == False:
			if multiplication == False and division == False:
				for c in range(0, len(parantheses)):
					floatparantheses.append(float(parantheses[c]))
				paranthesesfinal = sum(floatparantheses)
			else:
				paranthesesfinal = paranthesesmultiplicationdivision.solver(parantheses, multiplication, division)
		else:
			paranthesesfinallist, toputonotherside = xparanthesessolver.xparantheses(termslist, paranthesesterms, parantheses, termslist, oldparanthesesterms, paranthesesstar)

		for i in range(0, len(oldparanthesesterms)):	
			if oldparanthesesterms[i] in termslist:
				index = termslist.index(oldparanthesesterms[i])
		if paranthesesstar == True and paranthesesfinal != '':
			termslist[index] = '*' + str(paranthesesfinal)

		elif paranthesesfinallist == []:
			termslist[index] = str(paranthesesfinal)
		else:
			#insert paranthesesfinallist into termslist[index] and delete termslist[index]
			for i in range(0, len(paranthesesfinallist)):
				termslist.insert(index + i, paranthesesfinallist[i])
			numofitems = len(paranthesesfinallist)
			originalspot = index + numofitems
			del termslist[originalspot]

	return termslist, toputonotherside