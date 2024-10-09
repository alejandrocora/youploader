import os
from seleniumbase import Driver
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.firefox.options import Options as firefox_Options


def wait_return(driver, xpath, is_one, is_clickable, delay):
    if is_clickable:
        WebDriverWait(driver, delay).until(EC.element_to_be_clickable((By.XPATH, xpath)))
    else:
        WebDriverWait(driver, delay).until(EC.presence_of_element_located((By.XPATH, xpath)))
    if is_one:
        return driver.find_element(By.XPATH, xpath)
    else:
        return driver.find_elements(By.XPATH, xpath)


def chrome(mode):
    driver = Driver(uc=True, headed=mode)
    driver.set_window_size(1200, 760)
    return driver


def firefox(mode):
    options = firefox_Options()
    if mode:
        options.add_argument('--headless')
    options.add_argument("user-agent=Mozilla/5.0 (X11; Linux x86_64; rv:105.0) Gecko/20100101 Firefox/105.0")
    options.add_argument("--window-size=1280,800")
    driver = webdriver.Firefox(options=options)
    return driver