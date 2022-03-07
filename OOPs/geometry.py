from math import sqrt, gcd
from dataclasses import dataclass


@dataclass
class Point:
    name: str
    x: float = 0
    y: float = 0

    def __sub__(self, other=None):
        other = other or Point('O')
        return Line(other.name+self.name, other.x, other.y, self.x,  self.y)

    def distance(self, other=None):
        return (self-other).length if (self-other) else 0


@dataclass
class Line:
    name: str
    x1: float = 0
    y1: float = 0
    x2: float = 0
    y2: float = 0

    def __new__(cls, name, x1=0, y1=0, x2=0, y2=0):
        if (x1 != x2) or (y1 != y2):
            return super().__new__(cls)

    @property
    def center(self):
        midx = (self.x1 + self.x2) / 2
        midy = (self.y1 + self.y2) / 2
        return Point(f'center_{self.name}', midx, midy)

    @property
    def length(self):
        len_sqr = (self.x1 - self.x2)**2 + (self.y1 - self.y2)**2
        # return sqrt(len_sqr) # change for fun
        length = int(sqrt(len_sqr))
        return length if (length**2 == len_sqr) else f'√{len_sqr}'

    @property
    def equation(self):
        # sorted for taking min value in first term
        x1, x2 = sorted([self.x1, self.x2])
        y1, y2 = sorted([self.y1, self.y2])

        # if x or y unchanged it's parallel to axis
        if x1 == x2:
            return f'x = {x1}'
        if y1 == y2:
            return f'y = {y1}'

        d = gcd(x2-x1, y2-y1)
        a, b = (x2 - x1)//d, (y2 - y1)//d
        if a == b:
            a = b = ''

        def decider(val, val_other, z, cor):
            z = '' if z == 1 else z
            if not val or (a*y1 == b*x1):
                return f'{z}{cor}'
            else:
                return f'{z}({cor} - {val})'

        lhs = decider(y1, x1, a, 'y')
        rhs = decider(x1, y1, b, 'x')
        return lhs + " = " + rhs
