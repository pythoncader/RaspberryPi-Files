def termer(termslist):

	xterms = []
	constantterms = []

	#add all of the x-terms in the termslist to a new list called xterms 
	endoflist = len(termslist)
	for i in range(0, endoflist):
		if 'x' in termslist[i]:
			xterms.append(termslist[i])
		elif 'x' not in termslist[i]:
			constantterms.append(termslist[i])

	#xterms = [i for i in termslist if 'x' in i]
	if xterms != [] and constantterms != []:
		if '-' in xterms[0]:
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