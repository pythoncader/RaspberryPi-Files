def sider(constanttermsfirsthalf, constanttermssecondhalf):
	constantsidelist = []
	for i in constanttermssecondhalf:
		if '+' in i:
			index = constanttermssecondhalf.index(i)
			newstring = constanttermssecondhalf[index].replace('+', '-')
			constantsidelist.append(newstring)
		elif '-' in i:
			index = constanttermssecondhalf.index(i)
			newstring = constanttermssecondhalf[index].replace('-', '+')
			constantsidelist.append(newstring)

	for i in constanttermsfirsthalf:
		constantsidelist.append(i)

	return constantsidelist