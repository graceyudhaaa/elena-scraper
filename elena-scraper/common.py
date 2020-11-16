import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from settings import username, password, PATH

#setup webdriver
driver = webdriver.Chrome(PATH)
#set time out 60 seconds
driver.wait = WebDriverWait(driver, 60)

def click(selector, By):
    driver.wait.until(
        EC.element_to_be_clickable((By, selector))
    ).click()

def send_keys(keys, selector, By):
    driver.wait.until(
        EC.element_to_be_clickable((By, selector))
    ).send_keys(keys)

