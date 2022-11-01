from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait


class BaseDriver:
    def __init__(self, driver):
        self.driver = driver

    def wait_for_element_to_be_clickable(self, locator_type, locator):
        wait = WebDriverWait(self.driver, 10)
        element = wait.until(EC.element_to_be_clickable((locator_type, locator)))
        return element
    def wait_for_prescence_of_all_elements(self, locator_type, locator ):
        wait = WebDriverWait(self.driver, 10)
        list_elements = wait.until(EC.presence_of_all_elements_located((locator_type, locator)))
        return list_elements
    def pagetitle(self):
        title1 = self.driver.title
        return title1
    def screenshot(self,location):
        screeshot = self.driver.save_screenshot(location)
        return screeshot
    def switchToFrame(self,locator):
        iframe = self.driver.switch_to.frame(locator)
        return iframe
    def findelement(self,locater_type,locator):
        f = self.driver.find_element(locater_type,locator)
        return f



