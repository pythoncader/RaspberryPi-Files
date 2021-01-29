import reused.font as font
import terms.signremover as signremover

def quotienter(mylist):
	divisionterms = []

	for i in range(0, len(mylist)): #loop through the terms
		if '/' in mylist[i]: #if there are any division signs in the term
			divisionterms.append(mylist[i-1]) #add the term before it and the term to the division terms
			divisionterms.append(mylist[i])
			print("line 11 in division", divisionterms)
			newstring = divisionterms[1].replace('/', '') #get rid of the division sign in the term
			divisionterms[1] = newstring
			positive = "UNKNOWN"
			if "+" in divisionterms[0] and "-" not in divisionterms[1]:
				positive = True
				divisionterms[0] = signremover.remover(divisionterms[0])
			elif "-" in divisionterms[0] and "-" not in divisionterms[1]:
				positive = False
				divisionterms[0] = signremover.remover(divisionterms[0])
			elif "-" in divisionterms[0] and "-" in divisionterms[1]:
				positive = True
				divisionterms[0] = signremover.remover(divisionterms[0])
				divisionterms[1] =  signremover.remover(divisionterms[1])

			if 'x' not in mylist[i] and 'x' not in mylist[i - 1]: #if there is no x in either term
				first = float(divisionterms[0])
				second = float(divisionterms[1])
				divided = first / second #divide the two terms
		
				if positive != True:
					mylist[i] = "-" + str(divided)
				else:
					mylist[i] = str(divided) #add the newly divided term to the correct place in the equation.
				mylist[i - 1] = '' #delete the other term that we don't need any more

				divisionterms.clear() #clear the division terms list for further use
			
			elif 'x' in divisionterms[0] and 'x' not in divisionterms[1]: #otherwise, if x is in the first term
				if 'x' != divisionterms[0]: #if x is not the only thing being divided
					newstring = divisionterms[0].replace('x', '')
					divisionterms[0] = newstring #get rid of the x in the term
				elif 'x' == divisionterms[0]: #if x is the only thing in the term
					newstring = divisionterms[0].replace('x', '1')
					divisionterms[0] = newstring #replace the term with 1

				first = float(divisionterms[0])
				second = float(divisionterms[1])
				divided = first / second #divide the two terms
		
				if positive != True:
					mylist[i] = "-" + str(divided) + 'x'
				else:
					mylist[i] = str(divided) + 'x'
				mylist[i-1] = ''

				divisionterms.clear()
			
			elif 'x' not in divisionterms[0] and 'x' in divisionterms[1]:
				if 'x' != divisionterms[1]: 
					newstring = divisionterms[1].replace('x', '')
					divisionterms[1] = newstring
				elif 'x' == divisionterms[1]:
					newstring = divisionterms[1].replace('x', '1')
					divisionterms[1] = newstring

				first = float(divisionterms[0])
				second = float(divisionterms[1])
				divided = first / second
				if positive != True:
					mylist[i] = "-" + str(divided) + 'x'
				else:
					mylist[i] = str(divided) + 'x'

				mylist[i - 1] = ''

				divisionterms.clear()
			
			elif 'x' in divisionterms[0] and 'x' in divisionterms[1]:
				divisionterms[0] = divisionterms[0].replace('x', '')
				divisionterms[1] = divisionterms[1].replace('x', '')
				first = float(divisionterms[0])
				second = float(divisionterms[1])
				divided = first / second
				if positive != True:
					mylist[i] = "-" + str(divided)
				else:
					mylist[i] = str(divided)

				mylist[i - 1] = ''

				divisionterms.clear()


	while '' in mylist:
		mylist.remove('')
	for i in range(0, len(mylist)):
		if '+' not in mylist[i]:
			if '-' not in mylist[i]:
				mylist[i] = '+' + mylist[i]

	return mylist