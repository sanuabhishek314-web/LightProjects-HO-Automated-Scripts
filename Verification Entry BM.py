#Client Entry , Loan Entry, Penny drop and Update MObile number
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select
from selenium.webdriver import ActionChains
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

#select the Verification section and click on the Client Entry Verification
driver.find_element(By.XPATH,"/html/body/div[1]/aside/section/ul/li[2]/ul/li[1]/a/span").click()
#select the Client Entry verification
driver.find_element(By.XPATH,"/html/body/div[1]/aside/section/ul/li[2]/ul/li[1]/ul/li[1]/a").click()
time.sleep(2)
#select the staff from the dropdown
wait = WebDriverWait(driver, 15)

# Step 1: Click only the staff dropdown (using its container ID parent)
client_dropdown = wait.until(EC.element_to_be_clickable((By.XPATH, "/html/body/div[1]/div/section/div[1]/div/div/div[2]/div[1]/span/span[1]/span/span[1]")))
client_dropdown.click()
# Step 2: Search for "Ishan Patil"
search_input = wait.until(EC.presence_of_element_located((By.XPATH, "/html/body/span/span/span[1]/input")))
search_input.send_keys("fet1005")
# Step 3: Select the correct option
option = wait.until(EC.element_to_be_clickable((By.XPATH, "//li[contains(text(),'fet1005')]")))
option.click()
time.sleep(4)
print("✅ Staff is being selected successfully.")
#click on the New CLients section
driver.find_element(By.XPATH,"/html/body/div[1]/div/section/div[2]/div/div/div[1]").click()
#click on the Client Image
driver.find_element(By.XPATH,"/html/body/div[1]/div/section/div[2]/div/div/div[1]").click()
time.sleep(3)
#click on the Image popup
wait = WebDriverWait(driver, 20)
# Locate by text
button = wait.until(EC.element_to_be_clickable((By.XPATH, "//button[text()='View Finflux Image']")))
button.click()
time.sleep(4)

#click on the CLose icon
driver.find_element(By.XPATH,"/html/body/div[1]/div/section/div[6]/div/div/div[1]/button").click()
#scroll the gride to the extreme right
wait = WebDriverWait(driver, 10)
# Wait until the table is present
table = wait.until(EC.presence_of_element_located((By.ID, "tablePending")))
# Scroll the table to the extreme right using JavaScript
driver.execute_script("arguments[0].scrollLeft = arguments[0].scrollWidth", table)
# Example: Click on the "Edit" button after scrolling
edit_button = wait.until(EC.element_to_be_clickable((By.XPATH, "/html/body/div[1]/div/section/div[2]/div/div/div[2]/div/table/tbody/tr/td[23]/a")))
edit_button.click()
time.sleep(6)
#click on the clients 1st name
driver.find_element(By.ID,"client_fname").click()
driver.find_element(By.ID,"client_fname").send_keys("Santi")
#Scroll down to the Client KYC section
scroll_pause_time = 1  # Pause time between scrolls
scroll_height = driver.execute_script("return document.body.scrollHeight")

current_position = 0
increment = 50  # Number of pixels to scroll each time

while current_position < scroll_height:
    driver.execute_script(f"window.scrollTo(0, {current_position});")
    time.sleep(scroll_pause_time)
    current_position += increment
    scroll_height = driver.execute_script("return document.body.scrollHeight")
#select the Upload icon
driver.find_element(By.XPATH,"/html/body/div/div/section/div[1]/div[2]/div/form/div[8]/div[5]/input").click()
time.sleep(3)
#click on the Primary KYC popup
driver.find_element(By.XPATH,"/html/body/div[1]/div/section/div[3]/div/div/div[2]/div/div/div/div[1]").click()
#Select the Front KYC upload of client
wait = WebDriverWait(driver, 10)
file_input = wait.until(EC.presence_of_element_located((By.ID, "fileInputAadhaarFront")))
# Make the input element visible
driver.execute_script("arguments[0].style.display = 'block';", file_input)
driver.execute_script("arguments[0].style.visibility = 'visible';", file_input)
driver.execute_script("arguments[0].style.opacity = '1';", file_input)
# Send the file path directly to the input element
file_input.send_keys(r"D:\Images_Test\Edit KYC Image upload\KYC image\aadhaar upload01.jpeg")
# Just to observe the preview update
print("Aadhaar front image is selected successfully")
time.sleep(3)
#Select the Back KYC upload of client
wait = WebDriverWait(driver, 10)
file_input = wait.until(EC.presence_of_element_located((By.ID, "fileInputAadhaarBack")))
# Make the input element visible
driver.execute_script("arguments[0].style.display = 'block';", file_input)
driver.execute_script("arguments[0].style.visibility = 'visible';", file_input)
driver.execute_script("arguments[0].style.opacity = '1';", file_input)
# Send the file path directly to the input element
file_input.send_keys(r"D:\Images_Test\Edit KYC Image upload\KYC image\aadhaar upload02.jpg")
# Just to observe the preview update
print("Aadhaar Back image is selected successfully")
time.sleep(3)
#click on the upload button
driver.find_element(By.XPATH,"/html/body/div[1]/div/section/div[3]/div/div/div[2]/div/div/div/div[2]/form/input[6]").click()
driver.implicitly_wait(8)
print("Addhar data is being masked successfully")
#clickk on the popup
driver.find_element(By.XPATH,"/html/body/div[2]/div[2]/div/div/div/div/div/div/div/div[2]").click()
time.sleep(2)
#click on the close icon
driver.find_element(By.XPATH,"/html/body/div[2]/div[2]/div/div/div/div/div/div/div/div[4]/button").click()
time.sleep(4)
#click on the Front Image Button
driver.find_element(By.ID,"get_front_image").click()
time.sleep(5)
#click on the Back Image Button
driver.find_element(By.ID,"get_back_image").click()
time.sleep(8)

#scroll down to check further
scroll_pause_time = 1  # Pause time between scrolls
scroll_height = driver.execute_script("return document.body.scrollHeight")

current_position = 0
increment = 500  # Number of pixels to scroll each time

while current_position < scroll_height:
    driver.execute_script(f"window.scrollTo(0, {current_position});")
    time.sleep(scroll_pause_time)
    current_position += increment
    scroll_height = driver.execute_script("return document.body.scrollHeight")
#click on the Update button
driver.find_element(By.ID,"submitform").click()
driver.implicitly_wait(13)
print("Data is being updated")
#click on the approve client button
driver.find_element(By.XPATH,"/html/body/div[1]/div/section/div[2]/div/div/div[2]/div/table/tbody/tr/td[24]/button").click()
#Alert accept
WebDriverWait(driver, 10).until(EC.alert_is_present())
alert = driver.switch_to.alert
print(alert.text)
alert.accept()
#alert remove
WebDriverWait(driver, 10).until(EC.alert_is_present())
alert = driver.switch_to.alert
print(alert.text)
alert.accept()
driver.refresh()
driver.implicitly_wait(4)
#select the Loan Verification
driver.find_element(By.XPATH,"/html/body/div[1]/aside/section/ul/li[2]/ul/li[1]/a/span").click()
#select Loan Entry
driver.find_element(By.XPATH,"/html/body/div[1]/aside/section/ul/li[2]/ul/li[1]/ul/li[2]/a").click()
time.sleep(3)
#select the staff from the dropdown
wait = WebDriverWait(driver, 15)

# Step 1: Click only the staff dropdown (using its container ID parent)
client_dropdown = wait.until(EC.element_to_be_clickable((By.XPATH, "/html/body/div[1]/div/section/div[1]/div/div/div[2]/div[1]/span/span[1]/span/span[1]")))
client_dropdown.click()
# Step 2: Search for "fet1005"
search_input = wait.until(EC.presence_of_element_located((By.XPATH, "/html/body/span/span/span[1]/input")))
search_input.send_keys("fet1005")
# Step 3: Select the correct option
option = wait.until(EC.element_to_be_clickable((By.XPATH, "//li[contains(text(),'fet1005')]")))
option.click()
print("Staff is being selected successfully")
time.sleep(4)
#click on the Pending CLient section
driver.find_element(By.XPATH,"/html/body/div[1]/div/section/div[2]/div/div/div[2]/div/table/tbody/tr/td[12]").click()
#scroll the gride to the extreme right
wait = WebDriverWait(driver, 10)
# Wait until the table is present
table = wait.until(EC.presence_of_element_located((By.ID, "tablePending")))
# Scroll the table to the extreme right using JavaScript
driver.execute_script("arguments[0].scrollLeft = arguments[0].scrollWidth", table)
driver.implicitly_wait(3)
#click on the Approve Loan button
driver.find_element(By.XPATH,"/html/body/div[1]/div/section/div[2]/div/div/div[2]/div/table/tbody/tr/td[13]/button").click()
print("Loan has being approved successfully")
#Alert accept
WebDriverWait(driver, 10).until(EC.alert_is_present())
alert = driver.switch_to.alert
print(alert.text)
alert.accept()
#alert remove
WebDriverWait(driver, 10).until(EC.alert_is_present())
alert = driver.switch_to.alert
print(alert.text)
alert.accept()
time.sleep(2)
driver.refresh()

#select the Penny Drop module under the Verification Entry
driver.find_element(By.XPATH,"/html/body/div[1]/aside/section/ul/li[2]/ul/li[1]/a/span").click()
time.sleep(3)
#select the Penny Drop
driver.find_element(By.XPATH,"/html/body/div[1]/aside/section/ul/li[2]/ul/li[1]/ul/li[6]/a").click()
time.sleep(3)
#select the Center from the dropdown
wait = WebDriverWait(driver, 10)
# Step 1: Click on the Select2 dropdown to open options
dropdown = wait.until(EC.element_to_be_clickable((By.ID, "select2-centerId-container")))
dropdown.click()
# Step 2: Type "April" in the search box (Se#lect2 creates an input field after clicking)
search_box = wait.until(EC.presence_of_element_located((By.XPATH, "//input[@class='select2-search__field']")))
search_box.send_keys("April")
search_box.send_keys(Keys.ENTER)
time.sleep(3)
#select the Client from the dropdown
wait = WebDriverWait(driver, 10)
# Step 1: Click on the Select2 dropdown to open options
dropdown = wait.until(EC.element_to_be_clickable((By.ID, "select2-clientId-container")))
dropdown.click()
# Step 2: Type "April" in the search box (Se#lect2 creates an input field after clicking)
search_box = wait.until(EC.presence_of_element_located((By.XPATH, "/html/body/span/span/span[1]/input")))
search_box.send_keys("Tanay")
search_box.send_keys(Keys.ENTER)
time.sleep(3)
#click on the Submit button
driver.find_element(By.ID,"btnSubmit").click()
driver.implicitly_wait(4)
#Alert accept
WebDriverWait(driver, 10).until(EC.alert_is_present())
alert = driver.switch_to.alert
print(alert.text)
alert.accept()
print("Penny Drop is being restricted")
time.sleep(2)
#click on the Reset button
driver.find_element(By.ID,"btnReset").click()
time.sleep(4)
#select the Verification section
driver.find_element(By.XPATH,"/html/body/div[1]/aside/section/ul/li[2]/ul/li[1]/a/span").click()
#select the Update Client Mobile module
driver.find_element(By.XPATH,"/html/body/div[1]/aside/section/ul/li[2]/ul/li[1]/ul/li[7]/a").click()
time.sleep(2)
print("Mobile Update Module is selected")
#select the staff from the dropdown
wait = WebDriverWait(driver, 10)
# Step 1: Click on the Select2 dropdown to open options
dropdown = wait.until(EC.element_to_be_clickable((By.ID, "select2-staffId-container")))
dropdown.click()
# Step 2: Type "April" in the search box (Se#lect2 creates an input field after clicking)
search_box = wait.until(EC.presence_of_element_located((By.XPATH, "/html/body/span/span/span[1]/input")))
search_box.send_keys("fet1005")
search_box.send_keys(Keys.ENTER)
print("Staff is being selected")
time.sleep(3)
#select the center from the dropdown
wait = WebDriverWait(driver, 10)
# Step 1: Click on the Select2 dropdown to open options
dropdown = wait.until(EC.element_to_be_clickable((By.ID, "select2-table-center-container")))
dropdown.click()
# Step 2: Type "April" in the search box (Se#lect2 creates an input field after clicking)
search_box = wait.until(EC.presence_of_element_located((By.XPATH, "/html/body/span/span/span[1]/input")))
search_box.send_keys("April")
search_box.send_keys(Keys.ENTER)
print("Center is being selected")
time.sleep(3)
#select the Client from the dropdown
wait = WebDriverWait(driver, 10)
# Step 1: Click on the Select2 dropdown to open options
dropdown = wait.until(EC.element_to_be_clickable((By.ID, "select2-table-clientname-container")))
dropdown.click()
# Step 2: Type client name in the search box (Se#lect2 creates an input field after clicking)
search_box = wait.until(EC.presence_of_element_located((By.XPATH, "/html/body/span/span/span[1]/input")))
search_box.send_keys("Anu")
search_box.send_keys(Keys.ENTER)
print("Client is being selected")
time.sleep(3)
#select the Date Range
wait = WebDriverWait(driver, 10)
# Step 1: Click the date range picker div
date_picker = wait.until(EC.element_to_be_clickable((By.ID, "daterange")))
date_picker.click()
# Step 2: Select 'Yesterday'
yesterday_option = wait.until(EC.element_to_be_clickable((By.XPATH, "//li[contains(text(),'Yesterday')]")))
yesterday_option.click()
time.sleep(2)  # wait for selection to apply
# Step 3: Open date picker again
date_picker = wait.until(EC.element_to_be_clickable((By.ID, "daterange")))
date_picker.click()
# Step 4: Select 'Last 7 Days'
last7_option = wait.until(EC.element_to_be_clickable((By.XPATH, "//li[contains(text(),'Last 7 Days')]")))
last7_option.click()
print("Date is being selected")
time.sleep(3)
#click on th Submit button
driver.find_element(By.XPATH,"/html/body/div[1]/div/section/div[1]/div/div/div[2]/div[6]/div/span").click()
time.sleep(5)
print("Update Mobile Data is being fetched")
#click on the approval section
driver.find_element(By.XPATH,"/html/body/div[1]/div/section/div[2]/div[1]/div/div[2]").click()
#click on the approve button
driver.find_element(By.XPATH,"/html/body/div[1]/div/section/div[2]/div[1]/div/div[2]/div/div[3]/div[2]/table/tbody/tr/td[11]/button[1]").click()
time.sleep(3)
#click on the otp popup
driver.find_element(By.XPATH,"/html/body/div[1]/div/section/div[2]/div[2]/div/div[2]").click()
#click on the close icon
driver.find_element(By.XPATH,"/html/body/div[1]/div/section/div[2]/div[2]/div/div[1]/span").click()
print("OTP Popup is being closed")
driver.implicitly_wait(3)

#click on the logout button
driver.find_element(By.XPATH,"//a[normalize-space()='Sign out']").click()
print("the bm dashboard is successfully logout")
