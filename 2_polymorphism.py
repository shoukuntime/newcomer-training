# 定義父類別
class Animal:
    def __init__(self, name: str):
        self.name = name

    def make_sound(self):
        return "Some generic sound"

class Dog(Animal):
    def make_sound(self):
        return "Woof!"

# 多型範例
dog = Dog("Buddy")

print(dog.make_sound())  # Woof!