from pages.base_page import BasePage


class SignInPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)

    def open(self, url):
        self.driver.get(url)

    def open_page(self, domain):
        signin_url = domain + '/signin'
        self.driver.get(signin_url)
