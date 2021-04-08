class Counter:
    def __init__(self, first, last):
        self.current = 0
        self.first = first
        self.last = last

    def augmentation(self):
        for self.current in range(self.first, self.last + 2):  # с превышением верхнего значения
            if self.current > self.last:
                self.current = self.first
            print(self.current)

    def diminution(self):
        for self.current in reversed(range(self.first - 1, self.last + 1)):  # с уменьшенным нижним порогом
            if self.current < self.first:
                self.current = self.last
            print(self.current)

    def get_current(self):
        return self.current


def main():
    c1 = Counter(int(input("Нижний порог: ")), int(input("Верхний порог: ")))

    c1.augmentation()
    print("Текущий:", c1.get_current())
    print("---" * 7)
    c1.diminution()
    print("Текущий:", c1.get_current())


if __name__ == '__main__':
    main()
