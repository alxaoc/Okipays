from selenium.webdriver.common.by import By
import time


def test_open_reset_password_page(driver_fixture):
    driver = driver_fixture
    driver.get('https://okipays.com/reset-password')
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
    expected_h2_text = "Forgot password"
    assert actual_h2_text == expected_h2_text, f"Заголовок h2 не співпадає з очікуваним. Очікувано: {expected_h2_text}, Отримано: {actual_h2_text}"

    driver.close()
    driver.quit()
