import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

driver = webdriver.Chrome()
driver.get("https://rahulshettyacademy.com/AutomationPractice/")
radiobuttons = driver.find_elements(By.CSS_SELECTOR,".radioButton")
radiobuttons[2].click()

assert radiobuttons[2].is_selected()