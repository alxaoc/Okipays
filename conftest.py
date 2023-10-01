import pytest
from selenium import webdriver


# Цей фікстур допоможе ініціалізувати і закрити драйвер браузера перед кожним тестом
@pytest.fixture(scope="function")
def driver_fixture():
    driver = webdriver.Chrome()
    # Встановлюємо розмір вікна (ширина x висота)
    driver.set_window_size(1512, 982)
    yield driver
    driver.quit()
