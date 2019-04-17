from selenium.webdriver.common.by import By

from tests.acceptance.locators.common_trends_page import CommonTrendsPageLocators
from tests.acceptance.page_model.base_page import BasePage


class CommonTrendsPage(BasePage):

    @property
    def url(self):
        return super(CommonTrendsPage, self).url + '/commontrends'

    # @property
    # def form(self):
    #     return self.driver.find_element(*LoginPageLocators.LOGIN_FORM)
    #
    # @property
    # def submit_button(self):
    #     return self.driver.find_element(*LoginPageLocators.SUBMIT_BUTTON)

    # def form_field(self, name):
    #     return self.form.find_element(By.NAME, name)
