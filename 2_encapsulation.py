class Animal:
    def __init__(self, name: str,sex: str,age: int):
        self.name = name # 公開屬性
        self._sex=sex # 受保護屬性
        self.__age=age # 私有屬性（外部無法直接存取）

    def make_sound(self):
        return "Some generic sound"

class Dog(Animal):
    def make_sound(self):
        return "Woof!"

dog = Dog("Buddy","F",12)

print(dog.name)    # ✅ 可存取 (公開屬性)
print(dog._sex) #✅ 可存取 (受保護屬性, 但不建議)
# print(dog.__age)  # ❌ 會報錯，私有屬性無法直接存取
