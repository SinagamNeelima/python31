import time

import selenium
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

driver =selenium.webdriver.Chrome()
driver.get("https://rahulshettyacademy.com/AutomationPractice/")
drp=Select(driver.find_element(By.NAME,"dropdown-class-example"))
drp.select_by_value("option2")
time.sleep(5)