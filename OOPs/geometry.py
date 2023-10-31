from math import sqrt
from fractions import Fraction
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

    # pylint: disable-next=too-many-arguments, unused-argument
    def __new__(cls, name, x1=0, y1=0, x2=0, y2=0):
        if (x1, y1) != (x2, y2):
            return super().__new__(cls)
        return None

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
        x1, y1, x2, y2 = self.x1, self.y1, self.x2, self.y2

        # if x or y unchanged it's parallel to axis
        if x1 == x2:
            return f'x = {x1}'
        if y1 == y2:
            return f'y = {y1}'

        #    (y - y1)/(x - x1) = (y2 - y1)/(x2 - x1) = n/d
        # => dy - nx = d•y1 - n•x1
        n, d = Fraction(y2-y1, x2-x1).as_integer_ratio()
        dy = "y" if d == 1 else f"{d}y"
        nx = "x" if abs(n) == 1 else f"{abs(n)}x"
        sign = "-" if n > 0 else "+"

        return f"{dy} {sign} {nx} = {d*y1 - n*x1}"
