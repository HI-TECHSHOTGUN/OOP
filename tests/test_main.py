import pytest
from main import Product, Category

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
    assert captured.out == "Цена не должна быть нулевая или отрицательная\n"
    assert product.price == 100

def test_product_new_product_from_dict_valid():
    data = {"name": "Dict Product", "description": "Dict Description", "price": 200, "quantity": 5}
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
    assert category.products == ''
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
    assert category.products == 'Product 1, 50 руб. Остаток: 20 шт. Product 2, 75 руб. Остаток: 15 шт. '