import pytest
from selenium import webdriver

from action.page_actions import initialize_driver


# Цей фікстур допоможе ініціалізувати і закрити драйвер браузера перед кожним тестом
@pytest.fixture(scope='function')
def driver_fixture(all_tests):
    driver = webdriver.Chrome()
    driver.implicitly_wait(2)
    driver.set_window_size(1512, 982)
    yield driver
    driver.quit()


@pytest.fixture(scope="function")
def driver():
    driver = initialize_driver()
    yield driver
    driver.quit()


@pytest.fixture(scope='function')
def separator():
    print('\nTest run...')
    yield
    print('\nTest Finished!')


@pytest.fixture(scope='session')
def all_tests():
    print('\nBefore All')
    yield
    print('After All')
