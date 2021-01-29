import reused.font as font
import sys
def plussignremover(equationparts, equationsecondhalf):
	plussignindexes = []
	
	#if there is a plus sign directly after the equal sign, take it out
	if "+" in equationsecondhalf: #if there is a "+" sign in the second half of the equation
		#if the "+" sign is the first thing in the second half
		while equationsecondhalf.index('+') == 0:
			del equationsecondhalf[0]
			indexequal = equationparts.index("=") #reset the variable for where the "=" sign is in the equation parts list
			afterequal = indexequal + 1 #reset the variable for the index after the "=" sign is in the equation parts list
			del equationparts[afterequal] #delete the un-needed "+" sign out of the equation parts list using the index above

	#find un-needed plus signs, and throw an error if there is "+-" or "++" in the equation
	if "+" in equationparts:

		#add all indexes of "+" signs into a new list called plussignindexes
		for i in range(0, len(equationparts)):
			if equationparts[i] == "+":
				plussignindexes.append(i)
		
		#if the last thing in the equation is a plus sign, take it out of the equation list
		while len(equationparts) - 1 in plussignindexes:
			plussignindexes.remove(len(equationparts)-1)
			del equationparts[len(equationparts) - 1]

		#if there is a "+" sign before the equal sign, take it out of the equation list
		for i in plussignindexes:
			if equationparts[i + 1] == "=":
				plussignindexes.remove(i)
				del equationparts[i]
				break

		for i in plussignindexes:
			if equationparts[i - 1] == '*' or equationparts[i - 1] == '/':
				print('equationparts[i]: ', equationparts[i])
				print('equationparts[i - 1]: ', equationparts[i-1])
				plussignindexes.remove(i)
				del equationparts[i]
				break

		plussignindexes.clear()
		#add all indexes of "+" signs into a new list called plussignindexes
		for i in range(0, len(equationparts)):
			if equationparts[i] == "+":
				plussignindexes.append(i)
		
		for i in plussignindexes:
			if equationparts[i + 1] == "+":
				print(font.textcolors.bold + font.textcolors.fail +'\nThis is not a valid equation (there is a double plus sign') #Throw an error
				sys.exit()
			elif equationparts[i + 1] == "-":
				print(font.textcolors.bold + font.textcolors.fail +'\nThis is not a valid equation (there is a minus sign after a plus sign') #Throw an error
				sys.exit()

	return equationparts