#Module- Grievance Support , Cashbook Update & CIC Report & Tally Report
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException,TimeoutException
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
import time
import os
driver = webdriver.Chrome()
driver.get("https://uat-ho.lightmicrofinance.com/")
driver.maximize_window()
driver.implicitly_wait(10)

# Login
driver.find_element(By.ID, "username").send_keys("LMF09496")
driver.find_element(By.ID, "password").send_keys("Sanuabhishek$#@050392")
driver.find_element(By.ID, "login_button").click()

# Handle alert
WebDriverWait(driver, 10).until(EC.alert_is_present())
alert = driver.switch_to.alert
print(alert.text)
alert.accept()

#Select the Grievance Module
driver.find_element(By.XPATH,"//img[contains(@src,'../img/gms.png')]").click()

# Switch to iframe
WebDriverWait(driver, 10).until(EC.frame_to_be_available_and_switch_to_it((By.ID, "link")))

wait = WebDriverWait(driver, 10)

# Step 1: Click the Select2 dropdown to open it
dropdown = wait.until(EC.element_to_be_clickable((By.ID, "select2-branchId-container")))
dropdown.click()

# Step 2: Wait for the dropdown options to be visible
search_box = wait.until(EC.visibility_of_element_located((By.CLASS_NAME, "select2-search__field")))

# Step 3: Type the option you want to select
search_box.send_keys("210")
time.sleep(2)  # slight wait for options to load

search_box.send_keys(Keys.ENTER)

#Select the Search Field and select open
wait = WebDriverWait(driver, 10)
select_box = wait.until(EC.element_to_be_clickable((By.ID, "select2-statusId-container")))
select_box.click()

time.sleep(1)

# Select the option (e.g., 'Open/ Inprogress')
# Use the visible text of the option as it appears in the dropdown
option_to_select = wait.until(EC.element_to_be_clickable((By.XPATH, "//li[contains(text(), 'Open')]")))
option_to_select.click()
time.sleep(2)
#click on the Fetch Button
driver.find_element(By.XPATH,"/html[1]/body[1]/div[1]/div[1]/section[1]/form[1]/div[1]/div[1]/div[3]/button[1]").click()

#filter functionality
driver.find_element(By.XPATH,"//input[@type='search']").click()
driver.find_element(By.XPATH,"/html[1]/body[1]/div[1]/div[1]/section[1]/form[1]/div[1]/div[2]/div[2]/div[1]/div[2]/div[1]/label[1]/input[1]").send_keys('758473')
time.sleep(2)
#click on the View Button
driver.find_element(By.XPATH,"//tr[@id='rowIds1']//span[@id='view-info']").click()
driver.implicitly_wait(4)
#click on the doc icon to download
driver.find_element(By.XPATH,"/html/body/div[2]/div/div/div[2]/div/div[8]/div/div[2]/button[1]").click()
time.sleep(6)

#enter data in remarks
driver.find_element(By.XPATH,"/html/body/div[2]/div/div/div[2]/div/div[10]/div/div[2]/input").click()
driver.find_element(By.XPATH,"/html/body/div[2]/div/div/div[2]/div/div[10]/div/div[2]/input").send_keys('Automation Testing')
#click on the Update button
driver.find_element(By.ID,"modal-update-info").click()
time.sleep(13)
 #Handle alert
WebDriverWait(driver, 10).until(EC.alert_is_present())
alert = driver.switch_to.alert
print(alert.text)
alert.accept()

driver.implicitly_wait(4)
print("Grievance is successfully filtered and Refreshed")

#again select Branch
wait = WebDriverWait(driver, 10)

# Step 1: Click the Select2 dropdown to open it
dropdown = wait.until(EC.element_to_be_clickable((By.ID, "select2-branchId-container")))
dropdown.click()

# Step 2: Wait for the dropdown options to be visible
search_box = wait.until(EC.visibility_of_element_located((By.CLASS_NAME, "select2-search__field")))

# Step 3: Type the option you want to select
search_box.send_keys("210")
time.sleep(2)  # slight wait for options to load

search_box.send_keys(Keys.ENTER)
#select the InProgress Type
wait = WebDriverWait(driver, 10)
dropdown = wait.until(EC.element_to_be_clickable((By.ID, "select2-statusId-container")))
dropdown.click()
option = wait.until(EC.element_to_be_clickable((By.XPATH, "//li[contains(text(), 'In Progress ')]")))
option.click()
time.sleep(2)
#click on the Fetch Button
driver.find_element(By.XPATH,"//button[@id='fetchButton']").click()
time.sleep(4)

#filter functionality
driver.find_element(By.XPATH,"//input[@type='search']").click()
driver.find_element(By.XPATH,"//input[@type='search']").send_keys('757464')
time.sleep(4)
#click on the View Button
driver.find_element(By.XPATH,"//span[@id='view-info']").click()
#click on the Doc 1 image to download
driver.find_element(By.XPATH,"/html/body/div[2]/div/div/div[2]/div/div[8]/div/div[2]/button[1]").click()
time.sleep(4)

#enter data in remarks
driver.find_element(By.ID,"modal-remarks").click()
driver.find_element(By.ID,"modal-remarks").send_keys('Automation Testing Data')
#click on the Update button
driver.find_element(By.ID,"modal-update-info").click()
 #Handle alert
WebDriverWait(driver, 10).until(EC.alert_is_present())
alert = driver.switch_to.alert
print(alert.text)
alert.accept()
driver.implicitly_wait(5)
print("In Progress Data is filtered and updated")
driver.refresh()
driver.switch_to.default_content()

#Select the CIC Report
driver.find_element(By.XPATH,"/html/body/div/div/div[1]/div[2]/div[21]/a").click()
time.sleep(2)
# Switch to iframe
WebDriverWait(driver, 10).until(EC.frame_to_be_available_and_switch_to_it((By.ID, "link")))

#select the Dropdown popup
driver.find_element(By.XPATH,"/html/body/div[4]/div/div/div[1]/h4").click()
time.sleep(2)
#click on the dropdown and select the CIC report
dropdown = wait.until(EC.element_to_be_clickable((By.ID, "select2-reportTypeSelect-container")))
dropdown.click()

search_box = wait.until(EC.presence_of_element_located((By.XPATH, "//input[@class='select2-search__field']")))

#Select the CIC report from the dropdown
search_box.send_keys("CIC Report")
search_box.send_keys(Keys.ENTER)
print("CIC Report type selected!")
#click onto the continue button
driver.find_element(By.ID,"submitReportType").click()
driver.implicitly_wait(3)

#click on the view Icon
#driver.find_element(By.XPATH,"/html[1]/body[1]/div[3]/div[1]/div[1]/table[1]/tbody[1]/tr[1]/td[9]/button[1]").click()
#time.sleep(3)

# Handle alert
#WebDriverWait(driver, 10).until(EC.alert_is_present())
#alert = driver.switch_to.alert
#print(alert.text)
#alert.accept()
#click on the Popup
#driver.find_element(By.XPATH,"/html/body/div[5]/div/div/div[2]/table/tbody/tr[1]/td[5]").click()
#time.sleep(2)


#in popup click on the download button
#wait = WebDriverWait(driver, 10)
# Locate and click the download button (just once)
#downalod=driver.find_element(By.XPATH,"/html/body/div[5]/div/div/div[2]/table/tbody/tr[1]/td[5]/button/i")
#downalod.click()
# ⚡ Immediately handle the alert
#try:
    #alert = wait.until(EC.alert_is_present())
    #print("Alert text:", alert.text)

    # Accept alert (OK)
    #alert.accept()
    #print("Download confirmed!")

#except Exception as e:
    #print("No alert appeared:", e)

#click on the CLose ICon
#driver.find_element(By.XPATH,"/html/body/div[5]/div/div/div[1]/button").click()
#driver.implicitly_wait(5)

#click on the Download icon
driver.find_element(By.XPATH,"//tbody/tr[1]/td[9]/button[2]/i[1]").click()
#Alert handeling
WebDriverWait(driver, 11).until(EC.alert_is_present())
alert = driver.switch_to.alert
print(alert.text)
alert.accept()
time.sleep(2)

#click on the Initiate Process Icon
driver.find_element(By.XPATH,"/html/body/div[3]/div/div/table/tbody/tr[1]/td[9]/button[4]").click()
#Alert Accept
WebDriverWait(driver, 11).until(EC.alert_is_present())
alert = driver.switch_to.alert
print(alert.text)
alert.accept()
time.sleep(2)
#Alert remove
WebDriverWait(driver, 11).until(EC.alert_is_present())
alert = driver.switch_to.alert
print(alert.text)
alert.accept()
driver.implicitly_wait(4)
print("CIC Report is successfully Automated")
driver.refresh()

#select the Tally Report Again
driver.find_element(By.XPATH,"/html/body/div/div/div[1]/div[2]/div[21]/a/img").click()
time.sleep(2)
# Switch to iframe
WebDriverWait(driver, 10).until(EC.frame_to_be_available_and_switch_to_it((By.ID, "link")))

#select the Dropdown popup
driver.find_element(By.XPATH,"/html/body/div[4]/div/div/div[1]/h4").click()
time.sleep(2)
#click on the dropdown and select the CIC report
dropdown = wait.until(EC.element_to_be_clickable((By.ID, "select2-reportTypeSelect-container")))
dropdown.click()

search_box = wait.until(EC.presence_of_element_located((By.XPATH, "//input[@class='select2-search__field']")))

#Select the CIC report from the dropdown
search_box.send_keys("Tally Report")
search_box.send_keys(Keys.ENTER)
print("Tally Report type selected!")
#click onto the continue button
driver.find_element(By.ID,"submitReportType").click()
driver.implicitly_wait(3)
#click on the Tally Report sectiom
driver.find_element(By.XPATH,"/html/body/div[3]/div/div/table/thead/tr/th[9]").click()
#click on the View icon
driver.find_element(By.XPATH,"/html/body/div[3]/div/div/table/tbody/tr[1]/td[9]/button[1]").click()
time.sleep(2)
#click on the popup
driver.find_element(By.XPATH,"/html/body/div[5]/div/div/div[1]/h4").click()
time.sleep(2)
#click on the Download icon
driver.find_element(By.XPATH,"/html/body/div[5]/div/div/div[2]/table/tbody/tr/td[5]/button/i").click()
#alert accept
WebDriverWait(driver, 11).until(EC.alert_is_present())
alert = driver.switch_to.alert
print(alert.text)
alert.accept()
time.sleep(2)
#click on the Close icon in the poup
driver.find_element(By.XPATH,"/html/body/div[5]/div/div/div[1]/button").click()
time.sleep(2)
#click on the Download icon
driver.find_element(By.XPATH,"/html/body/div[3]/div/div/table/tbody/tr[1]/td[9]/button[2]").click()
print("Tally data is downloaded")
#alert accept
WebDriverWait(driver, 11).until(EC.alert_is_present())
alert = driver.switch_to.alert
print(alert.text)
alert.accept()
time.sleep(2)
#click on the Initaite button
driver.find_element(By.XPATH,"/html/body/div[3]/div/div/table/tbody/tr[1]/td[9]/button[4]/i").click()
print("Data is being Initiated")
#alert accept
WebDriverWait(driver, 11).until(EC.alert_is_present())
alert = driver.switch_to.alert
print(alert.text)
alert.accept()
time.sleep(2)
#alert remove
WebDriverWait(driver, 11).until(EC.alert_is_present())
alert = driver.switch_to.alert
print(alert.text)
alert.accept()
time.sleep(2)
driver.refresh()

#select the Cashbook Update module
driver.find_element(By.XPATH,"/html[1]/body[1]/div[1]/div[1]/div[1]/div[2]/div[10]/a[1]").click()

# Switch to iframe
WebDriverWait(driver, 10).until(EC.frame_to_be_available_and_switch_to_it((By.ID, "link")))
time.sleep(3)
#click on the box section
driver.find_element(By.XPATH,"/html[1]/body[1]/div[2]/div[1]").click()
time.sleep(2)

#click on the Branch Selection field
dropdown = wait.until(EC.element_to_be_clickable((By.ID, "select2-branchId-container")))
dropdown.click()

# Step 2: Wait for the dropdown options to be visible
search_box = wait.until(EC.visibility_of_element_located((By.XPATH, "//input[@role='searchbox']")))
search_box.click()
# Step 3: Type the option you want to select
search_box.send_keys("210")
time.sleep(2)  # slight wait for options to load
search_box.send_keys(Keys.ENTER)

#click on the search button
driver.find_element(By.ID,"searchButton").click()
time.sleep(14)

#click on the Editable section
driver.find_element(By.XPATH,"/html/body/div[3]").click()
driver.implicitly_wait(4)
#click on the Credit  section
driver.find_element(By.XPATH,"/html[1]/body[1]/div[3]/div[2]/div[1]/div[1]/table[1]/tbody[1]/tr[2]/td[2]/input[1]").click()
driver.find_element(By.XPATH,"/html[1]/body[1]/div[3]/div[2]/div[1]/div[1]/table[1]/tbody[1]/tr[2]/td[2]/input[1]").send_keys('100')
#click on the Debit section
driver.find_element(By.XPATH,"/html[1]/body[1]/div[3]/div[2]/div[1]/div[2]/table[1]/tbody[1]/tr[2]/td[2]/input[1]").click()
driver.find_element(By.XPATH,"/html[1]/body[1]/div[3]/div[2]/div[1]/div[2]/table[1]/tbody[1]/tr[2]/td[2]/input[1]").send_keys('100')
driver.implicitly_wait(5)

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

#click on the down section
driver.find_element(By.XPATH,"/html/body/div[3]/div[2]/div/div[1]/table/tbody/tr[15]/td[1]").click()
time.sleep(2)
#click on the Closing Balance section
driver.find_element(By.XPATH,"//div[@class='form-group col-md-4']").click()
driver.set_page_load_timeout(1)

#click on the Calculate button
driver.find_element(By.ID,"calculateButton").click()
time.sleep(2)

#click on the Denomination Button
driver.find_element(By.ID,"denominationBtn").click()
time.sleep(2)
#click on the popup section
driver.find_element(By.XPATH,"/html/body/div[3]/div[5]/div/div/div/div[2]/div[1]").click()
#click on the Update Button
driver.find_element(By.ID,"submitDenomination").click()
#alert accept
WebDriverWait(driver, 11).until(EC.alert_is_present())
alert = driver.switch_to.alert
print(alert.text)
alert.accept()
time.sleep(5)
#print("cashbook data updated successfully")
driver.refresh()






driver.switch_to.default_content()
# Logout
WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//a[normalize-space()='Logout']"))).click()
print("Ho Dashboard is successfully logged out")


