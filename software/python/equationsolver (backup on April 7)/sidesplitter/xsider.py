def sider(xtermsfirsthalf, xtermssecondhalf):
	xsidelist = []
	for i in xtermsfirsthalf:
		if '+' in i:
			index = xtermsfirsthalf.index(i)
			newstring = xtermsfirsthalf[index].replace('+', '-')
			xsidelist.append(newstring)
		elif '-' in i:
			index = xtermsfirsthalf.index(i)
			newstring = xtermsfirsthalf[index].replace('-', '+')
			xsidelist.append(newstring)

	for i in xtermssecondhalf:
		xsidelist.append(i)
	
	return xsidelist