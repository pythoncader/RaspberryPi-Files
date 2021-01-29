import sys

def quotienter(mylist):
	divisionterms = []
	for i in range(0, len(mylist)):
		if '/' in mylist[i]:
			divisionterms.append(mylist[i-1])
			divisionterms.append(mylist[i])
			print('division terms: ', divisionterms)

			newstring = divisionterms[i].replace('/', '')
			divisionterms[i] = newstring
			
			if 'x' not in mylist[i] and 'x' not in mylist[i - 1]:
				first = float(divisionterms[0])
				second = float(divisionterms[1])
				divided = first / second
				print(divided)
		
				mylist[i] = str(divided)
				mylist[i - 1] = ''
				print(mylist)

				divisionterms.clear()
			
			elif 'x' in divisionterms[0] and 'x' not in divisionterms[1]:
				if 'x' != divisionterms[0]: 
					newstring = divisionterms[0].replace('x', '')
					divisionterms[0] = newstring
				elif 'x' == divisionterms[0]:
					newstring = divisionterms[0].replace('x', '1')
					divisionterms[0] = newstring

				first = float(divisionterms[0])
				second = float(divisionterms[1])
				divided = first / second
				print(str(divided) + 'x')
		
				mylist[i] = str(divided) + 'x'
				mylist[i - 1] = ''
				print(mylist)

				divisionterms.clear()
			
			elif 'x' not in divisionterms[0] and 'x' in divisionterms[1]:
				print('hello: ', divisionterms)
				if 'x' != divisionterms[1]: 
					newstring = divisionterms[1].replace('x', '')
					divisionterms[1] = newstring
				elif 'x' == divisionterms[1]:
					newstring = divisionterms[1].replace('x', '1')
					divisionterms[1] = newstring

				first = float(divisionterms[0])
				second = float(divisionterms[1])
				divided = first / second
				print(str(divided) + 'x')
		
				mylist[i] = str(divided) + 'x'
				mylist[i - 1] = ''

				divisionterms.clear()
			
			elif 'x' in divisionterms[0] and 'x' in divisionterms[1]:
				sys.exit('\nThis is not a valid equation (This is a quadratic equation)')


	while '' in mylist:
		mylist.remove('')
	for i in range(0, len(mylist)):
		if '+' not in mylist[i]:
			if '-' not in mylist[i]:
				mylist[i] = '+' + mylist[i]
	print(mylist)
	return mylist