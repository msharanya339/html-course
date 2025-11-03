# parent class
class person(object):
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def display(self):
        print("Name:", self.name)
        print("Age:", self.age)

# child class
class student(person):
    def __init__(self, name, age, idnumber, salary, post):
        person.__init__(self, name, age)
        self.idnumber = idnumber
        self.salary = salary
        self.post = post
    