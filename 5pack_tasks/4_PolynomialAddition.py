class Polynomial:
    def __init__(self, *line):
        self.line = line
        self.size = len(line)

    def __call__(self, other):
        res = 0
        for i in range(self.size):
            res += self.line[i] * (other ** i)
        return res

    def __add__(self, *other):
        maximum = max(len(other), self.size)
        minimum = min(len(other), self.size)
        new_polynomial = []
        for i in range(0, maximum):
            if minimum >= i:
                new_polynomial.append(other[i] + self.line[i])
            elif self.size == maximum:
                new_polynomial.append(self.line[i])
            else:
                new_polynomial.append(other[i])
        print(new_polynomial)
        return Polynomial(new_polynomial)

    def __str__(self):
        return '{}, {}'.format(self.line, self.size)


poly1 = Polynomial(0, 1, 2, 3)
poly2 = Polynomial(10, 11)
poly3 = poly1 + poly2
