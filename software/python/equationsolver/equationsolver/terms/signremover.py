def remover(mystring):
	for i in range(0, len(mystring)):
		if mystring[i].isdigit() or mystring[i] == 'x':
			return mystring
		else:
			mystring = mystring.replace(mystring[i], '', 1)
			return mystring