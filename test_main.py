from selenium.webdriver.common.by import By
import time


def test_open_main_page(driver_fixture):
    driver = driver_fixture
    driver.get('https://okipays.com/')
    driver.implicitly_wait(5)

    try:
        accept_button = driver.find_element(By.XPATH, "//button[contains(text(), 'Accept')]")
        accept_button.click()
    except:
        # Якщо кнопку не знайдено, то ігноруємо помилку і продовжуємо виконання тесту
        pass

    time.sleep(1)

    h1_element = driver.find_element(By.TAG_NAME, 'h1')
    actual_h1_text = h1_element.text
    expected_h1_text = "THE MOST SECURE CRYPTO PAYMENTS"
    assert actual_h1_text == expected_h1_text, f"Заголовок h1 не співпадає з очікуваним. Очікувано: {expected_h1_text}, Отримано: {actual_h1_text}"

    driver.close()
    driver.quit()
