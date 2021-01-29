def combiner(xsidelist, constantsidelist):
	floatxsidelist = []
	floatconstantsidelist = []

	while '' in xsidelist:
		xsidelist.remove('')

	for i in range(0, len(xsidelist)):
		newstring = xsidelist[i].replace('x', ' ')
		xsidelist[i] = newstring
		if '+ ' in xsidelist[i]:
			newstring = xsidelist[i].replace('+ ', '1')
			xsidelist[i] = newstring
		elif '- ' in xsidelist[i]:
			newstring = xsidelist[i].replace('- ', ' -1')
			xsidelist[i] = newstring
		floatxsidelist.append(float(xsidelist[i]))


	for i in constantsidelist:
		floatconstantsidelist.append(float(i))


	print('Final equation: '+str(sum(floatconstantsidelist))+ ' = '+str(sum(floatxsidelist)) + 'x')
	xsidefinal = sum(floatxsidelist)
	constantsidefinal = sum(floatconstantsidelist)
	if xsidefinal != 0:
		answer = constantsidefinal / xsidefinal
	else:
		answer = 'undefined!!!!'

	if answer == 0:
		if "-" in str(answer):
			answernonegativezero = str(answer)
			answer = answernonegativezero.replace('-', '')


	return answer, xsidefinal, constantsidefinal