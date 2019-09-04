class Wings:
  def __str__(self):
    return "Wings"
    
  def fly(self):
    print("Flying /\\o/\\ ")

class ChickenWings:
  def __init__(self):
    self.price = 100
    
  def __str__(self):
    return "ChickenWings @{}".format(self.price)
    
  def fly(self):
    print("Can't!! I'm Dead")

# copyright leangaurav@github