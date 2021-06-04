from __future__ import annotations


class Stack:
    def __init__(self):
        self.digits: list = []

    def is_empty(self) -> bool:
        return self.digits == []

    def add(self, digit: int) -> None:
        self.digits.append(digit)

    def withdraw(self) -> int:
        return self.digits.pop()

    def print_digit(self) -> None:
        for digit in self.digits:
            print(digit, end="")


def set_first(stack: Stack, number: int) -> None:
    if stack.is_empty():
        stack.add(number)
    else:
        spare: int = stack.withdraw()
        set_first(stack, number)
        stack.add(spare)


def upend(stack: Stack) -> None:
    if not stack.is_empty():
        spare: int = stack.withdraw()
        upend(stack)
        set_first(stack, spare)


def main():
    stack = Stack()
    numbers: str = input("Führen Sie eine beliebige Zahl ein: ")

    try:
        for digit in numbers:
            stack.add(int(digit))
        upend(stack)
        print(numbers, "—►", end=" ")
        stack.print_digit()
    except ValueError:
        print("Es ist keine Zahl :(")


if __name__ == '__main__':
    main()
