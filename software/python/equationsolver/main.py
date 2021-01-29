import sys
import time

from equationsolver.reused import toputonothersider

from equationsolver.startup import duplicateequalsigns, equationsidevalidator, signvalidator, halfequation

from equationsolver.terms import terms, termsplitter

from equationsolver.sidesplitter import xsider, constantsider, sidecombiner

from equationsolver.signsolvers import multiplication, division

try:
	runtimes = 0
	while True:
		if runtimes > 0:
			print("\n\n")
		#get input 
		print('Please Write Your Equation in the Box Below \n') #prompt
		equation = str(input()) #get input (string)and set a variable to it
		equationwithoutspaces = equation.replace(" ", "") #get rid of the spaces

		#run duplicateequalsigns function and make sure that this is a valid equation
		equationparts, equationfirsthalf, equationsecondhalf = duplicateequalsigns.equalremover(equationwithoutspaces) #this made the equation into three lists, all of it, the first half, and the second half
		#neither equationfirsthalf or equationsecondhalf has an equal sign in it


		equationsidevalidatorreturnvalue = equationsidevalidator.equalvalidator(equationparts)
		#this returns whether to solve or simplify


		if equationsidevalidatorreturnvalue == "solve":
			#solve the equation
			print('\nSolving... (in main.py) \n')

			#this removes all un-needed signs from the equation
			print(equationparts, " before signvalidator (in main.py) \n")
			equationparts = signvalidator.remover(equationparts, equationfirsthalf, equationsecondhalf)
			print(equationparts, " after signvalidator (in main.py) \n")



			equationfirsthalf.clear()
			equationsecondhalf.clear()

			equationfirsthalf, equationsecondhalf = halfequation.halver(equationparts)

			print('\nafter halver (first half) (in main.py) : ', equationfirsthalf)
			print('\nafter halver (second half) (in main.py) : ', equationsecondhalf)
			print('\nequation (after halver) (in main.py) : ', equationparts)

			firsthalftermslist, toputonotherside = terms.termer(equationfirsthalf)

			print('\nFirst half terms  (in main.py) ', firsthalftermslist)

			secondhalftermslist, toputonotherside2 = terms.termer(equationsecondhalf)

			print('\nSecond half terms  (in main.py) ', secondhalftermslist)
			if toputonotherside2 != []:
				firsthalftermslist = toputonothersider.othersider(toputonotherside2, firsthalftermslist)
			if toputonotherside != []:
				secondhalftermslist = toputonothersider.othersider(toputonotherside, secondhalftermslist)

			firsthalftermslist = multiplication.producter(firsthalftermslist)
			secondhalftermslist = multiplication.producter(secondhalftermslist)

			print('Before: (in main.py)', firsthalftermslist, '\n', secondhalftermslist)
			firsthalftermslist = division.quotienter(firsthalftermslist)
			secondhalftermslist = division.quotienter(secondhalftermslist)
			print('After: (in main.py)', firsthalftermslist, '\n', secondhalftermslist)
			xtermsfirsthalf, constanttermsfirsthalf = termsplitter.termer(firsthalftermslist)

			print('\nxtermsfirsthalf (in main.py): ', xtermsfirsthalf)
			print('\nconstanttermsfirsthalf (in main.py): ', constanttermsfirsthalf)

			xtermssecondhalf, constanttermssecondhalf = termsplitter.termer(secondhalftermslist)

			print('\nx terms: first half  (in main.py) = ', xtermsfirsthalf, '\nsecond half  (in main.py) = ', xtermssecondhalf)
			print('\nconstant terms: first half  (in main.py) = ', constanttermsfirsthalf, '\nsecond half  (in main.py) = ', constanttermssecondhalf)

			xsidelist = xsider.sider(xtermsfirsthalf, xtermssecondhalf)

			print('xsidelist (in main.py) = ', xsidelist)

			constantsidelist = constantsider.sider(constanttermsfirsthalf, constanttermssecondhalf)

			print('constantsidelist (in main.py) = ', constantsidelist)

			answer, xsidefinal, constantsidefinal = sidecombiner.combiner(xsidelist, constantsidelist)

			print('Answer is: ', answer, '\n\n')
			time.sleep(2)
			
		elif equationsidevalidatorreturnvalue == "simplify":
			#simplify the expression
			print('\nSimplifying... (in main.py) \n')


		runagain = str(input('\nRun again? (y/n):  '))
		runagain_l = runagain.lower()
		if 'y' in runagain_l:
			print("Running program...")
			runtimes += 1
			continue
		else:
			print("\n\nProgram ended...")
			time.sleep(2)
			break
except KeyboardInterrupt:
	print('\n\nProgram ended...')
	time.sleep(2)
	sys.exit()
'''except:
	print('\n\nError...\n')
	print("Ending program...")
	time.sleep(2)
	sys.exit()'''