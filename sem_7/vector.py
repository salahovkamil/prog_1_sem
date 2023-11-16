class Vector():
    def __init__(self,x,y,z):
        self.x = x
        self.y = y
        self.z = z
        #assert str(x).isdigit() == True
        #assert str(y).isdigit() == True
        #assert str(z).isdigit() == True

    def __abs__(self):
        return (self.x ** 2 + self.y ** 2 + self.z ** 2) ** 0.5
    def __add__(self, other_vector):
        return (self.x + other_vector.x, self.y + other_vector.y,self.z + other_vector.z)
    def __sub__(self, other_vector):
        return (self.x - other_vector.x, self.y - other_vector.y,self.z - other_vector.z)
    def __mul__(self, other_vector):
        return (self.x * other_vector.x, self.y * other_vector.y,self.z * other_vector.z)
    def __rmul__(self, a):
        return (self.x * a, self.y * a,self.z * a)
