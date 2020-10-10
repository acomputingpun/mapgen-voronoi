import math

class Vec2(tuple):
    def __new__(self, x, y=None):
        if (y is None):
            (x, y) = x
        return tuple.__new__(Vec2, (x, y))
    def __add__(self, other):
        return Vec2(self[0]+other[0],self[1]+other[1])
    def __sub__(self, other):
        return Vec2(self[0]-other[0],self[1]-other[1])
    def __mul__(self, scalar):
        return Vec2(self[0]*scalar,self[1]*scalar)
    def __div__(self, scalar):
        return Vec2(self[0]/scalar,self[1]/scalar)
    def __eq__(self, other):
        return self[0] == other[0] and self[1] == other[1]
    def __hash__(self):
        return hash((self[0], self[1]))

    def __str__(self):
        return "v"+str(self.xy)
    def __repr__(self):
        return "v"+str(self.xy)

    def sub(self, other):
        return self-other
    def add(self, other):
        return self+other
    def sMul(self, scalar):
        return self*scalar
    def hMul(self, other):
        return Vec2(self[0]*other[0],self[1]*other[1])
    def dMul(self, other):
        return self[0]*other[0] + self[1]*other[1]
    def sDiv(self, scalar):
        return Vec2(self[0]/scalar,self[1]/scalar)
    def hDiv(self, other):
        return Vec2(self[0]/other[0],self[1]/other[1])
    def interp(self, scalar, other):
        return self+((other-self)*scalar)
    def floor(self):
        return Vec2(math.floor(self[0]), math.floor(self[1]))
    def round(self):
        return Vec2(round(self[0]), round(self[1]))

    @property
    def x(self):
        return self[0]
    @property
    def y(self):
        return self[1]
    @property
    def xy(self):
        return (self[0], self[1])

    @property
    def mag(self):
        return math.sqrt((self[0]**2)+(self[1]**2))

    @property
    def magPy(self):
        return math.sqrt((self[0]**2)+(self[1]**2))
    @property
    def magMan(self):
        return abs(self[0]) + abs(self[1])
    @property
    def mag4(self):
        return max(abs(self[0]),abs(self[1]))

    @property
    def norm(self):
        return self.sMul(1/self.mag)

def min2(v1, v2):
    return Vec2(min(v1[0], v2[0]), min(v1[1], v2[1]))
def max2(v1, v2):
    return Vec2(max(v1[0], v2[0]), max(v1[1], v2[1]))
