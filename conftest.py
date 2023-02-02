import time
import pytest

from selenium import webdriver
from selenium.webdriver.chrome.options import Options


@pytest.fixture(scope='function')
def driver():
    driver_path = 'webdriver\chromedriver.exe'

    options = Options()

    options.add_argument(r"user-data-dir=C:\Users\Treid Computers\AppData\Local\Google\Chrome\User Data\Default")

    driver = webdriver.Chrome(executable_path=driver_path, options=options)
    time.sleep(1)

    yield driver

    driver.quit()
