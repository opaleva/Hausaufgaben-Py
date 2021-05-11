class Product:
    def __init__(self, name: str, price: float, available: int):
        self.name = name
        self.price = price
        self.available = available

    def __repr__(self) -> str:
        return f'{self.name}: {self.price} руб., {self.available} шт.'


class Order:
    def __init__(self):
        self.order = {}

    def add_item(self, name: str, number: int) -> None:
        self.order[name] = number

    def __repr__(self) -> str:
        return f'{self.order}'

    def __str__(self) -> str:
        return f'{self.order}'


class ProductExpert:
    def __init__(self, *products: Product):
        self.products = list(products)
        self.sales = Sale()

    def add_product(self, name: str, price: float, available: int) -> None:
        self.products.append(Product(name, price, available))

    def remove_product(self, name: str) -> None:
        for product in self.products:
            if product.name.lower() == name.lower():
                self.products.remove(product)

    def enroll_sale(self, order: Order):
        self.sales.add_sale(order)

    def print_products(self):
        print("В наличии: ")
        for product in self.products:
            print(product)

    def print_sales(self):
        print(f'Продано: {self.sales}')


class Client:
    def __init__(self, expert: ProductExpert):
        self.expert = expert

    def create_order(self):
        order = Order()
        while True:
            item: str = input("Название продукта: (enter для выхода)")
            if item == "":
                break
            number: int = int(input("Количество: "))
            order.add_item(item.lower(), number)


        self.expert.enroll_sale(order)


class Sale:
    def __init__(self):
        self.sales: list = []

    def add_sale(self, order: Order) -> None:
        self.sales.append(order)

    def __str__(self) -> str:
        return " ".join(str(sale) for sale in self.sales)


def main():
    kamerad_1 = ProductExpert()
    kunde = Client(kamerad_1)

    kamerad_1.add_product("etwas", 10, 10)
    kamerad_1.add_product("noch etwas", 20, 20)
    kamerad_1.add_product("und etwas anderes", 30, 5)

    kunde.create_order()

    kamerad_1.print_products()
    kamerad_1.print_sales()


if __name__ == '__main__':
    main()
