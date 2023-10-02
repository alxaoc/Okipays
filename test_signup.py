import pytest
from selenium.webdriver.common.by import By
import time


@pytest.mark.smoke
def test_open_signup_page(driver_fixture, separator):
    driver = driver_fixture
    driver.get('https://okipays.com/signup')
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
    expected_h2_text = "Create an account"
    assert actual_h2_text == expected_h2_text, f"Заголовок h2 не співпадає з очікуваним. Очікувано: {expected_h2_text}, Отримано: {actual_h2_text}"

    driver.close()
    driver.quit()
