import sys
def remover(equationparts, equationfirsthalf, equationsecondhalf):
	
	#if there is a plus sign very first in the equation, take it out
	if "+" in equationfirsthalf: #if there is a "+" sign in the first half of the equation
		while equationparts.index('+') == 0: #if the "+" sign is the first thing in the equation
			del equationparts[0] #delete it out of the whole equation list

	#if there are plus signs at the end of the first half of the equation, take them out
	while "+" == equationfirsthalf[-1] or "-" == equationfirsthalf[-1]:
		del equationfirsthalf[-1]
		del equationparts[len(equationfirsthalf)]


	plussignindexes = []
	minussignindexes = []
	
	#if there is a plus sign directly after the equal sign, take it out
	if "+" in equationsecondhalf: #if there is a "+" sign in the second half of the equation
		#if the "+" sign is the first thing in the second half
		while equationsecondhalf.index('+') == 0:
			del equationsecondhalf[0]
			indexequal = equationparts.index("=") #reset the variable for where the "=" sign is in the equation parts list
			afterequal = indexequal + 1 #reset the variable for the index after the "=" sign is in the equation parts list
			del equationparts[afterequal] #delete the un-needed "+" sign out of the equation parts list using the index above

	#find un-needed plus signs and delete them
	if "+" in equationparts:

		#add all indexes of "+" signs into a new list called plussignindexes
		for i in range(0, len(equationparts)):
			if equationparts[i] == "+":
				plussignindexes.append(i)

		#add all indexes of "-" signs into a new list called minussignindexes
		for i in range(0, len(equationparts)):
			if equationparts[i] == "-":
				minussignindexes.append(i)

		while len(equationparts)-1 in plussignindexes or len(equationparts)-1 in minussignindexes:
			#if the last things in the equation are plus signs, take them out of the equation list
			while len(equationparts)-1 in plussignindexes:
				plussignindexes.remove(len(equationparts)-1)
				del equationparts[-1]

			#if the last things in the equation are minus signs, take them out of the equation list
			while len(equationparts)-1 in minussignindexes:
				minussignindexes.remove(len(equationparts)-1)
				del equationparts[-1]


		for i in plussignindexes:
			if equationparts[i - 1] == '*' or equationparts[i - 1] == '/':
				plussignindexes.remove(i)
				del equationparts[i]

		plussignindexes.clear()
		#add all indexes of "+" signs into a new list called plussignindexes
		for i in range(0, len(equationparts)):
			if equationparts[i] == "+":
				plussignindexes.append(i)

		deletelist = []
		#if there are plus signs next to each other, take them out
		for i in range(0, len(plussignindexes)):
			if len(plussignindexes)-1 > i:
				if plussignindexes[i]+1 == plussignindexes[i+1]:
					deletelist.append(plussignindexes[i])

		for i in range(0, len(deletelist)):
			del equationparts[deletelist[i]-i]

		minussignindexes.clear()
		#add all indexes of "-" signs into a new list called minussignindexes
		for i in range(0, len(equationparts)):
			if equationparts[i] == "-":
				minussignindexes.append(i)

		deletelist.clear()
		#if there are minus signs next to each other, take them out
		for i in range(0, len(minussignindexes)):
			if len(minussignindexes)-1 > i:
				if minussignindexes[i]+1 == minussignindexes[i+1]:
					deletelist.append(minussignindexes[i])

		for i in range(0, len(deletelist)):
			del equationparts[deletelist[i]-i]


		minussignindexes.clear()
		#add all indexes of "-" signs into a new list called minussignindexes
		for i in range(0, len(equationparts)):
			if equationparts[i] == "-":
				minussignindexes.append(i)

		plussignindexes.clear()
		#add all indexes of "+" signs into a new list called minussignindexes
		for i in range(0, len(equationparts)):
			if equationparts[i] == "+":
				plussignindexes.append(i)

		for i in range(0, len(plussignindexes)):
			if plussignindexes[i]+1 in minussignindexes:
				del equationparts[plussignindexes[i]]
				del plussignindexes[i]

		for i in range(0, len(minussignindexes)):
			if minussignindexes[i]+1 in plussignindexes:
				del equationparts[minussignindexes[i]+1]
				plussignindexes.remove(minussignindexes[i]+1)

	return equationparts