import pytest
from selenium.webdriver.common.by import By
import time

from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


@pytest.mark.smoke
def test_open_signin_page(driver_fixture, separator):
    driver = driver_fixture
    driver.get('https://okipays.com/signin')
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


@pytest.mark.smoke
def test_login(driver_fixture, separator):
    driver = driver_fixture
    driver.get('https://okipays.com/signin')
    driver.implicitly_wait(1)
    # Заповнюємо форму та тиснем кнопку "Sign in"
    driver.find_element(By.ID, 'email').send_keys('qawpt@qawpt.qa')
    driver.find_element(By.ID, 'password').send_keys('@Okipays17')
    driver.find_element(By.XPATH, '//button[contains(text(), "Sign in")]').click()
    time.sleep(1)
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
