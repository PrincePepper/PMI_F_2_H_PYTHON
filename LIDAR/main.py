class Median_filter():
    def __init__(self, *line, step=3, amount=1):
        self.LINE = line
        self.SIZE = len(line)
        self.STEP = step
        self.AMOUNT = amount

    def middle_of_3(self, a, b, c):
        if a <= b & a <= c:
            middle = b if b <= c else c
        else:
            if b <= a & b <= c:
                middle = a if a <= c else c
            else:
                middle = a if a <= b else b

    def middle_more_than_3(self):
        stopper = 0  # Smaller than any datum
        buffer = [0] * self.STEP  # Buffer of width pairs
        datpoint = buffer  # Pointer into circular buffer of data
        if self.STEP == stopper:
            self.STEP = stopper + 1
        if (1 + datpoint - buffer) >= self.STEP:
            datpoint = buffer

    def start(self):
        for i in range(self.SIZE):
            if self.STEP < 3:
                return
            if self.STEP == 3:
                self.middle_of_3(1, 2, 3)
            else:
                self.middle_more_than_3()
