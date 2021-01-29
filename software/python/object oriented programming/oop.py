class Polygon:
    def __init__(self, no_of_sides):
        self.n = no_of_sides
        self.sideslist = [0 for i in range(no_of_sides)]
        if 'Triangle' in str(type(self)):
            print('\nYou made a Triangle!')
        elif 'Square' in str(type(self)):
            print('\nYou made a Square!')
        else:
            print('\nYou made a Polygon!')

    def inputSides(self):
        if isinstance(self, Square) == True:
            self.sideslist[0] = float(input("Enter side: "))
            self.sideslist[1] = self.sideslist[0]
            self.sideslist[2] = self.sideslist[0]
            self.sideslist[3] = self.sideslist[0]
        else:
            self.sideslist = [float(input("Enter side "+str(i+1)+": ")) for i in range(self.n)]

    def dispSides(self):
        for i in range(self.n):
            print("Side",i+1,"is",self.sideslist[i])

class Triangle(Polygon):
    def __init__(self):
        Polygon.__init__(self,3)

    def findArea(self):
        a, b, c = self.sideslist
        # calculate the semi-perimeter
        s = (a + b + c) / 2
        self.area = (s*(s-a)*(s-b)*(s-c)) ** 0.5

class Square(Polygon):
    def __init__(self):
        Polygon.__init__(self, 4)
    def findArea(self):
        s1 = self.sideslist[0]
        self.area = s1 * s1

    

myTriangle = Triangle()
myTriangle.inputSides()
myTriangle.dispSides()
myTriangle.findArea()
print('Your area is:', myTriangle.area)
mypolygon = Polygon(6)
mypolygon.inputSides()
mypolygon.dispSides()
mysquare = Square()
mysquare.inputSides()
mysquare.findArea()
print('Your area is:', mysquare.area)