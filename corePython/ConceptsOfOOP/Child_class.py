class Person:
    def __init__(self, fname, lname):
        self.firstname = fname
        self.lastname = lname

    def printname(self):
        print(self.firstname, self.lastname)


class student(Person):
    pass


x = student('Anant', 'Agrawal')
x.printname()
