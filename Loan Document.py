# Center Wise Document, Loan Application Document, Generate Loan Document and Loan Card
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select
from selenium.webdriver import ActionChains
from selenium.common.exceptions import NoSuchElementException, TimeoutException
from datetime import datetime
import time
import os
from utils import get_screenshot_path

driver = webdriver.Chrome()
driver.get("https://uat-bm.lightmicrofinance.com/index.php")
driver.maximize_window()
driver.implicitly_wait(10)

# login to the dashboard
driver.find_element(By.ID, "inputUsername").click()
driver.find_element(By.NAME, "inputUsername").send_keys("BMT1009")
driver.find_element(By.ID, "inputPassword").click()
driver.find_element(By.NAME, "inputPassword").send_keys("Light@123")
driver.find_element(By.XPATH, "//button[@type='submit']").click()
time.sleep(11)

# select the Loan Document Section
driver.find_element(By.XPATH, "/html/body/div[1]/aside/section/ul/li[2]/ul/li[2]/a/span").click()
# select the Center Wise Document
driver.find_element(By.XPATH, "/html/body/div[1]/aside/section/ul/li[2]/ul/li[2]/ul/li[1]/a").click()
time.sleep(3)
# click on the Center Wise popup
driver.find_element(By.XPATH, "/html/body/div[3]/div[1]/div[2]/div[2]/div[1]/div/h3").click()
time.sleep(3)
# Select the Center from the dropdown
wait = WebDriverWait(driver, 10)
# Step 1: Click the Select2 container to open the dropdown
select_box = wait.until(EC.element_to_be_clickable(
    (By.XPATH, "/html/body/div[3]/div[1]/div[2]/div[2]/div[1]/div/form/div[1]/div/span/span[1]/span/span[1]")))
select_box.click()
# Step 2: Type or click the desired option (e.g., "April")
search_box = wait.until(
    EC.element_to_be_clickable((By.XPATH, "/html/body/div[3]/div[1]/div[2]/div[2]/div[1]/div/span/span/span[1]/input")))
search_box.send_keys("April")
search_box.send_keys(Keys.ENTER)
time.sleep(3)
# click on the Submit button
driver.find_element(By.XPATH, "/html/body/div[3]/div[1]/div[2]/div[2]/div[1]/div/form/div[4]/div/button").click()
time.sleep(5)
print("Addendum is being downloaded")
# select the Sanction Note from the dropdown
wait = WebDriverWait(driver, 10)
dropdown_element = wait.until(EC.presence_of_element_located((By.ID, "document")))
# create Select object
dropdown = Select(dropdown_element)
# Option 2: select by visible text
dropdown.select_by_visible_text("Sanction")
# Click onto the submit button
driver.find_element(By.XPATH, "/html/body/div[3]/div[1]/div[2]/div[2]/div[1]/div/form/div[4]/div/button").click()
time.sleep(4)
print(dropdown.first_selected_option.text)
# Select LPF Acknowledgement
wait = WebDriverWait(driver, 10)
dropdown_element = wait.until(EC.presence_of_element_located((By.ID, "document")))
# create Select object
dropdown = Select(dropdown_element)
# Option 3: select by visible text
dropdown.select_by_visible_text("LPF Acknowledgement")
# Click onto the submit button
driver.find_element(By.XPATH, "/html/body/div[3]/div[1]/div[2]/div[2]/div[1]/div/form/div[4]/div/button").click()
time.sleep(4)
print(dropdown.first_selected_option.text)
# Select the Insurance ACK
wait = WebDriverWait(driver, 10)
dropdown_element = wait.until(EC.presence_of_element_located((By.ID, "document")))
# create Select object
dropdown = Select(dropdown_element)
# Option 4: select by visible text
dropdown.select_by_visible_text("Insurance Acknowledgement")
# Click onto the submit button
driver.find_element(By.XPATH, "/html/body/div[3]/div[1]/div[2]/div[2]/div[1]/div/form/div[4]/div/button").click()
time.sleep(4)
print(dropdown.first_selected_option.text)
# click on the Close icon in the popup
driver.find_element(By.XPATH, "/html/body/div[3]/div[1]/div[2]/div[2]/button[4]").click()
time.sleep(2)
# click on the Dashboard section
driver.find_element(By.XPATH, "/html/body/div[1]/header/a/span[2]").click()
time.sleep(4)

# select the Loan application document
driver.find_element(By.XPATH, "/html/body/div[1]/aside/section/ul/li[2]/ul/li[2]/a/span").click()
time.sleep(2)
driver.find_element(By.XPATH, '/html/body/div[1]/aside/section/ul/li[2]/ul/li[2]/ul/li[2]/a').click()
driver.implicitly_wait(3)
# click on the Loan Application popup
driver.find_element(By.XPATH, "/html/body/div[3]/div[1]/div[2]/div[2]/div[1]/div/h3").click()
time.sleep(3)
# select the Center from the dropdown
wait = WebDriverWait(driver, 10)
# Step 1: Click the Select2 container to open the dropdown
select_box = wait.until(EC.element_to_be_clickable(
    (By.XPATH, "/html/body/div[3]/div[1]/div[2]/div[2]/div[1]/div/form/div[1]/div/span/span[1]/span/span[1]")))
select_box.click()
# Step 2: Type or click the desired option (e.g., "April")
search_box = wait.until(
    EC.element_to_be_clickable((By.XPATH, "/html/body/div[3]/div[1]/div[2]/div[2]/div[1]/div/span/span/span[1]/input")))
search_box.send_keys("April")
search_box.send_keys(Keys.ENTER)
time.sleep(3)
# click on the Submit button
driver.find_element(By.XPATH, "/html/body/div[3]/div[1]/div[2]/div[2]/div[1]/div/form/div[2]/div/button").click()
time.sleep(10)
print("Loan Document Data is being downloaded successfullly")
# click on the close icon in the popup
driver.find_element(By.ID, "cboxClose").click()
time.sleep(2)
# click on the Dasboard section at the top
driver.find_element(By.XPATH, '/html/body/div[1]/header/a/span[2]').click()
time.sleep(2)
# expand loan document section again
driver.find_element(By.XPATH, "/html/body/div[1]/aside/section/ul/li[2]/ul/li[2]/a/span").click()
# select Generate Loan Document
driver.find_element(By.XPATH, "/html/body/div[1]/aside/section/ul/li[2]/ul/li[2]/ul/li[3]/a").click()
time.sleep(3)
# click on the Generate Loan section
driver.find_element(By.XPATH, "/html/body/div[1]/div/section/div[1]/div/div/div[1]/h3").click()
#click on the CLient ID field
driver.find_element(By.ID,"clientId").click()
driver.find_element(By.ID,"clientId").send_keys("759938")
time.sleep(3)
#click on the Backdated Checkbox
driver.find_element(By.XPATH,"/html/body/div[1]/div/section/div[1]/div/div/div[2]/div[4]/div/input").click()
time.sleep(3)
#click on to the fetch button
driver.find_element(By.ID,'fetchDataBtn').click()
time.sleep(18)
#click on select all checkbox and click on Loan ACK button
driver.find_element(By.XPATH,"//div[@class='col-md-2']").click()
driver.implicitly_wait(4)
#click on the select all section
driver.find_element(By.XPATH,"//th[@class='sorting_disabled']").click()
time.sleep(3)
#checkin the select all checkbox
driver.find_element(By.XPATH,"//input[@id='checkAll']").click()
time.sleep(4)
print("Select All checkbox is checked")
#now again click onto the button section again
wait = WebDriverWait(driver, 30)
# Wait until overlay disappears
try:
    wait.until(EC.invisibility_of_element_located((By.CSS_SELECTOR, "div.bg")))
except:
    pass  # overlay might not always appear
# Wait for the Insurance button to become clickable
insurance_btn = wait.until(EC.element_to_be_clickable((By.ID, "submitIncDocBtn")))
# Scroll into view (sometimes helps)
driver.execute_script("arguments[0].scrollIntoView(true);", insurance_btn)
time.sleep(0.5)
# Click using JavaScript to bypass overlay issues
driver.execute_script("arguments[0].click();", insurance_btn)
print(" Insurance document download triggered.")
time.sleep(10)

#click on the Dashboard section
driver.find_element(By.XPATH,"//span[@class='logo-lg']").click()
time.sleep(5)

#Expand the loan Document section again
driver.find_element(By.XPATH,"//span[normalize-space()='Loan Document']").click()
#select Loan Card , SOA
driver.find_element(By.XPATH,"//a[normalize-space()='Loan Card, SOA, NOC']").click()
print("Loan card & SOA is selected")
time.sleep(5)
#select the staff from the dropdown
wait = WebDriverWait(driver, 10)
# Step 1: Click the Select2 dropdown to open it
dropdown = wait.until(EC.element_to_be_clickable((By.ID, "select2-staff-container")))
dropdown.click()
# Step 2: Wait for the dropdown options to be visible
search_box = wait.until(EC.visibility_of_element_located((By.CLASS_NAME, "select2-search__field")))
# Step 3: Type the option you want to select
search_box.send_keys("fet1005")
# slight wait for options to load
search_box.send_keys(Keys.ENTER)
time.sleep(3)
#select the center from the dropdown
wait = WebDriverWait(driver, 10)
# Step 1: Click the Select2 dropdown to open it
dropdown = wait.until(EC.element_to_be_clickable((By.ID, "select2-center-container")))
dropdown.click()
# Step 2: Wait for the dropdown options to be visible
search_box = wait.until(EC.visibility_of_element_located((By.XPATH, "/html/body/span/span/span[1]/input")))
# Step 3: Type the option you want to select
search_box.send_keys("April")
# slight wait for options to load
search_box.send_keys(Keys.ENTER)
time.sleep(3)
#select the client from the dropdown
wait = WebDriverWait(driver, 10)
# Step 1: Click the Select2 dropdown to open it
dropdown = wait.until(EC.element_to_be_clickable((By.ID, "select2-client-container")))
dropdown.click()
# Step 2: Wait for the dropdown options to be visible
search_box = wait.until(EC.visibility_of_element_located((By.XPATH, "/html/body/span/span/span[1]/input")))
# Step 3: Type the option you want to select
search_box.send_keys("Pushpanjali")
# slight wait for options to load
search_box.send_keys(Keys.ENTER)
time.sleep(3)
#select the Loan ID
wait = WebDriverWait(driver, 10)
# Step 1: Click the Select2 dropdown to open it
dropdown = wait.until(EC.element_to_be_clickable((By.XPATH, "/html/body/div[1]/div/section/div[1]/div/div/div[2]/div[2]/div[1]/div/span/span[1]/span/span[1]")))
dropdown.click()
# Step 2: Wait for the dropdown options to be visible
search_box = wait.until(EC.visibility_of_element_located((By.XPATH, "/html/body/span/span/span[1]/input")))
# Step 3: Type the option you want to select
search_box.send_keys("1077083")
# slight wait for options to load
search_box.send_keys(Keys.ENTER)
time.sleep(3)
#select the Document Type
wait = WebDriverWait(driver, 10)
# Step 1: Click the Select2 dropdown to open it
dropdown = wait.until(EC.element_to_be_clickable((By.XPATH, "/html/body/div[1]/div/section/div[1]/div/div/div[2]/div[2]/div[2]/div/span/span[1]/span/span[1]")))
dropdown.click()
# Step 2: Wait for the dropdown options to be visible
search_box = wait.until(EC.visibility_of_element_located((By.XPATH, "/html/body/span/span/span[1]/input")))
# Step 3: Type the option you want to select
search_box.send_keys("Loan Card")
# slight wait for options to load
search_box.send_keys(Keys.ENTER)
time.sleep(3)
#click on the Generate Document button
driver.find_element(By.ID,"generateDocument").click()
time.sleep(10)
print("Loan Document has been downloaded successfully")
#select the SOA
wait = WebDriverWait(driver, 10)
# Step 1: Click the Select2 dropdown to open it
dropdown = wait.until(EC.element_to_be_clickable((By.XPATH, "/html/body/div[1]/div/section/div[1]/div/div/div[2]/div[2]/div[2]/div/span/span[1]/span/span[1]")))
dropdown.click()
# Step 2: Wait for the dropdown options to be visible
search_box = wait.until(EC.visibility_of_element_located((By.XPATH, "/html/body/span/span/span[1]/input")))
# Step 3: Type the option you want to select
search_box.send_keys("SOA")
# slight wait for options to load
search_box.send_keys(Keys.ENTER)
time.sleep(3)
#click on Generate button
driver.find_element(By.ID,"generateDocument").click()
time.sleep(10)
print("SOA data is fetched successfully")
#select the NOC certificate
wait = WebDriverWait(driver, 10)
# Step 1: Click the Select2 dropdown to open it
dropdown = wait.until(EC.element_to_be_clickable((By.XPATH, "/html/body/div[1]/div/section/div[1]/div/div/div[2]/div[2]/div[2]/div/span/span[1]/span/span[1]")))
dropdown.click()
# Step 2: Wait for the dropdown options to be visible
search_box = wait.until(EC.visibility_of_element_located((By.XPATH, "/html/body/span/span/span[1]/input")))
# Step 3: Type the option you want to select
search_box.send_keys("NOC")
# slight wait for options to load
search_box.send_keys(Keys.ENTER)
time.sleep(3)
#click on the generate button
driver.find_element(By.ID,"generateDocument").click()
time.sleep(10)
print("NOC certificate data is fetched successfully")
#click on the popup
driver.find_element(By.XPATH,"/html/body/div[6]/div[2]/div/div/div/div/div/div/div").click()
#click on the close button in the popup
driver.find_element(By.XPATH,"/html/body/div[6]/div[2]/div/div/div/div/div/div/div/div[4]/button").click()
print("Popup is being closed for NOC")

# click on the logout button
driver.find_element(By.XPATH, "//a[normalize-space()='Sign out']").click()
print("the bm dashboard is successfully logout")
