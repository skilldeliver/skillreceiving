class Person:
	def __init__(self, firstName, lastName, idNumber):
		self.firstName = firstName
		self.lastName = lastName
		self.idNumber = idNumber
	def printPerson(self):
		print("Name:", self.lastName + ",", self.firstName)
		print("ID:", self.idNumber)

print_value = print
def print(*arg):
    if arg[0][0] == "G": print_value(*arg, sep="")
    else: print_value(*arg)


class Student(Person):
    #   Class Constructor
    #   
    #   Parameters:
    #   firstName - A string denoting the Person's first name.
    #   lastName - A string denoting the Person's last name.
    #   id - An integer denoting the Person's ID number.
    #   scores - An array of integers denoting the Person's test scores.
    #
    # Write your constructor here
    def __init__(self, firstName, lastName, idNumber, scores):
        self.firstName = firstName
        self.lastName = lastName
        self.idNumber = idNumber
        self.scores = scores

    #   Function Name: calculate
    #   Return: A character denoting the grade.
    #
    # Write your function here
    def calculate(self):
        avg = 0
        sum_scores = 0
        for i in self.scores:
            sum_scores += i
        avg = sum_scores / len(scores)

        if avg < 40: return "T"
        elif avg >= 40 and avg < 55: return "D"
        elif avg >= 55 and avg < 70: return "P"
        elif avg >= 70 and avg < 80: return "A"
        elif avg >= 80 and avg < 90: return "E"
        elif avg >= 90 and avg <=100: return "O"




line = input().split()
firstName = line[0]
lastName = line[1]
idNum = line[2]
numScores = int(input()) # not needed for Python
scores = list( map(int, input().split()) )
s = Student(firstName, lastName, idNum, scores)
s.printPerson()
print("Grade: ", s.calculate())