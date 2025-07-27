class Animal:
    def speak(self):
        return "The animal makes a sound."

class Dog(Animal):
    def speak(self):
        return "The dog barks."

class Cat(Animal):
    def speak(self):
        return "The cat meows."

# Demonstration of hierarchical inheritance
if __name__ == "__main__":
    animal = Animal()
    dog = Dog()
    cat = Cat()
    
    print(animal.speak())  # Output: The animal makes a sound.
    print(dog.speak())     # Output: The dog barks.
    print(cat.speak())     # Output: The cat meows.