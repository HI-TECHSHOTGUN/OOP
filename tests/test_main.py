import pytest
from main import Category


@pytest.fixture(autouse=True)
def reset_counts():
    Category.category_count = 0
    Category.product_count = 0


def test_product_initialization(sample_product):
    assert sample_product.name == "Test Product"
    assert sample_product.description == "Test Description"
    assert sample_product.price == 20
    assert sample_product.quantity == 10


def test_category_initialization(sample_category, sample_product):
    assert sample_category.name == "Test Category"
    assert sample_category.description == "Test Category Description"
    assert sample_category.products == [sample_product]
    assert Category.category_count == 1
    assert Category.product_count == 1


def test_category_count_multiple_categories(sample_product):
    Category("Category 1", "Description 1", [sample_product])
    Category("Category 2", "Description 2", [sample_product])
    assert Category.category_count == 2


def test_product_count_multiple_products(sample_product, sample_product2):
    Category("Category 1", "Description 1", [sample_product, sample_product2])
    assert Category.product_count == 2

def test_product_count_multiple_categories_and_products(sample_product, sample_product2):
     Category("Category 1", "Description 1", [sample_product])
     Category("Category 2", "Description 2", [sample_product, sample_product2])
     assert Category.product_count == 3