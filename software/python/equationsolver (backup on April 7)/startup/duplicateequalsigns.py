import reused.font as font
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
			print(font.textcolors.bold + font.textcolors.fail +'\nThis is not a valid equation') #Throw an error
			sys.exit()
			break

		#if it sees an equal sign and it is the first thing that it sees
		if i == "=" and equalsign == 0 and len(equationparts) == 0:
			equalsign += 1
			print(font.textcolors.bold + font.textcolors.fail +'\nThis is not a valid equation') #Throw an error
			sys.exit()
			break
	
		if equalsign == 0:
			equationfirsthalf.append(i)
		elif equalsign == 1:
			equationsecondhalf.append(i)
			
		#print('runtimes: '+str(len(equationparts))) #this prints the number of times the for loop has run
		equationparts.append(i)
	if equationparts[-1] == "=":
		print(font.textcolors.bold + font.textcolors.fail +'\nThis is not a valid equation') #Throw an error
		sys.exit()
	return equationparts, equationfirsthalf, equationsecondhalf