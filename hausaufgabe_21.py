# --------------------------------------
# На доработке
# --------------------------------------
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
        while True:
            self.weight += 2
            if self.weight > 200:
                print(f'{self.name} лопнул от переедания.')
                break


    def search_more(self):
        self.weapon.search_more()


class SecondEater(Character):
    def __init__(self, name, weight, weapon):
        super().__init__(name, weight, weapon)

    def overeat(self):

        self.weapon.overeat()

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
        ...

    def search_more(self):
        print('123')


class Bun(Bakery):
    def __init__(self, pieces):
        super().__init__(pieces)

    def overeat(self):
        ...

    def search_more(self):
        ...


fg = Cake(130)
a = FirstEater('gfhfg', 180, fg)
a.overeat()
a.search_more()
