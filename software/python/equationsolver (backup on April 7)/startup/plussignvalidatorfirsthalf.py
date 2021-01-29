def plussignremover(equationparts, equationfirsthalf):

	#if there is a plus sign very first in the equation, take it out
	if "+" in equationfirsthalf: #if there is a "+" sign in the first half of the equation
		while equationparts.index('+') == 0: #if the "+" sign is the first thing in the equation
			del equationparts[0] #delete it out of the whole equation list
	return equationparts