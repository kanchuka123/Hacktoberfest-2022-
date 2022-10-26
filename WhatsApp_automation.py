from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time

driver=webdriver.Chrome(r"C:.............\anaconda3\chromedriver")

driver.get("https://web.whatsapp.com")
wait=WebDriverWait(driver,600)
target='"contact name"'
string="message that you want to send"
x_arg='//span[contains(@title,'+ target+ ')]'
target=wait.until(EC.presence_of_element_located((By.XPATH ,x_arg)))
target.click()

input_box=driver.find_element_by_class_name('p3_M1')
for i in range(500):
    input_box.send_keys(string+Keys.ENTER)
