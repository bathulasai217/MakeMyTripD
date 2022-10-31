from selenium.webdriver.common.by import By
import time

from base.base_driver import BaseDriver


class LaunchPage(BaseDriver):
    text_departfrom_CSS = "input#fromCity"
    text_departfrom_search_Xpath = "//input[@placeholder='From']"
    text_departfrom_select_XPATH = "li#react-autowhatever-1-section-0-item-0"

    text_goingto_search_XPATH = "//input[@placeholder='To']"
    text_gointto_select_CSS = "li#react-autowhatever-1-section-0-item-0"

    text_select_date_CSS = "div.DayPicker-Caption>div"
    text_date_month = "November 2022"
    text_date = 'Thu Nov 24 2022'
    text_date_mon_year  = "//div[contains(@aria-label,{0})]"
    text_date_mon_year_XPATH = text_date_mon_year.format(text_date)
    text_next_mon_XPATH = "//span[@aria-label='Next Month']"
    text_studentfare_CSS = "ul.specialFareNew>li:nth-child(3)"
    text_searcgbutton_XPATH = "//a[@class='primaryBtn font24 latoBold widgetSearchBtn ']"

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver
        # self.wait =wait

    def departfrom(self, departlocation):
        self.wait_for_element_to_be_clickable(By.CSS_SELECTOR, self.text_departfrom_CSS).click()
        self.wait_for_element_to_be_clickable(By.XPATH, self.text_departfrom_search_Xpath).send_keys(departlocation)
        time.sleep(1)
        self.wait_for_element_to_be_clickable(By.CSS_SELECTOR, self.text_departfrom_select_XPATH).click()

    def goingto(self, destinylocation):
        # self.wait.until(EC.element_to_be_clickable((By.XPATH, "//input[@placeholder='To']"))).send_keys(destinylocation)
        self.wait_for_element_to_be_clickable(By.XPATH, self.text_goingto_search_XPATH).send_keys(destinylocation)
        time.sleep(1)
        # self.wait.until(
        #     EC.element_to_be_clickable((By.CSS_SELECTOR, "li#react-autowhatever-1-section-0-item-0"))).click()
        self.wait_for_element_to_be_clickable(By.CSS_SELECTOR, self.text_gointto_select_CSS).click()
        time.sleep(1)

    def selectdate(self,):
        # month_year = self.wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, "div.DayPicker-Caption>div")))
        month_year = self.wait_for_element_to_be_clickable(By.CSS_SELECTOR, self.text_select_date_CSS)
        try:

            for c in range(12):
                time.sleep(2)
                if month_year.text == self.text_date_month:
                    time.sleep(1)
                    # self.driver.find_element(By.XPATH, "//div[contains(@aria-label,'Thu Nov 24 2022')]").click()
                    self.wait_for_element_to_be_clickable(By.XPATH, self.text_date_mon_year_XPATH).click()
                else:
                    # self.driver.find_element(By.XPATH, "//span[@aria-label='Next Month']").click()
                    self.wait_for_element_to_be_clickable(By.XPATH, self.text_next_mon_XPATH).click()
        except:
            print("refresh")

    def selectstudentfare(self):
        # self.driver.find_element(By.CSS_SELECTOR, "ul.specialFareNew>li:nth-child(3)").click()
        self.wait_for_element_to_be_clickable(By.CSS_SELECTOR, self.text_studentfare_CSS).click()

    def clickonsearch(self):
        self.driver.find_element(By.XPATH, self.text_searcgbutton_XPATH).click()
    def searchFlights(self,departlocation,goiningtolocation):
        self.departfrom(departlocation)
        self.goingto(goiningtolocation)