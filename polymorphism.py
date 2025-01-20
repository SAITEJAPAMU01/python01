class Animal:
    def speak(self):
        pass

class Dog(Animal):
    def speak(self):
        return "Bark"

class Cat(Animal):
    def speak(self):
        return "Meow"

class Duck(Animal):
    def speak(self):
        return "Quack"

def animal_sound(animal):
    print(animal.speak())

# Creating instances of each animal
dog = Dog()
cat = Cat()
duck = Duck()

# Demonstrating polymorphism
animal_sound(dog)  # Output: Bark
animal_sound(cat)  # Output: Meow
animal_sound(duck) # Output: Quack
