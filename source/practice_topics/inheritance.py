class Animal:
    def __init__(self, legs):
        self.legs = legs

    def makeSound(self):
        print("No sound")

class Fish(Animal):
    def __init__(self):
        super().__init__(0) 

    def swim(self):
        print("Just keep swimming")

class Dog(Animal):
    def __init__(self):
        super().__init__(4)

    def makeSound(self):
        print("WOOOOFFWOOOF")  

nemo = Fish()
print(f"nemo has {nemo.legs} nr of legs")
nemo.makeSound()
nemo.swim()

myDog = Dog()
print(f"My dog has {myDog.legs} nr of legs")
myDog.makeSound()