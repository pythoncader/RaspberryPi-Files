file = open("corner_coords.txt", "r")
numlist = file.readlines()

allNums = []
x = []
y = []

polygon = ((0,0),(0,0),(0,0),(0,0),(0,0),(0,0))


#print(list)
for line in numlist:
    allNums += line.strip().split(" ") # get a list containing 
    
for num in range(6*2):
    
    if(num % 2) == 0:
        x.append(int(allNums[num]))
    else:
        y.append(int(allNums[num]))

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

print(x,y)
file.close()