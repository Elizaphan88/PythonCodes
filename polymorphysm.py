class Animal:
    def make_sound(self):
        pass

class Dog(Animal):
    def make_sound(self):
        return "Woof!"

class Cat(Animal):
    def make_sound(self):
        return "Meow!"

def animal_speak(animal):
    return animal.make_sound()

dog = Dog()
cat = Cat()

print(animal_speak(dog))  # Calls Dog's make_sound method
print(animal_speak(cat))  # Calls Cat's make_sound method
