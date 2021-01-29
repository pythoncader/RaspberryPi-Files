import equationsolver.parentheses.solveparentheses as solveparentheses
import equationsolver.reused.blankstringremover as blankstringremover
import equationsolver.terms.signremover as signremover


def isdigitatend(mystring):
	if mystring != '':
		if '0' == mystring[-1]:
			return True
		elif '1' in mystring[-1]:
			return True
		elif '2' in mystring[-1]:
			return True
		elif '3' in mystring[-1]:
			return True
		elif '4' in mystring[-1]:
			return True
		elif '5' in mystring[-1]:
			return True
		elif '6' in mystring[-1]:
			return True
		elif '7' in mystring[-1]:
			return True
		elif '8' in mystring[-1]:
			return True
		elif '9' in mystring[-1]:
			return True
		else:
			return False
	else:
		return False

def termer(equationhalflist, innerparenthesescall = False):
	openingparentheses = 0
	halftermslist = []
	termsstring = ''
	toputonotherside = []
	mynewstring = ''
	#add all of the items in equationhalflist to a new list* split into terms *termslist
	#also add the signs to each of the terms
	for i in range(0, len(equationhalflist)):
		wasclosingparentheses = False
		if termsstring == 'parentheses' and equationhalflist[i].isdigit():
			termsstring = '*' + equationhalflist[i]
			wasclosingparentheses = True
			continue

		elif termsstring == 'parentheses':
			termsstring = ''
			wasclosingparentheses = True

		if equationhalflist[i] != '':
			if wasclosingparentheses == True and equationhalflist[i] != "(" and equationhalflist[i] != "/" and equationhalflist[i] != "*" and equationhalflist[i] != "+":
				termsstring = termsstring + "*"
				continue

			elif wasclosingparentheses == True and equationhalflist[i] == "(":
				termsstring = termsstring + "*("
				openingparentheses += 1
				continue
				


		if equationhalflist[i] != '(' and openingparentheses == 0: #if the part of the equation is not opening parentheses and there hasn't been opening parentheses
			if equationhalflist[i] == "+" and openingparentheses == 0: #if the character is a plus and it's not in parentheses
				halftermslist.append(termsstring) #add the current termsstring, then add the sign to the next termsstring
				termsstring = "+"
				continue
			if equationhalflist[i] == "-" and openingparentheses == 0: #if the character is a minus and it's not in parentheses
				halftermslist.append(termsstring) #add the current termsstring, then add the sign to the next termsstring
				termsstring = "-"
				continue
			if equationhalflist[i] == "*" and openingparentheses == 0: #if the character is a multiplication and it's not in parentheses
				halftermslist.append(termsstring) #add the current termsstring, then add the sign to the next termsstring
				termsstring = "*"
				continue
			if equationhalflist[i] == "/" and openingparentheses == 0: #if the character is a division and it's not in parentheses
				halftermslist.append(termsstring) #add the current termsstring, then add the sign to the next termsstring
				termsstring = "/"
				continue
	
			if openingparentheses == 0: #if it is a number or x, then just add it to the termsstring
				termsstring = termsstring + equationhalflist[i]

		elif equationhalflist[i] == '(' and openingparentheses == 0: #if it is a starting parentheses and there hasn't been one already started it
			openingparentheses += 1 #say that there is an opened parentheses. this kind of skips everything else and gives the whole parentheses term to the parentheses solver.
			if termsstring != 'parentheses' and termsstring != '+' and termsstring != '*' and termsstring != '/' and termsstring != '-' and isdigitatend(termsstring) != True:
				halftermslist.append(termsstring) #if the termsstring isn't a sign (besides "-")
				termsstring = equationhalflist[i]
				continue
			elif termsstring == '-':
				termsstring = '-1' #change the - sign outside the parentheses to a -1
				halftermslist.append(termsstring)
				termsstring = '*' + equationhalflist[i]
				continue

			if termsstring != '': #this adds a "*" sign to parentheses-term if there is something multiplied by it
				mynewstring = signremover.remover(termsstring) #this simply lets us check whether it is a digit (without a sign)
				if len(mynewstring) != 0:
					if mynewstring.isdigit() or mynewstring[len(mynewstring)-1] == ')' or "x" in mynewstring:
						halftermslist.append(termsstring)
						termsstring = '*' + equationhalflist[i]
						mynewstring = ''
						continue
			if mynewstring == '':
				termsstring += equationhalflist[i]
				continue
						

		elif equationhalflist[i] == '(' and openingparentheses > 0:
			termsstring = termsstring + equationhalflist[i]
			openingparentheses += 1 #say that there is an opened parentheses. this kind of skips everything else and gives the whole parentheses term to the parentheses solver.

		elif openingparentheses > 0 and equationhalflist[i] != ')': #if there is an opened parentheses and this character is not a closing parentheses sign
			termsstring = termsstring + equationhalflist[i]

		elif openingparentheses == 1 and equationhalflist[i] == ')': #if there is a closing parentheses sign after parentheses have been opened
			openingparentheses = openingparentheses - 1 #close one of the paranthese(s)
			termsstring = termsstring + equationhalflist[i] #add the closing parentheses to the termsstring, then add it.
			halftermslist.append(termsstring)
			termsstring = 'parentheses'

		elif openingparentheses > 1 and equationhalflist[i] == ')':
			openingparentheses = openingparentheses -1
			termsstring = termsstring +equationhalflist[i]

	if termsstring != 'parentheses':
		halftermslist.append(termsstring)
	else:
		termsstring = ''

	#remove un-needed strings in termslist
	halftermslist = blankstringremover.remover(halftermslist)
	if innerparenthesescall == False:
		for i in halftermslist:
			if '(' in i:
				#print(f'\nline 139 in terms: {halftermslist}')
				halftermslist = solveparentheses.parentheses(halftermslist)

	return halftermslist