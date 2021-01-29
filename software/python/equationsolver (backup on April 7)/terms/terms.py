import parantheses.solveparantheses as solveparantheses
import reused.blankstringremover as blankstringremover
import terms.signremover as signremover
import reused.font as font

def termer(equationhalflist):
	#this method gets half of the equation as separate strings in a list and puts them into terms.
	openingparantheses = 0
	termslist = []
	paranthesesterms = []
	parantheses = []
	termsstring = ''
	toputonotherside = []
	#add all of the items in equationhalflist to a new list* split into terms *termslist
	#also add the signs to each of the terms
	for i in range(0, len(equationhalflist)): #loop through the list
		if equationhalflist[i] != '(' and openingparantheses == 0: #if there haven't been opening parantheses and this isn't the start of parantheses.
			if termsstring == '()':
				termsstring = ''

			#if the character is a plus sign, and it's not in parantheses, then add the current term to the list, and start a new term.	
			if equationhalflist[i] == "+" and openingparantheses == 0: 
				if equationhalflist[i-1] == "/" or equationhalflist[i-1] == "*":
					pass
				else:
					termslist.append(termsstring)
					termsstring = "+"
					continue

			#if the character is a minus sign, then add the current term to the list and start a new term.
			if equationhalflist[i] == "-" and openingparantheses == 0: 
				if equationhalflist[i-1] == "/" or equationhalflist[i-1] == "*":
					pass
				else:
					termslist.append(termsstring)
					termsstring = "-"
					continue

			#if the character is a multiplication sign, then add the current term to the list and start a new term.
			if equationhalflist[i] == "*" and openingparantheses == 0:
				termslist.append(termsstring)
				termsstring = "*"
				continue

			#if the character is a division sign, then add the current term to the list and start a new term.
			if equationhalflist[i] == "/" and openingparantheses == 0:
				termslist.append(termsstring)
				termsstring = "/"
				continue
				
			#if there haven't been any parantheses, add the current character to the termsstring.	
			if openingparantheses == 0:
				termsstring = termsstring + equationhalflist[i]


		#if the current character is the start of parantheses
		elif equationhalflist[i] == '(':
			#if the current character is not a () (which means that a parantheses just ended), and it's not a math sign, add it to the list
			if termsstring != '()' and termsstring != '+' and termsstring != '*' and termsstring != '/' and termsstring != '-':
				termslist.append(termsstring) #this means that the parantheses will either be multiplied by a number or it is the first thing in the list

			#if the current character is a minus sign, then we want to replace it with a -1 multiplied by the parantheses
			elif termsstring == '-':
				termsstring = '-1'
				termslist.append(termsstring)

			#if there is a current term, remove the signs from it
			if termsstring != '':
				mynewstring = signremover.remover(termsstring)
				if len(mynewstring) != 0:
					#if the character or term before a parantheses is a number, closing parantheses, or x, then multiply it
					if mynewstring.isdigit() or mynewstring[-1] == ')' or "x" in mynewstring:
						termsstring = '*'
						
			openingparantheses += 1 #tell the program that there is one more opened parantheses

		if openingparantheses > 0 and equationhalflist[i] != ')': #if this is not the first opened parantheses, and it isn't the closing parantheses, then just add the character to the term.
			termsstring = termsstring + equationhalflist[i]

		#if this is the closing parantheses, finish the term, and add it to the list.
		elif equationhalflist[i] == ')':
			openingparantheses = openingparantheses - 1
			termsstring = termsstring + equationhalflist[i]
			paranthesesterms.append(termsstring)
			termslist.append(termsstring)
			termsstring = '()'

	#if the character is not an ended parantheses, add the term to the list.
	if termsstring != '()':
		termslist.append(termsstring)
	else:
		termsstring = ''

	#remove un-needed strings in termslist
	termslist = blankstringremover.remover(termslist)
	
	#solve the parantheses
	if paranthesesterms != []:
		termslist, toputonotherside = solveparantheses.parantheses(paranthesesterms, parantheses, termslist)
		print('in terms:', termslist, toputonotherside)

	return termslist, toputonotherside