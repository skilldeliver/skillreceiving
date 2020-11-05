class Difference:
    def __init__(self, a):
        self.__elements = a
        self.maximumDifference = -1000000
	# Add your code here
    def computeDifference(self):
        for i in self.__elements:
            for j in self.__elements:
                sum_el = abs(i - j)
                if sum_el > self.maximumDifference:
                    self.maximumDifference = sum_el

# End of Difference class

_ = input()
a = [int(e) for e in input().split(' ')]

d = Difference(a)
d.computeDifference()

print(d.maximumDifference)