def termer(termslist):

	xterms = []
	constantterms = []

	#add all of the x-terms in the termslist to a new list called xterms 

	for i in range(0, len(termslist)): #loop through the equation
		if 'x' in termslist[i]: #if x is the current character, add it to the xterms list.
			xterms.append(termslist[i])
		elif 'x' not in termslist[i]: #otherwise, add it to the constant terms list
			constantterms.append(termslist[i])

	#xterms = [i for i in termslist if 'x' in i]
	if xterms != [] and constantterms != []: #if both lists are not empty
		if '-' in xterms[0]: #if the current string is a minus sign
			if '-' in constantterms[0]: 
				return xterms, constantterms
		elif '+' not in xterms[0]:
			xterms[0] = '+' + xterms[0]

	if constantterms != []:
		if '-' in constantterms[0]:
			return xterms, constantterms
		elif '+' not in constantterms[0]:
			constantterms[0] = '+' + constantterms[0]

	return xterms, constantterms