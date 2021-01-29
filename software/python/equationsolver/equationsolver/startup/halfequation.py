def halver(equationparts):
	
	equationfirsthalf = []
	equationsecondhalf = []
	equalsign = 0

	#put the halves of the equation into the half equation lists
	for i in equationparts:
		if i != "=" and equalsign == 0:
			equationfirsthalf.append(i)
		elif i == "=":
			equalsign = 1
			continue
		elif i != "=" and equalsign == 1:
			equationsecondhalf.append(i)

	return equationfirsthalf, equationsecondhalf