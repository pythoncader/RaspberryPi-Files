import sys

def equalremover(equationwithoutspaces):
	equalsign = 0
	equationparts = []
	equationfirsthalf = []
	equationsecondhalf = []
	#loop through the equation and make sure that it does not have duplicate "=" signs
	#add each character to a list called equationparts
	for i in equationwithoutspaces:

		#if it sees an equal sign for the first time and it is not the first thing that it sees
		if i == "=" and equalsign == 0 and len(equationparts) > 0:
			equalsign += 1
			equationparts.append(i)
			continue

		#if it sees an equal sign and it is not the first equal sign
		if i == "=" and equalsign > 0:
			sys.exit('\nThis is not a valid equation')
			break

		#if it sees an equal sign and it is the first thing that it sees
		if i == "=" and equalsign == 0 and len(equationparts) == 0:
			equalsign += 1
			sys.exit('\nThis is not a valid equation')
			break
	
		if equalsign == 0:
			equationfirsthalf.append(i)
		elif equalsign == 1:
			equationsecondhalf.append(i)
			
		equationparts.append(i)
	if equationparts[-1] == "=":
		sys.exit('\nThis is not a valid equation')

	return equationparts, equationfirsthalf, equationsecondhalf