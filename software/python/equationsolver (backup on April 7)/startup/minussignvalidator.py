import reused.font as font
import sys

def minusremover(equationparts):

	minussignindexes = []

	#find un-needed minus signs, and throw an error if there is "-+" or "--" in the equation
	if "-" in equationparts:
		#add all indexes of "-" signs into a new list called minussignindexes
		for i in range(0, len(equationparts)):
			if equationparts[i] == "-":
				minussignindexes.append(i)
	
		#if the last thing in the equation is a minus sign, take it out of the equation list
		while len(equationparts) - 1 in minussignindexes:
			minussignindexes.remove(len(equationparts)-1)
			del equationparts[len(equationparts) - 1]

		#if there is a "-" sign before the equal sign, take it out of the equation list
		for i in minussignindexes:
			if equationparts[i + 1] == "=":
				minussignindexes.remove(i)
				del equationparts[i]
				break

		minussignindexes.clear()

		#add all indexes of "-" signs into a new list called minussignindexes
		for i in range(0, len(equationparts)):
			if equationparts[i] == "-":
				minussignindexes.append(i)

		for i in minussignindexes:
			if equationparts[i + 1] == "-":
				print(font.textcolors.bold + font.textcolors.fail +'\nThis is not a valid equation (there is a double minus sign') #Throw an error
				sys.exit()
				break
			if equationparts[i + 1] == "+":
				print(font.textcolors.bold + font.textcolors.fail +'\nThis is not a valid equation (there is a plus sign after a minus sign') #Throw an error
				sys.exit()
				break

	return equationparts