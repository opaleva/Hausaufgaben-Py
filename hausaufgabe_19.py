# Описать класс, реализующий счетчик, который работает в заданном диапазоне.
# Он может увеличивать или уменьшать свое значение на единицу.
# Счетчик имеет три метода: увеличение, уменьшение и геттер текущего значения — и поле,
# содержащее его текущее состояние. Если счетчик при увеличении выходит за максимальный
# диапазон, то счетчик обновляется. Если счетчик при умешении выходит за минимальный
# диапазон, то счетчик принимает максимальное значение из своего диапазона.
# Написать программу, демонстрирующую все возможности класса.
class Counter:
    current = 0

    def __init__(self, first, last):
        self.first = first
        self.last = last

    @property
    def augmentation(self):
        if self.current < self.last:
            self.current += 1
            return self.current
        else:
            return self.first

    @property
    def diminution(self):
        if self.current < self.last:
            self.current -= 1
            return self.current
        else:
            return self.last


c1 = Counter(first=0, last=5)

