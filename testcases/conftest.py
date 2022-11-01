import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.edge.service import Service
from webdriver_manager.microsoft import EdgeChromiumDriverManager


@pytest.fixture(scope="class")
def setup(request):
    ser_obj = Service(EdgeChromiumDriverManager().install())
    driver = webdriver.Edge(service=ser_obj)
    #wait = WebDriverWait(driver, 10)
    driver.get("https://www.makemytrip.com")
    driver.maximize_window()
    request.cls.driver = driver
    #request.cls.wait = wait
    yield
    driver.close()
