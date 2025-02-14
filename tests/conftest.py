import pytest

from main import Category, Product

"""Фикстуры для тестирования"""


@pytest.fixture
def sample_product():
    return Product("Test Product", "Test Description", 20, 10)


@pytest.fixture
def sample_product2():
    return Product("Another Product", "Another Description", 30, 5)


@pytest.fixture
def sample_category(sample_product):
    return Category("Test Category", "Test Category Description", [sample_product])
