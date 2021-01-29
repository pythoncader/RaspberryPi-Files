import reused.font as font
import sys

solveorsimplify = ''

def equalvalidator(equationparts):
	#This checks where the "=" sign is in the equation, then it figures out whether there is something on both sides of the equation
	if "=" in equationparts: #if there is an equal sign in the equation
		indexequal = equationparts.index("=") #setting a variable to the index of the equal sign in the list
		afterequal = indexequal + 1 #setting a variable to the value of the index directly after the equal sign
		highestindex = len(equationparts) - 1 #finding the highest index number in the list (basically checking whether there is something after the "=" sign in the equation)
		#print('highest index: '+str(highestindex)) #printing that value

		if highestindex < afterequal: #if there is not a value after the equal sign
			print(font.textcolors.bold + font.textcolors.fail +'\nThis is not a valid equation') #Throw an error
			sys.exit()

		else: #if there is a value after the equal sign
			solveorsimplify = 'solve'
			return solveorsimplify

	else: #if there is not an equal sign in the equation
		solveorsimplify = 'simplify'
		return solveorsimplify