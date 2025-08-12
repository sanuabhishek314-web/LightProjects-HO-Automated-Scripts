#Testcases for the HO Dashboard ( DBT, Branch Grading and Ticket Allocation)
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
driver.get("https://uat-ho.lightmicrofinance.com/index.php")
driver.maximize_window()
driver.implicitly_wait(10)




# Login
driver.find_element(By.ID, "username").send_keys("LMF09496")
driver.find_element(By.ID, "password").send_keys("Sanuabhishek$#@050392")
driver.find_element(By.ID, "login_button").click()

# Handle alert
WebDriverWait(driver, 11).until(EC.alert_is_present())
alert = driver.switch_to.alert
print(alert.text)
alert.accept()



driver.save_screenshot('full_page.png')
print("Screenshot is captured successfully")

# Click DBT Module
WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//a[contains(@onclick, 'dbt_module/index.php')]"))).click()

# Switch to iframe
WebDriverWait(driver, 10).until(EC.frame_to_be_available_and_switch_to_it((By.ID, "link")))

# Click and type in clientId field
searchbox = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.ID, "clientId")))
searchbox.click()
searchbox.send_keys("758226")
searchbox.send_keys(Keys.ENTER)

time.sleep(3)  # optional, give time to load
#Click on the Submit button
driver.find_element(By.ID,"btnSubmit").click()
time.sleep(1)
#Alert Accept
WebDriverWait(driver, 11).until(EC.alert_is_present())
alert = driver.switch_to.alert
print(alert.text)
alert.accept()
# Back to default content if needed for logout
driver.save_screenshot('full_page.png')
print("Screenshot is captured successfully")

driver.switch_to.default_content()

# Select the Branch Grading Module
driver.find_element(By.XPATH,"/html[1]/body[1]/div[1]/div[1]/div[1]/div[2]/div[12]/a[1]").click()

# Switch to iframe
WebDriverWait(driver, 10).until(EC.frame_to_be_available_and_switch_to_it((By.ID, "link")))

#Click on the Parameter Master option button
driver.find_element(By.ID,"optionsRadios1").click()
time.sleep(8)

#Click on Parameter Master Button
driver.find_element(By.XPATH,"/html[1]/body[1]/div[1]/div[2]/div[2]/div[1]/section[1]/form[1]/div[1]/div[1]/div[1]/button[1]").click()
#click on the Para name field
driver.find_element(By.ID,"parameterNameId").click()
driver.find_element(By.ID,"parameterNameId").send_keys('Parameter 21')
driver.save_screenshot('full_page.png')
print("Screenshot is captured successfully")
try:

 # Wait up to 10 seconds for the dropdown element to be present
    dropdown_element = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, "//select[@id='parameterStatus']")))

    # Create a Select object
    select = Select(dropdown_element)

    # Select "Active" by visible text
    select.select_by_index(1)

    print("Dropdown selection successful.")

except TimeoutException as e:
    print("Timeout: Dropdown element not found within 10 seconds:", e)

except NoSuchElementException as e:
    print("Dropdown element not found:", e)


#Date Picker
wait = WebDriverWait(driver, 10)

# Wait until the input is ready and set the date (format: YYYY-MM-DD)
date_input = wait.until(EC.element_to_be_clickable((By.NAME, "activationDate")))
date_input.clear()
date_input.send_keys("07-04-2025")  # Replace with your desired date
print("Date set successfully.")
#selected_date = calendar_input.get_attribute("value")
#print("Selected date:", selected_date)

#select the Value Type
try:

 # Wait up to 10 seconds for the dropdown element to be present
    dropdown_element = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, "//select[@id='parameterValueType']")))

    # Create a Select object
    select = Select(dropdown_element)

    # Select "Active" by visible text
    select.select_by_value("exact")

    print("Dropdown selection successful.")

except TimeoutException as e:
    print("Timeout: Dropdown element not found within 10 seconds:", e)

except NoSuchElementException as e:
    print("Dropdown element not found:", e)



#click on the Submit button
driver.find_element(By.ID,"btnSubmit").click()
time.sleep(3)


#Select the Score Rule Master option
driver.find_element(By.ID,"optionsRadios2").click()
driver.save_screenshot('full_page.png')
print("Screenshot is captured successfully")
#Click on the Score Rule Master button
driver.find_element(By.XPATH,"//button[normalize-space()='Create Score Rule Master']").click()
try:

 # Wait up to 10 seconds for the dropdown element to be present
    dropdown_element = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, "//select[@id='paramName']")))

    # Create a Select object
    select = Select(dropdown_element)

    # Select "Paramater" by visible text
    select.select_by_index(14)

    print("Dropdown selection successful.")

except TimeoutException as e:
    print("Timeout: Dropdown element not found within 10 seconds:", e)

except NoSuchElementException as e:
    print("Dropdown element not found:", e)

#select the category type
try:

 # Wait up to 10 seconds for the dropdown element to be present
    dropdown_element = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, "//select[@id='paramCategory']")))

    # Create a Select object
    select = Select(dropdown_element)

    # Select "Paramater" by visible text
    select.select_by_index(1)

    print("Dropdown selection successful.")
except TimeoutException as e:
    print("Timeout: Dropdown element not found within 10 seconds:", e)

except NoSuchElementException as e:
    print("Dropdown element not found:", e)

#enter data in the Max Score and Target and Condition Score
driver.find_element(By.ID,"maxScore").click()
driver.find_element(By.ID,"maxScore").send_keys("21")
driver.find_element(By.ID,"paramTarget").click()
driver.find_element(By.ID,"paramTarget").send_keys("18")
driver.find_element(By.ID,"paramCondTarget").click()
driver.find_element(By.ID,"paramCondTarget").send_keys("19")
#click on the Submit button
driver.find_element(By.ID,"btnSubmit").click()
print("Score Rule Master Created Successfully")
driver.refresh()
time.sleep(3)

driver.switch_to.default_content()

#Ticket Allocation Module
driver.find_element(By.XPATH,"//img[@alt='receipt_manager']").click()
driver.save_screenshot('full_page.png')
print("Screenshot is captured successfully")
WebDriverWait(driver, 10).until(EC.frame_to_be_available_and_switch_to_it((By.ID, "link")))
#select the dropdown
driver.implicitly_wait(5)
driver.find_element(By.XPATH,"//span[@role='presentation']").click()


#click on the searchx
search_input = WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.XPATH, "//input[@role='searchbox']")))
search_input.clear()
search_input.send_keys("fet1004")

# Wait for suggestions to load
option = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//li[contains(text(), '210208Test - fet1004, fet1004')]")))
option.click()
driver.implicitly_wait(13)
#click on  End Range section
WebDriverWait(driver, 10).until(EC.invisibility_of_element_located((By.CLASS_NAME, "loadingClass")))
#driver.find_element(By.XPATH, "//label[normalize-space()='Enter Receipt End Count']").click()
#click on end range field
driver.find_element(By.XPATH,"//input[@id='txtInputReceiptEndRange']").click()
driver.find_element(By.XPATH,"//input[@id='txtInputReceiptEndRange']").send_keys('16084')
#click on the Allocate Button
driver.find_element(By.XPATH,"//button[@type='submit']").click()
time.sleep(13)
#assert accept
WebDriverWait(driver, 11).until(EC.alert_is_present())
alert = driver.switch_to.alert
print(alert.text)
alert.accept()
time.sleep(17)
#WebDriverWait(driver, 20).until(EC.invisibility_of_element_located((By.CLASS_NAME, "loadingClass")))

# Now safely click the history icon
WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//i[@class='fa fa-history']"))).click()
#click on the view icon
#driver.find_element(By.XPATH,"//i[@class='fa fa-history']").click()
#time.sleep(4)
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
driver.implicitly_wait(2)
#click on the close button in the popup
driver.find_element(By.XPATH,"/html/body/div[1]/div/section/div[1]/div/div/div[3]/button").click()
time.sleep(3)
print("View icon popup is closed")
#click on the Refresh button
#driver.find_element(By.XPATH,"/html[1]/body[1]/div[1]/div[1]/section[1]/div[2]/div[2]/form[1]/table[1]/tbody[1]/tr[1]/td[3]/div[1]/button[2]").click()
print("Ticket Allocation is successfull")
driver.refresh()



driver.switch_to.default_content()

driver.save_screenshot('full_page.png')
print("Screenshot is captured successfully")
# Logout
WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//a[normalize-space()='Logout']"))).click()
print("Ho Dashboard is successfully logged out")
