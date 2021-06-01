from abc import ABC, abstractmethod


class PastaFactory(ABC):
    @abstractmethod
    def name(self):
        ...

    @abstractmethod
    def add_sauce(self):
        ...

    @abstractmethod
    def add_filling(self):
        ...

    @abstractmethod
    def add_supplements(self):
        ...

    def get_dish(self):
        print(self.name(), self.add_filling(), self.add_sauce(), self.add_supplements(),
              "Danke schön für Ihre Bestellung!")


class NavyPasta(PastaFactory):
    def name(self):
        return " Marinenudeln wurden ausgewählt.\n"

    def add_sauce(self):
        return "Ketchup wurde hinzugefügt.\n"

    def add_filling(self):
        return "Hackfleisch wurde hinzugefügt.\n"

    def add_supplements(self):
        return "Rosmarin und Oregano wurden hinzugefügt.\n\n"


class Carbonara(PastaFactory):
    def name(self):
        return " Carbonara wurde ausgewählt.\n"

    def add_sauce(self):
        return "Carbonara-Sauce wurde hinzugefügt.\n"

    def add_filling(self):
        return "Guanciale wurde hinzugefügt.\n"

    def add_supplements(self):
        return "Käse wurde hinzugefügt.\n\n"


class Lasagne(PastaFactory):
    def name(self):
        return " Lasagne wurde ausgewählt.\n"

    def add_sauce(self):
        return "Bechamelsauce wurde hinzugefügt.\n"

    def add_filling(self):
        return "Ragout mit Hackfleisch wurden hinzugefügt.\n"

    def add_supplements(self):
        return "Parmesan wurde hinzugefügt.\n\n"


def get_pasta(number: int):
    if number == 1:
        return NavyPasta().get_dish()
    if number == 2:
        return Carbonara().get_dish()
    if number == 3:
        return Lasagne().get_dish()
    else:
        print("Bitte wählen Sie aus, was wir haben.")


def main():
    print("Bitte wählen Sie eine Nummer aus:\n1 — Marinenudeln\n2 — Carbonara\n3 — Lasagne")
    get_pasta(int(input("—► ")))


if __name__ == '__main__':
    main()

