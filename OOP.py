class Cube:
  # init is a constructor :D
  # is allways called when an object is initialize :DDDD
  def __init__(self, owner, edge, color, transparency):
    self.owner = owner
    self.edge = edge
    self.color = color
    self.transparency = transparency

  def __del__(self):
    print("Destructor called, cube is going down")

  def create():
    cub = Cube()
    return cub

  def printCube(self):
    print("The owner is {}\nEdge:{}\nColor:{}\nTransparency:{}".format(self.owner, self.edge, self.color, self.transparency))

cubuLuiGabi = Cube("Gabi", 30, "black", 0)
cubuLuiSorin = Cube("Sorin", 5, "white", 100)

cubuLuiSorin.printCube()

