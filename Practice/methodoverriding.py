class circle:
  
 def __init__(self,radius):
  self.radius = radius
  self.pi = 3.14

 def area(self):
  return 0.5 * (self.radius^2) * self.pi

 def __repr__(self):
   return "radius=" + str(self.radius)


class cylinder(circle):
 def __init__(self, height, radius):
   super().__init__(radius)
   self.height = height

 def area(self):
   return (2 * self.pi + self.radius * 2) + (2 * self.pi * self.radius * self.height)

 def volume(self):
   return 2 * self.pi * self.radius * self.height

 def __repr__(self):
   return super().__repr__() + " height=" + str(self.height)

if(__name__ == "__main__"):
    cy = cylinder(12,5)
    print(cy)
    print(round(cy.area(),2))
    print(cy.volume())
    #iterator vs generator 
    
