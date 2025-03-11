from pyexpat.errors import messages

import pytest

from main import Category, LawnGrass, Product, Smartphone


def test_product_creation():
    product = Product("Test Product", "Test Description", 100, 10)
    assert product.name == "Test Product"
    assert product.description == "Test Description"
    assert product.price == 100
    assert product.quantity == 10


def test_product_price_setter_valid():
    product = Product("Test Product", "Test Description", 100, 10)
    product.price = 150
    assert product.price == 150


def test_product_price_setter_invalid(capsys):
    product = Product("Test Product", "Test Description", 100, 10)
    product.price = -50
    captured = capsys.readouterr()
    assert (
        captured.out.split("\n")[-2] == "Цена не должна быть нулевая или отрицательная"
    )
    assert product.price == 100


def test_product_new_product_from_dict_valid():
    data = {
        "name": "Dict Product",
        "description": "Dict Description",
        "price": 200,
        "quantity": 5,
    }
    product = Product.new_product(data)
    assert isinstance(product, Product)
    assert product.name == "Dict Product"
    assert product.description == "Dict Description"
    assert product.price == 200
    assert product.quantity == 5


def test_product_new_product_from_dict_invalid():
    data = {"name": "Dict Product", "description": "Dict Description", "quantity": 5}
    product = Product.new_product(data)
    assert "KeyError" in product


def test_category_creation():
    category = Category("Test Category", "Test Category Description")
    assert category.name == "Test Category"
    assert category.description == "Test Category Description"
    assert category.products == ""
    assert Category.category_count == 1
    assert Category.product_count == 0


def test_category_add_product():
    category = Category("Test Category", "Test Category Description")
    product1 = Product("Product 1", "Desc 1", 50, 20)
    category.add_product(product1)
    assert product1.name in category.products
    assert Category.product_count == 1
    assert "Product 1, 50 руб. Остаток: 20 шт." in category.products


def test_category_with_products_creation():
    product1 = Product("Product 1", "Desc 1", 50, 20)
    product2 = Product("Product 2", "Desc 2", 75, 15)
    Category.category_count = 0
    Category.product_count = 0
    category = Category("Category with Products", "Description", [product1, product2])
    assert Category.product_count == 2
    assert product1.name in category.products
    assert product2.name in category.products
    assert "Product 1, 50 руб. Остаток: 20 шт." in category.products
    assert "Product 2, 75 руб. Остаток: 15 шт." in category.products
    assert (
        category.products
        == "Product 1, 50 руб. Остаток: 20 шт. Product 2, 75 руб. Остаток: 15 шт. "
    )


def test_product_str():
    product = Product("Молоко", "Молоко 3,2%", 80, 15)
    assert str(product) == "Молоко, 80 руб. Остаток: 15 шт."

    with pytest.raises(ValueError):
        product2 = Product("Хлеб", "Хлеб дарницкий", 30, 0)

    product3 = Product("Яблоки", "Яблоки голандские", 50, 100)
    assert str(product3) == "Яблоки, 50 руб. Остаток: 100 шт."


def test_product_add():
    product1 = Product("Молоко", "Молоко 3,2%", 80, 15)
    product2 = Product("Хлеб", "Хлеб дарницкий", 30, 20)
    assert product1 + product2 == 15 * 80 + 20 * 30 == 1800

    product3 = Product("Яблоки", "", 50, 10)
    product4 = Product("Груши", "", 70, 5)
    assert product3 + product4 == 10 * 50 + 5 * 70 == 850

    with pytest.raises(ValueError):
        product5 = Product("Бананы", "бананы узбекистанские", 40, 0)


def test_category_str_single_product():
    product = Product("Яблоки", "яблоки сердобские", 50, 10)
    category = Category("Фрукты", "Фрукты содержат много витамин", [product])
    assert str(category) == "Фрукты, количество продуктов: 10 шт."


def test_category_str_with_zero_quantity_products():
    product1 = Product("Вода", "вода негазированная", 20, 5)
    product2 = Product("Сок яблочный", "натуральный сок", 50, 2)
    category = Category("Напитки", "Напитки газ/негаз, соки", [product1, product2])
    assert str(category) == "Напитки, количество продуктов: 7 шт."

    with pytest.raises(ValueError):
        product3 = Product("Сок яблочный", "натуральный сок", 50, 0)


def test_add_two_products():
    product1 = Product("Product A", "Desc A", 10, 2)
    product2 = Product("Product B", "Desc B", 5, 3)
    assert product1 + product2 == 35


def test_add_zero_price():
    product1 = Product("Product A", "Desc A", 0, 2)
    product2 = Product("Product B", "Desc B", 5, 3)
    assert product1 + product2 == 15


def test_add_same_product():
    product1 = Product("Product A", "Desc A", 10, 2)
    assert product1 + product1 == 40


def test_add_different_type():
    product1 = Product("Product A", "Desc A", 10, 2)
    with pytest.raises(TypeError):
        product1 + 5


def test_add_none():
    product1 = Product("Product A", "Desc A", 10, 2)
    with pytest.raises(TypeError):
        product1 + None


def test_add_string():
    product1 = Product("Product A", "Desc A", 10, 2)
    with pytest.raises(TypeError):
        product1 + "string"


def test_price_setter_valid():
    product = Product("Product E", "Desc E", 10, 1)
    product.price = 15
    assert product.price == 15


def test_lawngrass_creation():
    grass = LawnGrass(
        "Kentucky Bluegrass", "Fine-bladed turf", 20, 10, "USA", "14-21 days", "Green"
    )
    assert grass.name == "Kentucky Bluegrass"
    assert grass.description == "Fine-bladed turf"
    assert grass.price == 20
    assert grass.quantity == 10
    assert grass.country == "USA"
    assert grass.germination_period == "14-21 days"
    assert grass.color == "Green"


def test_add_two_lawngrasses():
    grass1 = LawnGrass(
        "Festuca", "Drought-tolerant", 25, 5, "Canada", "7-10 days", "Dark Green"
    )
    grass2 = LawnGrass(
        "Ryegrass", "Fast-growing", 15, 12, "UK", "10-14 days", "Light Green"
    )
    total_cost = grass1 + grass2  # Используем оператор +
    assert total_cost == (25 * 5) + (15 * 12)  # 125 + 180 = 305


def test_add_lawngrass_and_product():
    grass = LawnGrass(
        "Tall Fescue", "Shade-tolerant", 18, 8, "Germany", "10-14 days", "Green"
    )
    product = Product("Fertilizer", "Lawn fertilizer", 30, 1)
    with pytest.raises(TypeError):
        grass + product  # Используем оператор +


def test_add_lawngrass_and_other_type():
    grass = LawnGrass(
        "Tall Fescue", "Shade-tolerant", 18, 8, "Germany", "10-14 days", "Green"
    )
    with pytest.raises(TypeError):
        grass + 5  # Используем оператор +


def test_add_lawngrass_and_none():
    grass = LawnGrass(
        "Tall Fescue", "Shade-tolerant", 18, 8, "Germany", "10-14 days", "Green"
    )
    with pytest.raises(TypeError):
        grass + None


def test_smartphone_creation():
    smartphone = Smartphone(
        "iPhone 14",
        "A great phone",
        1000,
        1,
        "A15",
        "14 Pro Max",
        "256GB",
        "Space Gray",
    )
    assert smartphone.name == "iPhone 14"
    assert smartphone.description == "A great phone"
    assert smartphone.price == 1000
    assert smartphone.quantity == 1
    assert smartphone.efficiency == "A15"
    assert smartphone.model == "14 Pro Max"
    assert smartphone.memory == "256GB"
    assert smartphone.color == "Space Gray"


def test_add_two_smartphones():
    smartphone1 = Smartphone(
        "iPhone 14",
        "A great phone",
        1000,
        2,
        "A15",
        "14 Pro Max",
        "256GB",
        "Space Gray",
    )
    smartphone2 = Smartphone(
        "Samsung S23",
        "Another great phone",
        900,
        3,
        "Snapdragon 8 Gen 2",
        "S23 Ultra",
        "512GB",
        "Black",
    )
    sum_smartphone = smartphone1 + smartphone2
    assert sum_smartphone == 4700


def test_add_smartphone_and_product():
    smartphone = Smartphone(
        "iPhone 14",
        "A great phone",
        1000,
        2,
        "A15",
        "14 Pro Max",
        "256GB",
        "Space Gray",
    )
    product = Product("Charger", "Phone charger", 50, 1)
    with pytest.raises(TypeError):
        smartphone + product


def test_add_smartphone_and_other_type():
    smartphone = Smartphone(
        "iPhone 14",
        "A great phone",
        1000,
        2,
        "A15",
        "14 Pro Max",
        "256GB",
        "Space Gray",
    )
    with pytest.raises(TypeError):
        smartphone + 5


def test_add_smartphone_and_none():
    smartphone = Smartphone(
        "iPhone 14",
        "A great phone",
        1000,
        2,
        "A15",
        "14 Pro Max",
        "256GB",
        "Space Gray",
    )
    with pytest.raises(TypeError):
        smartphone + None


def test_print_mixin(capsys):
    Product("Сок яблочный", "натуральный сок", 50, 1)
    message = capsys.readouterr()
    assert message.out.strip() == "Product(Сок яблочный, натуральный сок, 50, 1)"
