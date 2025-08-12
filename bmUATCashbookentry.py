from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException,TimeoutException
from datetime import datetime
import time
import os
from utils import get_screenshot_path

driver = webdriver.Chrome()
driver.get("https://uat-bm.lightmicrofinance.com/index.php")
driver.maximize_window()
driver.implicitly_wait(10)

#login to the dashboard
driver.find_element(By.ID,"inputUsername").click()
driver.find_element(By.NAME,"inputUsername").send_keys("BMT1008")
driver.find_element(By.ID,"inputPassword").click()
driver.find_element(By.NAME,"inputPassword").send_keys("Light@123")
driver.find_element(By.XPATH,"//button[@type='submit']").click()
time.sleep(11)
#expand the Cashbook section
driver.find_element(By.XPATH,"//span[normalize-space()='Digital Cashbook']").click()
time.sleep(4)
#click on the Digical Cashbook module
driver.find_element(By.XPATH,"//a[normalize-space()='Cashbook Entries']").click()
time.sleep(4)
# Switch to iframe
#WebDriverWait(driver, 10).until(EC.frame_to_be_available_and_switch_to_it((By.ID, "link")))
#click on the Submit button
driver.find_element(By.ID,"submitBtn").click()
driver.implicitly_wait(4)
#click on the Cashbook section
driver.find_element(By.XPATH,"//body//div[@class='wrapper']//div[@class='col-md-12']//div[@class='col-md-12']//div[1]//div[2]//div[1]").click()
#click on the Fund Transfer field
driver.find_element(By.XPATH,"//input[@name='DR-20009']").click()
driver.find_element(By.XPATH,"//input[@name='DR-20009']").send_keys("1400")
#click on the text field
driver.find_element(By.XPATH,"//textarea[@name='Remark-Debit-20009']").click()
driver.find_element(By.XPATH,"//textarea[@name='Remark-Debit-20009']").send_keys("Test Auto")
#click on the Credit Section field
driver.find_element(By.XPATH,"//input[@name='CR-D-56489utt_test']").click()
driver.find_element(By.XPATH,"//input[@name='CR-D-56489utt_test']").send_keys("1400")
#click on the text field
driver.find_element(By.XPATH,"//textarea[@name='Remark-Credit-D-56489utt_test']").click()
driver.find_element(By.XPATH,"//textarea[@name='Remark-Credit-D-56489utt_test']").send_keys("Test Auto 1")
time.sleep(3)

#scroll the page down
scroll_pause_time = 1  # Pause time between scrolls
scroll_height = driver.execute_script("return document.body.scrollHeight")

current_position = 0
increment = 500  # Number of pixels to scroll each time

while current_position < scroll_height:
    driver.execute_script(f"window.scrollTo(0, {current_position});")
    time.sleep(scroll_pause_time)
    current_position += increment
    scroll_height = driver.execute_script("return document.body.scrollHeight")  # update in case it changes

# Optional: Scroll to bottom one last time
driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")

#click on the Calculate Button
driver.find_element(By.ID,"calculateBtn").click()
time.sleep(2)
#click on the Denomination Button
driver.find_element(By.XPATH,"//button[@id='denominationBtn']").click()
#click on the popup
driver.find_element(By.XPATH,"/html/body/div[1]/div/section/div[1]/div/div/div/div[2]/div/div/form/div/table/thead/tr/th").click()
#erase
#input_field = driver.find_element(By.XPATH, "/html/body/div[1]/div/section/div[1]/div/div/div/div[2]/div/div/form/div/table/tbody/tr[4]/td[2]/input")
# Clear the existing data
#input_field.clear()
# Optional: enter new data
#input_field.send_keys("9")
#click on one field and add the data
driver.find_element(By.ID,"cashMultiples_3").click()
driver.find_element(By.ID,"cashMultiples_3").send_keys("9")
#click on the disable field
driver.find_element(By.XPATH,"/html/body/div[1]/div/section/div[1]/div/div/div/div[2]/div/div/form/div/table/tbody/tr[4]/td[3]/input").click()
#click on the Close Icon
#driver.find_element(By.XPATH,"/html/body/div[1]/div/section/div[1]/div/div/div/div[1]/div/button").click()
time.sleep(2)
#click on the Submit button in the popup
driver.find_element(By.ID,"submitDenomination").click()
time.sleep(5)

#click on the final Submit button
driver.find_element(By.ID,"cashbookEntryBtn").click()
#alert accept
WebDriverWait(driver, 11).until(EC.alert_is_present())
alert = driver.switch_to.alert
print(alert.text)
alert.accept()
time.sleep(5)
print("Branch cashbook data is submitted successfully")
#click on the logout button
driver.find_element(By.XPATH,"//a[normalize-space()='Sign out']").click()
print("the bm dashboard is successfully logout")
