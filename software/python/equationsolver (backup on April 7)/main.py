import reused.font as font
import reused.toputonothersider as toputonothersider

import startup.duplicateequalsigns as duplicateequalsigns
import startup.equationsidevalidator as equationsidevalidator
import startup.plussignvalidatorfirsthalf as plussignvalidatorfirsthalf
import startup.plussignvalidatorsecondhalf as plussignvalidatorsecondhalf
import startup.minussignvalidator as minussignvalidator
import startup.halfequation as halfequation
import startup.replacewithx as replacewithx

import terms.terms as terms
import terms.termsplitter as termsplitter
import sidesplitter.xsider as xsider
import sidesplitter.constantsider as constantsider
import sidesplitter.sidecombiner as sidecombiner
import signsolvers.multiplication as multiplication
import signsolvers.division as division

#get input
print('\nPlease Write Your Equation in the Box Below \n') #prompt
equation = str(input()) #get input (string) and set a variable to it
equationwithoutspaces = equation.replace(" ", "") #get rid of the spaces

#run duplicateequalsigns function and make sure that this is a valid equation
equationparts, equationfirsthalf, equationsecondhalf = duplicateequalsigns.equalremover(equationwithoutspaces)

equationparts = replacewithx.replacer(equationparts)
equationfirsthalf = replacewithx.replacer(equationfirsthalf)
equationsecondhalf = replacewithx.replacer(equationsecondhalf)
equationsidevalidatorreturnvalue = equationsidevalidator.equalvalidator(equationparts)
if equationsidevalidatorreturnvalue == "solve":
	#solve the equation
	print('\nSolving... (in main.py) \n')

	print(equationparts, ' before plussignvalidatorfirsthalf (in main.py) \n')
	equationparts = plussignvalidatorfirsthalf.plussignremover(equationparts, equationfirsthalf)
	print(equationparts, ' after (in main.py) \n')

	equationparts = plussignvalidatorsecondhalf.plussignremover(equationparts, equationsecondhalf)
	print(equationparts, " after plussignvalidatorsecondhalf (in main.py) \n")

	equationparts = minussignvalidator.minusremover(equationparts)
	print(equationparts, ' after minussignvalidator (in main.py) \n')

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
		print("toputonotherside2,", toputonotherside2)
		firsthalftermslist = toputonothersider.othersider(toputonotherside2, firsthalftermslist)
	if toputonotherside != []:
		print("toputonotherside,", toputonotherside)
		secondhalftermslist = toputonothersider.othersider(toputonotherside, secondhalftermslist)

	firsthalftermslist = multiplication.producter(firsthalftermslist)
	secondhalftermslist = multiplication.producter(secondhalftermslist)

	print('Before division first half (in main.py): ', firsthalftermslist)
	firsthalftermslist = division.quotienter(firsthalftermslist)
	print('After division first half (in main.py): ', firsthalftermslist)
	print('Before division second half (in main.py): ', secondhalftermslist)
	secondhalftermslist = division.quotienter(secondhalftermslist)
	print('After division second half (in main.py): ', secondhalftermslist)
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

	print(font.textcolors.underlined, font.textcolors.okgreen, '\n\nAnswer is: ', answer, "\n", font.textcolors.endc)
	
elif equationsidevalidatorreturnvalue == "simplify":
	#simplify the expression
	print('\nSimplifying... (in main.py) \n')