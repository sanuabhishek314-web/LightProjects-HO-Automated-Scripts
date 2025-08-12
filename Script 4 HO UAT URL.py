# Document Verification , Pay by link and Digital Cashbook
from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException, TimeoutException, UnexpectedAlertPresentException
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
import os
import time
driver = webdriver.Chrome()
driver.get("https://uat-ho.lightmicrofinance.com/")
driver.maximize_window()
driver.implicitly_wait(10)
driver.save_screenshot('full_page.png')
# Login
driver.find_element(By.ID, "username").send_keys("LMF09496")
driver.find_element(By.ID, "password").send_keys("Sanuabhishek$#@050392")
driver.find_element(By.ID, "login_button").click()

# Handle alert
WebDriverWait(driver, 10).until(EC.alert_is_present())
alert = driver.switch_to.alert
print(alert.text)
alert.accept()

#select the Document Verification Module
#driver.find_element(By.XPATH,"//img[contains(@src,'../img/doc_verification.png')]").click()
time.sleep(4)
# Switch to iframe
#WebDriverWait(driver, 10).until(EC.frame_to_be_available_and_switch_to_it((By.ID, "link")))

#select the Branch
#dropdown = driver.find_element(By.ID, 'select2-branch-container')
#dropdown.click()
#time.sleep(2)
#search_box = driver.find_element(By.XPATH, '/html[1]/body[1]/span[1]/span[1]/span[1]/input[1]')
#search_box.send_keys("210")
#search_box.send_keys(Keys.ENTER)
#time.sleep(2)

#click on the Apply Button
#driver.find_element(By.ID,"verification-list-form-submit").click()
#time.sleep(4)
#click on the Verify Document button
#driver.find_element(By.ID,"verify-docs").click()
#time.sleep(5)

#scroll down to click on the Back button
#scroll_pause_time = 1  # Pause time between scrolls
#scroll_height = driver.execute_script("return document.body.scrollHeight")

#current_position = 0
#increment = 500  # Number of pixels to scroll each time

#while current_position < scroll_height:
    #driver.execute_script(f"window.scrollTo(0, {current_position});")
    #time.sleep(scroll_pause_time)
    #current_position += increment
    #scroll_height = driver.execute_script("return document.body.scrollHeight")  # update in case it changes

#click on the Back button
#driver.find_element(By.ID,"back-btn").click()
#time.sleep(2)
#print("Document Verification Date Not available")
#driver.refresh()
#driver.implicitly_wait(7)


#select the Digital Cashbook Module
driver.find_element(By.XPATH,"/html[1]/body[1]/div[1]/div[1]/div[1]/div[2]/div[9]/a[1]/img[1]").click()
time.sleep(3)

# Switch to iframe
WebDriverWait(driver, 10).until(EC.frame_to_be_available_and_switch_to_it((By.ID, "link")))
time.sleep(1)

#select the Cashbook Report option
driver.find_element(By.ID,"optionsRadios2").click()
driver.implicitly_wait(4)
#select the Branch from the dropdown
dropdown = Select(driver.find_element(By.ID, "branch_ID"))
dropdown.select_by_value('208')
time.sleep(15)
#WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.XPATH, "/html/body/div/div[2]/div[3]/div/div/div[2]/div[1]/button[1]/span"))).click()
#click on the search button section
driver.find_element(By.XPATH,"/html[1]/body[1]/div[1]/div[2]/div[3]/div[1]/div[1]/div[1]/table[1]/tbody[1]/tr[1]/td[3]").click()
driver.implicitly_wait(12)
#click on the Search button
driver.find_element(By.XPATH,"//button[@class='search_filter btn']").click()
driver.implicitly_wait(10)

#click on the CSV
driver.find_element(By.XPATH,"/html/body/div/div[2]/div[3]/div/div/div[2]/div[1]/button[1]/span").click()
time.sleep(2)
#click on excel
driver.find_element(By.XPATH,"/html/body/div/div[2]/div[3]/div/div/div[2]/div[1]/button[2]/span").click()
time.sleep(4)
#click on the Branch hyperlink
#driver.find_element(By.XPATH,"/html/body/div/div[2]/div[3]/div/div/div[2]/table/tbody/tr/td[3]/a").click()
#time.sleep(3)
print("Digital Cashbook File is downloaded successfully")
driver.refresh()
driver.implicitly_wait(5)

driver.switch_to.default_content()
#select the Pay by link Module
driver.find_element(By.XPATH,"/html[1]/body[1]/div[1]/div[1]/div[1]/div[2]/div[16]/a[1]/img[1]").click()
time.sleep(3)
# Switch to iframe
WebDriverWait(driver, 10).until(EC.frame_to_be_available_and_switch_to_it((By.ID, "link")))

#click on the Branch dropdown
wait = WebDriverWait(driver, 10)
select2_container = wait.until(EC.element_to_be_clickable((By.XPATH, "//span[@id='select2-branchId-container']")))
select2_container.click()
search_box = wait.until(EC.presence_of_element_located((By.XPATH, "//input[@class='select2-search__field']")))

search_box.send_keys("210")
search_box.send_keys(Keys.ENTER)
time.sleep(2)
#select the center to proceed
wait = WebDriverWait(driver, 10)

# Step 1: Click on the Select2 dropdown for center selection
center_dropdown = wait.until(EC.element_to_be_clickable((By.ID, "select2-centerId-container")))
center_dropdown.click()

# Step 2: Wait for the input field to appear
search_input = wait.until(EC.presence_of_element_located((By.XPATH, "//input[@class='select2-search__field']")))

# Step 3: Type "Consent ekyc" and hit ENTER
search_input.send_keys("Consent ekyc")
search_input.send_keys(Keys.ENTER)

# Wait for selection to apply (optional)
#wait.until(EC.text_to_be_present_in_element((By.ID, "select2-centerId-container"), "Consent ekyc"))
time.sleep(3)
#click on the search button
driver.find_element(By.XPATH,"/html[1]/body[1]/div[1]/div[1]/section[1]/form[1]/div[1]/div[1]/div[3]/button[1]").click()
time.sleep(2)
#click on the search field
driver.find_element(By.XPATH,"//input[@type='search']").click()
time.sleep(2)
#enter the client ID
driver.find_element(By.XPATH,"/html[1]/body[1]/div[1]/div[1]/section[1]/form[1]/div[1]/div[3]/div[2]/div[1]/div[2]/div[1]/label[1]/input[1]").send_keys("757860")
driver.implicitly_wait(3)

#click on select all checkbox
driver.find_element(By.XPATH,"/html/body/div/div/section/form/div/div[3]/div[2]/div[2]/div/div/div[1]/div/table/thead/tr/th[1]/input").click()
#click on send payment link button
driver.find_element(By.ID,"sendPayLinkButton").click()
driver.implicitly_wait(15)
#click on the popup
#driver.find_element(By.XPATH,"/html/body/div[2]/div[2]/div/div/div/div/div/div/div/div[2]").click()
driver.implicitly_wait(6)
#click on the OK button
#driver.find_element(By.XPATH,"//button[normalize-space()='OK']").click()
#time.sleep(6)
print("Payment Link is successfully sent")
#click on the clear filter button
#driver.find_element(By.ID,"clearFilterButton").click()
#driver.implicitly_wait(4)
driver.refresh()


driver.switch_to.default_content()
# Logout
WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//a[normalize-space()='Logout']"))).click()
print("Ho Dashboard is successfully logged out")

