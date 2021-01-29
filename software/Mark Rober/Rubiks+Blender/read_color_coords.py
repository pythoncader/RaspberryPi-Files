#Help from https://www.yawintutor.com/typeerror-tuple-object-does-not-support-item-assignment/
# Test program to retrieve the color coordinates from the text file color_coords.txt
#

file = open("color_coords.txt", "r")
numlist = file.readlines()

allNums = []
x = []
y = []

side1 = ((0,0),
         (0,0),
         (0,0),
	     (0,0),
	     (0,0),
	     (0,0),
	     (0,0),
	     (0,0),
	     (0,0))
side2 = ((0,0),
         (0,0),
         (0,0),
	     (0,0),
	     (0,0),
	     (0,0),
	     (0,0),
	     (0,0),
	     (0,0))
side3 = ((0,0),
         (0,0),
         (0,0),
	     (0,0),
	     (0,0),
	     (0,0),
	     (0,0),
	     (0,0),
	     (0,0))


#print(list)
for line in numlist:
    allNums += line.strip().split(" ") # get a list containing 
    print(line)
for num in range(27*2):
    
    if(num % 2) == 0:
        x.append(allNums[num])
    else:
        y.append(allNums[num])

#x_list = list(x)
#y_list = list(y)    
#for i in range(0,8):
#    side1_list[i][0] = x_list[i]
#    side1_list[i][1] = y_list[i]

#for i in range(9,17):
#    side2_list[i][0] = x_list[i]
#    side2_list[i][1] = y_list[i]

#for i in range(18,27):
#    side3_list[i][0] = x_list[i]
#    side3_list[i][1] = y_list[i]

#print (side1)
#print (side2)
#print (side3)    
file.close()