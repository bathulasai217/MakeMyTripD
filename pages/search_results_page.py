import pytest
import time

from selenium.webdriver.common.by import By

from base.base_driver import BaseDriver


class SearchResults(BaseDriver):
    text_flightname_XPATH = "//p[@class = 'boldFont blackText airlineName']"
    text_depature_time_XPATH = "//div[@class = 'flexOne timeInfoLeft']/p/span"
    text_flghtduratin_XPATH = "//div[@class = 'stop-info flexOne']/p"
    text_studentfareflights = "//font[contains(@color,'#ffffff')][normalize-space()='STUDENT']"
    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver
    def flightname(self):
        flightnames = self.wait_for_prescence_of_all_elements(By.XPATH, self.text_flightname_XPATH)
        return flightnames
    def depaturetime(self):
        depaturetime = self.wait_for_prescence_of_all_elements(By.XPATH, self.text_depature_time_XPATH)
        return depaturetime
    def flightduration(self):
        flightduration = self.wait_for_prescence_of_all_elements(By.XPATH, self.text_flghtduratin_XPATH)
        return flightduration
    def studentfareflight(self):
        studentfareflight = self.wait_for_prescence_of_all_elements(By.XPATH, self.text_studentfareflights)
        return studentfareflight
