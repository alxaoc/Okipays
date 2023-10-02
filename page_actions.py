from selenium import webdriver


# Домен для використання у всіх тестах
domain = 'https://okipays.com'

# Функція для ініціалізації драйвера
def initialize_driver():
    driver = webdriver.Chrome()
    driver.set_window_size(1512, 982)
    return driver


# Функція для відкриття сторінки за URL
def open_page(driver, url):
    driver.get(url)
