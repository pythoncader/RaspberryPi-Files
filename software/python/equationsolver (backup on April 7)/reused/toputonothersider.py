import reused.font as font
def othersider(toputonotherside, mylist):
	for i in range(0, len(toputonotherside)):
		print(font.textcolors.okgreen, 'line 5 in toputonothersider, ', mylist)
		mylist.append(toputonotherside[i])
		print(font.textcolors.okgreen, 'line 5 in toputonothersider, ', mylist)
	return mylist