
class Fraction:
    def __init__(self, num, demon):
        self.num = num
        self.demon = demon

    def __str__(self):    
        
        return str(self.num) + "\\" + str(self.demon)

    def __add__(self, other):
        top = self.num * other.demon + self.demon * other.num
        bot = self.demon * other.demon
        return Fraction(top, bot)

    def __sub__(self, other):
        top = self.num * other.demon - self.demon * other.num
        bot = self.demon * other.demon
        return Fraction(top, bot)

a = Fraction(3, 5)
b = Fraction(4, 3)
c = a + b
print(c)

c = a - b
print(c)