class Polynomial:
    def __init__(self, line: list):
        self.line = line.copy()
        self.size = len(line)

    def __call__(self, other):
        res = 0
        for i in range(self.size):
            res += self.line[i] * (other ** i)
        return res

    def __add__(self, other):
        maximum = max(len(other.line), self.size)
        minimum = min(len(other.line), self.size)
        _new_polynomial = []
        for i in range(0, maximum):
            if minimum > i:
                _new_polynomial.append(other.line[i] + self.line[i])
            elif self.size == maximum:
                _new_polynomial.append(self.line[i])
            else:
                _new_polynomial.append(other.line[i])
        return Polynomial(_new_polynomial)

    def __str__(self):
        return '{}, {}'.format(self.line, self.size)


a = [10, -1]
poly = Polynomial(a)
poly2 = Polynomial([15, -3, 5])
a.append(10)
poly3 = poly + poly2
print(poly3(0))
print(poly3(1))
print(poly3(2))
