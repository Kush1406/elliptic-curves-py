INF_POINT = None

class EllipticCurve:

  def __init__(self, a, b, p):
    self.a = a
    self.b = b
    self.p = p
    self.points = []
    self.define_points()

  def define_points(self):
    self.points.append(INF_POINT)
    for x in range(self.p):
      for y in range(self.p):
        if self.equal_modp(y * y, x * x * x + self.a * x + self.b):
          self.points.append((x,y))

  def print_points(self):
    print(self.points)


  # helper functions

  def reduce_modp(self, x):
    return x % self.p


  def equal_modp(self, x, y):
    return self.reduce_modp(x - y) == 0
    
  def inverse_modp(self, x):
    for y in range(self.p):
      if equal_mod(x * y, 1): 
        return y
    return None


ec = EllipticCurve(2, 7, 19)
ec.print_points()
