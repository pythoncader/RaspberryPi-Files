import parantheses.xparanthesessolver as xparanthesessolver
import reused.blankstringremover as blankstringremover
import reused.font as font
import parantheses.paranthesesmultiplicationdivision as paranthesesmultiplicationdivision
import terms.terms as terms
def parantheses(paranthesesterms, parantheses, termslist):
	toputonotherside = []
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
		print("line 36 in parantheses", newlist)
		parantheses = terms.termer(newlist)[0]
		print("line 38 in  parantheses", parantheses)

		for a in range(0, len(parantheses)):
			if '*' in parantheses[a]:
				multiplication = True
			if '/' in parantheses[a]:
				division = True
			if '(' in parantheses[a]:
				print(font.textcolors.warning, 'Error - There are parantheses in parantheses')

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
				print("line 61 in parantheses", paranthesesfinal)
			else:
				print("line 63 in parantheses", parantheses)
				paranthesesfinal = paranthesesmultiplicationdivision.solver(parantheses, multiplication, division)
		else:
			paranthesesfinallist, toputonotherside = xparanthesessolver.xparantheses(termslist, paranthesesterms, parantheses, termslist, oldparanthesesterms, paranthesesstar)
			print(font.textcolors.okgreen, 'line 67 in solveparantheses', paranthesesfinallist)
			print(toputonotherside, 'line 68 in solveparantheses')

		for i in range(0, len(oldparanthesesterms)):	
			if oldparanthesesterms[i] in termslist:
				index = termslist.index(oldparanthesesterms[i])
				print('line 72 in solveparantheses', termslist[index])
		if paranthesesstar == True and paranthesesfinal != '':
			termslist[index] = '*' + str(paranthesesfinal)

		elif paranthesesfinallist == []:
			termslist[index] = str(paranthesesfinal)
			print('line 77 in solveparantheses', termslist)
		else:
			#insert paranthesesfinallist into termslist[index] and delete termslist[index]
			print(font.textcolors.endc, "line 82 in parantheses", paranthesesfinallist)
			for i in range(0, len(paranthesesfinallist)):
				termslist.insert(index + i, paranthesesfinallist[i])
				print('line 83 in solveparantheses', termslist)
			numofitems = len(paranthesesfinallist)
			originalspot = index + numofitems
			print('line 86 in solveparantheses', termslist[originalspot])
			del termslist[originalspot]

	print(font.textcolors.fail, 'termslist: ', termslist)
	print(font.textcolors.endc, 'toputonotherside', toputonotherside)
	return termslist, toputonotherside