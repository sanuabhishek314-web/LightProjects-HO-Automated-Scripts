#Upload Script, Tax Invoice Generation and Upload Utility Modules
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

driver = webdriver.Chrome()
driver.get("https://uat-ho.lightmicrofinance.com/index.php")
driver.maximize_window()
driver.implicitly_wait(10)




# Login
driver.find_element(By.ID, "username").send_keys("LMF09496")
driver.find_element(By.ID, "password").send_keys("Sanuabhishek$#@160897")
driver.find_element(By.ID, "login_button").click()

# Handle alert
WebDriverWait(driver, 11).until(EC.alert_is_present())
alert = driver.switch_to.alert
print(alert.text)
alert.accept()

#select the Upload Script module
driver.find_element(By.XPATH,"//img[contains(@src,'../img/cloud-computing.png')]").click()
time.sleep(3)

# Switch to iframe
WebDriverWait(driver, 10).until(EC.frame_to_be_available_and_switch_to_it((By.ID, "link")))


#click on the bulk CB section
driver.find_element(By.XPATH,'//div[4]//div[2]').click()
time.sleep(2)


#click on the Upload button
csv_path = r"C:\Users\Abhishek Yadav\Pictures\UploadScript\Bulk CB check New.csv"
file_input = WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.ID, "csv")))
file_input.send_keys(csv_path)
# Click Upload & Process button
upload_btn = WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, "//form[@action='bulk_import_cb_check.php']//input[@name='submit']")))
upload_btn.click()
time.sleep(10)
print("CB data is successfully updated")

driver.switch_to.default_content()

#select the Tax Invoice generation module
driver.find_element(By.XPATH,"//img[contains(@src,'../img/invoice.png')]").click()
time.sleep(3)

# Switch to iframe
WebDriverWait(driver, 10).until(EC.frame_to_be_available_and_switch_to_it((By.ID, "link")))

#click on the upload section
driver.find_element(By.XPATH,"/html[1]/body[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[2]").click()
time.sleep(3)
#click on the upload button
file_path = r"C:\Users\Abhishek Yadav\Pictures\UploadScript\InvoiceGenerate.csv"
file_input = WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.ID, "fileInput")))
file_input.send_keys(file_path)
print("Invoice File is being uploaded")

# Click generate invoice button
upload_btn = WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, "//input[@name='submit']")))
upload_btn.click()
time.sleep(10)
print("Invoice Generated successfully")

driver.switch_to.default_content()

#select the upload utility module
driver.find_element(By.XPATH,"//img[@src='../img/uploadutility.png']").click()
time.sleep(3)
# Switch to iframe
WebDriverWait(driver, 10).until(EC.frame_to_be_available_and_switch_to_it((By.ID, "link")))

#click on the bulk file section
driver.find_element(By.XPATH,"//div[@class='section upload-section']").click()
time.sleep(3)
#select the action from the drodpown
wait = WebDriverWait(driver, 20)  #explicit wait
action_dropdown = wait.until(EC.element_to_be_clickable((By.XPATH, "//span[@class='select2-selection select2-selection--single']")))
action_dropdown.click()
search_box = wait.until(EC.presence_of_element_located((By.XPATH, "//input[@class='select2-search__field']")))
search_box.send_keys("Tax Invoice Generation")
search_box.send_keys(Keys.ENTER)
time.sleep(3)

#click on the upload file button
file_path = r"C:\Users\Abhishek Yadav\Pictures\UploadScript\InvoiceGenerate.csv"
file_input = WebDriverWait(driver, 30).until(EC.presence_of_element_located((By.ID, "file")))
file_input.send_keys(file_path)
time.sleep(2)

#click on the Upload file button
driver.find_element(By.ID,"upload-file").click()
time.sleep(9)
print("Invoice being generated successfully")

#alert accept
WebDriverWait(driver, 11).until(EC.alert_is_present())
alert = driver.switch_to.alert
print(alert.text)
alert.accept()
time.sleep(7)

#click on the Search section
driver.find_element(By.XPATH,"/html[1]/body[1]/div[2]/div[2]/div[2]").click()
time.sleep(3)
#click on the search field
driver.find_element(By.XPATH,"//input[@type='search']").click()
driver.find_element(By.XPATH,"//input[@type='search']").send_keys("LMF09496")
time.sleep(3)
print("Data is filtered")
#assert the filter data
expected_value = "LMF09496"
actual_value = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH,"/html/body/div[2]/div[2]/div[2]/table/tbody/tr[1]/td[6]"))).text.strip()

assert actual_value == expected_value, f"Expected {expected_value} but got {actual_value}"
print("Expected Value:",expected_value)
time.sleep(3)


driver.switch_to.default_content()



driver.save_screenshot('full_page.png')
print("Screenshot is captured successfully")
# Logout
WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//a[normalize-space()='Logout']"))).click()

print("Ho Dashboard is successfully logged out")