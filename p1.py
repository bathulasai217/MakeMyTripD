import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
serv_obj = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=serv_obj)
driver.get("https://www.makemytrip.com/")
driver.maximize_window()
driver.switch_to.frame("notification-frame-~55852cba")
print(driver.title)

driver.find_element(By.ID,"webklipper-publisher-widget-container-notification-close-div").click()
time.sleep(3)
driver.find_element(By.XPATH,"//div[@class = 'langCard  fixedCard bounceAni']/span").click()
time.sleep(4)