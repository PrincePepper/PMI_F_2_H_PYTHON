class Balance:
    def __init__(self):
        self.right = 0
        self.left = 0

    def add_left(self, item):
        self.left = self.left + item

    def add_right(self, item):
        self.right = self.right + item

    def result(self):
        if self.left == self.right:
            return '='
        elif self.left > self.right:
            return 'L'
        else:
            return 'R'


balance = Balance()
balance.add_right(10)
balance.add_left(9)
balance.add_left(2)
print(balance.result())
