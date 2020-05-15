def isPrime(a):
    if a % 2 == 0:
        return a == 2
    d = 3
    while d * d <= a and a % d != 0:
        d += 2
    return d * d > a


def polindrom(b):
    if b != b[::-1]:
        return False
    return True


def stepenTwo(c):
    if c & (c - 1):
        return False
    return True


def check_pin(pinCode):
    a, b, c = pinCode.split("-")
    if isPrime(int(a)) and polindrom(b) and stepenTwo(int(c)):
        return "Корректен"
    else:
        return "Некорректен"


print(check_pin('12-22-16'))
