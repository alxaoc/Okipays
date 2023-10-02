import pytest
from selenium.webdriver.common.by import By
import time
from decouple import config

from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from page_actions import open_page, domain


@pytest.mark.smoke
def test_open_signin_page(driver, separator):
    open_page(driver, domain + '/signin')
    driver.implicitly_wait(1)

    try:
        accept_button = driver.find_element(By.XPATH, "//button[contains(text(), 'Accept')]")
        accept_button.click()
    except:
        # Якщо кнопку не знайдено, то ігноруємо помилку і продовжуємо виконання тесту
        pass

    time.sleep(1)

    h2_element = driver.find_element(By.TAG_NAME, 'h2')
    actual_h2_text = h2_element.text
    expected_h2_text = "Sign in"
    assert actual_h2_text == expected_h2_text, f"Заголовок h2 не співпадає з очікуваним. Очікувано: {expected_h2_text}, Отримано: {actual_h2_text}"
    driver.quit()


users = ['user1@wpt.dev', 'user2@wpt.dev', 'user3@wpt.dev']
passwords = ['password1', 'password2', 'password3']


def generate_pairs():
    pairs = []
    for user in users:
        for password in passwords:
            pairs.append(pytest.param((user, password), id=f'{user}, {password}'))
    return pairs


# @pytest.mark.parametrize(
#     'creds',
#     [
#         pytest.param(('user1@wpt.dev', 'password1'), id='user1@wpt.dev, password1'),
#         pytest.param(('user2@wpt.dev', 'password2'), id='user2@wpt.dev, password2'),
#         pytest.param(('user3@wpt.dev', 'password3'), id='user3@wpt.dev, password3')
#     ]
# )


@pytest.mark.parametrize('creds', generate_pairs())
def test_login_error(driver, separator, creds):
    login, password = creds
    open_page(driver, domain + '/signin')
    driver.implicitly_wait(1)
    # Заповнюємо форму та тиснем кнопку "Sign in"
    driver.find_element(By.ID, 'email').send_keys(login)
    driver.find_element(By.ID, 'password').send_keys(password)
    driver.find_element(By.XPATH, '//button[contains(text(), "Sign in")]').click()
    time.sleep(2)
    # Очікуємо, поки з'явиться сповіщення (задаємо тайм-аут)
    wait = WebDriverWait(driver, 3)
    notification = wait.until(EC.presence_of_element_located((By.CLASS_NAME, 'toasted')))
    # Отримуємо текст сповіщення
    notification_text = notification.text
    # Очікуваний текст сповіщення
    expected_notification_text = "Email or password is incorrect"
    time.sleep(1)
    # Порівнюємо отриманий текст з очікуваним за допомогою assert
    if expected_notification_text == notification_text:
        print("\nУспіх: Текст сповіщення відповідає очікуваному.")
    else:
        print(
            f"Помилка: Текст сповіщення не відповідає очікуваному. Очікувано: {expected_notification_text}, Отримано: {notification_text}")

    time.sleep(1)
    # Закриваємо веб-сторінку
    driver.quit()


mail = config('EMAIL')
passw = config('PASSWORD')
@pytest.mark.smoke
def test_login_success(driver, separator):
    open_page(driver, domain + '/signin')
    driver.implicitly_wait(1)
    # Заповнюємо форму та тиснем кнопку "Sign in"
    driver.find_element(By.ID, 'email').send_keys(mail)
    driver.find_element(By.ID, 'password').send_keys(passw)
    driver.find_element(By.XPATH, '//button[contains(text(), "Sign in")]').click()
    time.sleep(2)
    # Очікуємо, поки з'явиться сповіщення (задаємо тайм-аут)
    wait = WebDriverWait(driver, 3)
    notification = wait.until(EC.presence_of_element_located((By.CLASS_NAME, 'toasted')))
    # Отримуємо текст сповіщення
    notification_text = notification.text
    # Очікуваний текст сповіщення
    expected_notification_text = "Welcome!"
    time.sleep(1)
    # Порівнюємо отриманий текст з очікуваним за допомогою assert
    if expected_notification_text == notification_text:
        print("\nУспіх: Текст сповіщення відповідає очікуваному.")
    else:
        print(
            f"Помилка: Текст сповіщення не відповідає очікуваному. Очікувано: {expected_notification_text}, Отримано: {notification_text}")

    time.sleep(1)

    try:
        accept_button = driver.find_element(By.XPATH, "//button[contains(text(), 'Accept')]")
        accept_button.click()
    except:
        # Якщо кнопку не знайдено, то ігноруємо помилку і продовжуємо виконання тесту
        pass

    time.sleep(1)
    # Закриваємо веб-сторінку
    driver.quit()
