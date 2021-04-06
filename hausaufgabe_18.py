class Vehicle:
    def __init__(self):
        self.working_engine = True  # во избежание путаницы с условиями заменено с False

    def start(self):
        if not self.working_engine:
            self.working_engine = True
            print("Двигатель заведен")

    def move(self):
        if self.working_engine:
            print("Средство передвижения едет")

    def stop(self):
        if self.working_engine:
            self.working_engine = False
            print("Двигатель остановлен")


class Tank(Vehicle):
    def __init__(self):
        super().__init__()
        self.count_ammo = 10

    def move(self):
        if self.working_engine:
            print("Гусеницы заскрипели от движения")
        else:
            print("Нужно завести двигатель")

    def shoot(self):
        if self.count_ammo > 0:
            print("Танк выстрелил")
            self.count_ammo -= 1
        else:
            print("Снаряды кончились")


class Car(Vehicle):
    def __init__(self):
        super().__init__()
        self.fuel = 100

    def start(self):
        if not self.working_engine:
            if self.fuel > 0:
                self.working_engine = True
                print("Двигатель машины заведён")
                if self.fuel < 10:
                    print("Недостаточно бензина для движения")
            else:
                print("Бензина нет")

    def move(self):
        if self.working_engine:  # в цикле, т.к. расход должен уменьшаться не разово
            while self.fuel >= 10:  # так как при < 10 self.fuel -= 10 не может быть реализован
                print("Машина поехала")
                self.fuel -= 10
            else:
                self.working_engine = False
                print("Машина заглохла")
        else:
            print("Машина не заведена")


class Boat(Vehicle):
    def __init__(self):
        super().__init__()
        self.air_pressure = 100

    def start(self):
        if self.air_pressure > 0:
            if not self.working_engine:
                self.working_engine = True
                print("Мотор лодки гудит")
                if self.air_pressure < 10:
                    print("Недостаточно давления для движения")
        else:
            print("Лодка тонет!")
            self.working_engine = False

    def move(self):
        if self.working_engine:  # –//– (как в Car.move() )
            while self.air_pressure >= 10:
                print("Лодка плывёт")
                self.air_pressure -= 10
            else:
                self.working_engine = False
                print("Лодка заглохла")
        else:
            print("Мотор лодки не заведен")
