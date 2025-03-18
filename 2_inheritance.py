# 定義父類別
class Animal:
    def __init__(self, name: str):
        self.name = name

    def make_sound(self):
        pass  # 這是抽象方法，由子類別實作

# 定義子類別，繼承 Animal
class Dog(Animal):
    def make_sound(self):
        return "Woof!"

# 使用子類別
dog = Dog("Buddy")

print(dog.make_sound())  # Woof!