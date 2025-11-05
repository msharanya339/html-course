class Dog:
    def __init__(self, name, age):
        self.name = name
        self.age = age
        print(f"hello, i am {self.name} and i am {self.age} years old.")
    def speak(self):
        return "Woof!"

class Cat:
    def __init__(self, name, age):
        self.name = name
        self.age = age
        print(f"hello, i am {self.name} and i am {self.age} years old.")
    def speak(self):
        return "Meow!"

def animal_sound(animal):
    print(animal.speak())
dog = Dog("Buddy", 3)
cat = Cat("Whiskers", 2)
        

    