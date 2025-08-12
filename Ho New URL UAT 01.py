# Module- FOIR, Documents and Penny Drop
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

#Select the FOIR MOdule
driver.find_element(By.XPATH,"/html[1]/body[1]/div[1]/div[1]/div[1]/div[2]/div[13]/a[1]").click()
time.sleep(3)

# Switch to iframe
WebDriverWait(driver, 10).until(EC.frame_to_be_available_and_switch_to_it((By.ID, "link")))

#Select the Branch and Date range
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

#Date Range Select
daterange = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.ID, "daterange")))
daterange.click()
Date_range_key = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//li[normalize-space()='Last 7 Days']")))
Date_range_key.click()

daterange = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.ID, "daterange")))
daterange.click()

Date_Range_key1 = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "/html[1]/body[1]/div[2]/div[1]/ul[1]/li[4]")))
Date_Range_key1.click()

daterange = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.ID, "daterange")))
daterange.click()
time.sleep(2)

#Click on the Apply Button
apply_button = driver.find_element(By.XPATH, "//button[text()='Apply']")
apply_button.click()
#click on the search button
driver.find_element(By.ID,"fetchButton").click()
time.sleep(4)
#click on the search filter
driver.find_element(By.XPATH,"//input[@type='search']").click()
driver.find_element(By.XPATH,"//input[@type='search']").send_keys('760060')
time.sleep(3)
print("The FOIR data is being filtered successfully")
#click on the clear button
driver.find_element(By.ID,"clearFilterButton").click()

driver.refresh()

#Select the Documents Module
driver.find_element(By.XPATH,"//img[contains(@src,'../img/images_list.png')]").click()

# Switch to iframe
WebDriverWait(driver, 10).until(EC.frame_to_be_available_and_switch_to_it((By.ID, "link")))
#click on the search field
driver.find_element(By.XPATH,"//input[@name='branch_type_filter']").click()
driver.find_element(By.XPATH,"/html[1]/body[1]/div[2]/div[1]/div[1]/table[1]/tbody[1]/tr[1]/td[1]/input[1]").send_keys('745409')
#click on the top grid
driver.find_element(By.XPATH,"//div[@id='employee-grid_length']").click()
time.sleep(2)

#Select the Dropdown
#wait = WebDriverWait(driver, 10)

# Step 1: Click to open the dropdown
select2_container = wait.until(EC.element_to_be_clickable((By.XPATH, "/html[1]/body[1]/div[2]/div[1]/div[1]/table[1]/tbody[1]/tr[1]/td[2]/span[1]/span[1]/span[1]/span[2]/b[1]")))
select2_container.click()

#Enter Data on the search field
try:
    # Wait for the input to be visible
    search_input = WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.CLASS_NAME, "select2-search__field")))

    search_input.click()

    # Type into the input
    search_input.send_keys("210")  # Replace with your desired input

    # Wait for results and press Enter to select first match (if appropriate)
    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR, "li.select2-results__option")))
    search_input.send_keys(Keys.ENTER)
finally:
    # Optional: pause and then quit
    import time
    time.sleep(5)



try:
    # Wait for the dropdown to be present
    dropdown_element = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, "//tbody/tr/td[3]/select[1]")))

    select = Select(dropdown_element)

    select.select_by_value("GRT Images")  # Change to any other option as needed

    # Optional: pause to observe result
    import time
    time.sleep(5)

finally:
    time.sleep(2)



#click on the Downloaded button
driver.find_element(By.XPATH,"//tbody/tr[1]/td[6]/button[1]").click()

#click on the Reset button
driver.implicitly_wait(6)
driver.find_element(By.XPATH,"//button[@class='reset_filter btn']").click()
time.sleep(4)
print("Documents Being Filtered Successfully")

driver.refresh()




#Select the Penny Drop Module
driver.find_element(By.XPATH,"/html[1]/body[1]/div[1]/div[1]/div[1]/div[2]/div[3]/a[1]").click()

# Switch to iframe
WebDriverWait(driver, 10).until(EC.frame_to_be_available_and_switch_to_it((By.ID, "link")))
time.sleep(3)
#click on the Client ID field
searchbox = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.ID, "clientIdInput")))
searchbox.click()
searchbox.send_keys("758503")
searchbox.send_keys(Keys.ENTER)
time.sleep(6)
#click on the Submit button
driver.find_element(By.ID,"btnSubmit").click()
time.sleep(2)
#alert to accept
WebDriverWait(driver, 11).until(EC.alert_is_present())
alert = driver.switch_to.alert
print(alert.text)
alert.accept()
time.sleep(7)
#click on the Reset Button
driver.find_element(By.ID,"btnReset").click()

#Alert to remove
#WebDriverWait(driver, 11).until(EC.alert_is_present())
#alert = driver.switch_to.alert
#print(alert.text)
#alert.accept()
time.sleep(3)
print("Penny Drops Max Attempt Exceeded")
driver.refresh()
#click on reset button
#driver.find_element(By.ID,"btnReset").click()
#driver.refresh()



driver.switch_to.default_content()


# Logout
WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//a[normalize-space()='Logout']"))).click()
print("Ho Dashboard is successfully logged out")
