def othersider(toputonotherside, mylist):
	for i in range(0, len(toputonotherside)):
		print('line 5 in toputonothersider, ', mylist)
		mylist.append(toputonotherside[i])
		print('line 5 in toputonothersider, ', mylist)
	return mylist