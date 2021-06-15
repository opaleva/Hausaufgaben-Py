from random import seed, randint


class VSState:
    def clean(self):
        ...


class CombinedCleaning(VSState):
    def clean(self):
        print("Пытается убирать кафельные покрытия.".center(100))


class DryCleaning(VSState):
    def clean(self):
        print("Едет по ламинату.".center(99))


class WetCleaning(VSState):
    def clean(self):
        print("Застрял в ковре...".center(99))


class VacuumCleaner:
    def __init__(self):
        self.current_state = False

    def start(self):
        if not self.current_state:
            self.current_state = True
            print("Пылесос поехал.".center(100, "="))

    def move(self, coefficient):
        if self.current_state:
            if 0 <= coefficient < 10:
                CombinedCleaning().clean()
            elif 10 <= coefficient < 20:
                DryCleaning().clean()
            elif coefficient > 20:
                WetCleaning().clean()

    def finish(self):
        if self.current_state:
            self.current_state = False
            print(" Пылесос или сломался, или закончил уборку. ".center(100, "="))


def main():
    seed(7)
    vc = VacuumCleaner()
    vc.start()
    [vc.move(randint(0, 30)) for _ in range(8)]
    vc.finish()


if __name__ == "__main__":
    main()
