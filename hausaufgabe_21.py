from abc import ABC, abstractmethod


class Character(ABC):
    def __init__(self, name, weight, weapon):
        self.name = name
        self.weight = weight
        self.weapon = weapon

    @abstractmethod
    def overeat(self):
        ...

    @abstractmethod
    def search_more(self):
        ...


class FirstEater(Character):
    def __init__(self, name, weight, weapon):
        super().__init__(name, weight, weapon)

    def overeat(self):
        i = 0
        while True:
            i += 1
            self.weight += 2
            if self.weight > 200:
                print(f'{self.name} лопнул от переедания, съев {i}{self.weapon.overeat()}')
                break

    def search_more(self):
        self.weapon.search_more()


class SecondEater(Character):
    def __init__(self, name, weight, weapon):
        super().__init__(name, weight, weapon)

    def overeat(self):
        i = 0
        while True:
            i += 1
            self.weight += 1
            if self.weight > 200:
                print(f'{self.name} лопнул от переедания, съев {i}{self.weapon.overeat()}')
                break

    def search_more(self):
        self.weapon.search_more()


class Bakery(ABC):
    def __init__(self, pieces):
        self.pieces = pieces

    @abstractmethod
    def overeat(self):
        ...

    @abstractmethod
    def search_more(self):
        ...


class Cake(Bakery):
    def __init__(self, pieces):
        super().__init__(pieces)

    def overeat(self):
        print('Поглощает торты.')
        self.pieces -= 1
        return f' кусков торта.'

    def search_more(self):
        self.pieces = 100
        print('Запас тортов пополнен.')


class Bun(Bakery):
    def __init__(self, pieces):
        super().__init__(pieces)

    def overeat(self):
        print('Кушает булочки.')
        self.pieces -= 1
        return f' булочек.'

    def search_more(self):
        self.pieces = 100
        print('Запас булочек пополнен.')


buns = Bun(100)
cakes = Cake(100)
a = FirstEater('Вася', 45, cakes)
b = SecondEater('Петя', 152, buns)

a.overeat()
a.search_more()
b.overeat()
b.search_more()
