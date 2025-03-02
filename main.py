class Product:
    name: str
    description: str
    price: int
    quantity: int

    def __init__(self, name, description, price, quantity):
        self.name = name
        self.description = description
        self.__price = price
        self.quantity = quantity

    def __str__(self):
        return f'{self.name}, {self.price} руб. Остаток: {self.quantity} шт.'

    def __add__(self, other):
        return self.quantity * self.price + other.quantity * other.price

    @classmethod
    def new_product(cls, _dict):
        try:
            name = _dict['name']
            description = _dict['description']
            price = _dict['price']
            quantity = _dict['quantity']
            return cls(name, description, price, quantity)
        except KeyError as e:
            return f"KeyError: {e}"

    @property
    def price(self):
        return self.__price

    @price.setter
    def price(self, new_price):
        if new_price > 0:
            self.__price = new_price
        else:
            print("Цена не должна быть нулевая или отрицательная")


class Category:
    name: str
    description: str
    products: list
    category_count = 0
    product_count = 0

    def __init__(self, name, description, products=None):
        self.name = name
        self.description = description
        self.__products = products if products else []
        Category.category_count += 1
        Category.product_count += len(self.__products) if products else 0

    def __str__(self):
        total_quantity = sum(i.quantity for i in self.__products)
        return f'{self.name}, количество продуктов: {total_quantity} шт.'

    def add_product(self, product):
        if isinstance(product, Product):
            self.__products.append(product)
            Category.product_count += 1
        else:
            print('Можно добавлять только объекты класса Product.')

    @property
    def products(self):
        result = ''
        for i in self.__products:
            result += f'{i.name}, {i.price} руб. Остаток: {i.quantity} шт. '
        return result


if __name__ == '__main__':
    product1 = Product("Samsung Galaxy S23 Ultra", "256GB, Серый цвет, 200MP камера", 180000.0, 5)
    product2 = Product("Iphone 15", "512GB, Gray space", 210000.0, 8)
    product3 = Product("Xiaomi Redmi Note 11", "1024GB, Синий", 31000.0, 14)

    print(str(product1))
    print(str(product2))
    print(str(product3))

    category1 = Category(
        "Смартфоны",
        "Смартфоны, как средство не только коммуникации, но и получения дополнительных функций для удобства жизни",
        [product1, product2, product3]
    )

    print(str(category1))

    print(category1.products)

    print(product1 + product2)
    print(product1 + product3)
    print(product2 + product3)
