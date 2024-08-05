class Animal:
    def __init__(self, name):
        self.alive = True            # Живой
        self.fed = False             # Накормленный
        self.name = name             # Индивидуальное название каждого животного


class Plant:
    def __init__(self, name):
        self.edible = False                                  # Несъедобное
        self.name = name                                     # Индивидуальное название каждого растения

class Mammal(Animal):                                        # Млекопитающие
    def eat(self, food):
        if food.edible:                                      # Если съедобно, то
            print(f"{self.name} съел {food.name}")           # выводим сообщение
            self.fed = True                                  # Меняем атрибут на True (накормлен)
        else:                                                # Если не съедобное, то
            print(f"{self.name} не стал есть {food.name}")   # выводим сообщение
            self.alive = False                               # Меняем атрибут на False (не живой)

class Predator(Animal):                                      # Хищник
    def eat(self, food):
        if food.edible:                                      # Если съедобно, то
            print(f"{self.name} съел {food.name}")           # выводим сообщение
            self.fed = True                                  # Меняем атрибут на True (накормлен)
        else:                                                # Если не съедобное, то
            print(f"{self.name} не стал есть {food.name}")   # выводим сообщение
            self.alive = False


class Flower(Plant):
    def __init__(self, name):
        self.name = name
        self.edible = False   # Переопределять не опязательно, т.к. в классе Plant по умолчанию False

class Fruit(Plant):
    def __init__(self, name):
        self.name = name
        self.edible = True


a1 = Predator('Волк с Уолл-Стрит')
a2 = Mammal('Хатико')
p1 = Flower('Цветик семицветик')
p2 = Fruit('Заводной апельсин')

print(a1.name)
print(p1.name)

print(a1.alive)
print(a2.fed)
a1.eat(p1)
a2.eat(p2)
print(a1.alive)
print(a2.fed)