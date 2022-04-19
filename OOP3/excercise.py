from cmath import sqrt
from math import floor
class line:
    def __init__(self,x1,x2,y1,y2):
        self.x1=x1
        self.x2=x2
        self.y1=y1
        self.y2=y2
        self.length=0
        self.points=[]
    def distance(self):
        comp1=(self.x1-self.x2)**2
        comp2=(self.y1-self.y2)**2
        self.length=sqrt(comp1+comp2)
    def def_points(self):
        self.point_0=[self.x1,self.y1]
        self.points.append(self.point_0)
    def find_slope(self):
        self.slope=(self.x1-self.x2)/(self.y1-self.y2)
        return self.slope
    def __str__(self):
        return 