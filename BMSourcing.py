#BM Sourcing (Till Client) (One Challenge- OTP send to mobile number cant be automated)
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

#select the Client Sourcing Section
driver.find_element(By.XPATH,"/html/body/div[1]/aside/section/ul/li[2]/ul/li[9]/a/span").click()
time.sleep(2)
#click on Add client module
driver.find_element(By.XPATH,"/html/body/div[1]/aside/section/ul/li[2]/ul/li[9]/ul/li[1]/a").click()
driver.implicitly_wait(3)
#select the staff dropdown and select "Fet1005" user
wait = WebDriverWait(driver, 10)

# Step 1: Click the Select2 dropdown to open it
dropdown = wait.until(EC.element_to_be_clickable((By.ID, "select2-staffId-container")))
dropdown.click()

# Step 2: Wait for the dropdown options to be visible
search_box = wait.until(EC.visibility_of_element_located((By.XPATH, "/html/body/span/span/span[1]/input")))
# Step 3: Type the option you want to select
search_box.send_keys("fet1005")
time.sleep(4)  # slight wait for options to load
search_box.send_keys(Keys.ENTER)

#select the Center Name from the Dropdown
wait = WebDriverWait(driver, 10)
# 1. Click on the "Select Center" dropdown
center_dropdown = wait.until(EC.element_to_be_clickable((By.ID, "select2-centerId-container")))
center_dropdown.click()
# 2. Type the center name into the search box
search_box = wait.until(EC.presence_of_element_located((By.XPATH, "//input[@class='select2-search__field']")))
search_box.send_keys("April")  # <-- replace with actual center name
# 3. Select the option from the results
option = wait.until(EC.element_to_be_clickable((By.XPATH, "//li[contains(@class,'select2-results__option') and text()='April']")))
option.click()
print("center is selected")
#click onto the Add New Client button
driver.find_element(By.XPATH,"/html/body/div[1]/div/section/div[2]/div/div/div[2]/div[4]/button").click()
time.sleep(3)
#select the Client image
wait = WebDriverWait(driver, 10)
file_input = wait.until(EC.presence_of_element_located((By.ID, "imageUpload")))
# Make the input element visible
driver.execute_script("arguments[0].style.display = 'block';", file_input)
driver.execute_script("arguments[0].style.visibility = 'visible';", file_input)
driver.execute_script("arguments[0].style.opacity = '1';", file_input)
# Send the file path directly to the input element
file_input.send_keys(r"C:\Users\Abhishek Yadav\Pictures\ImagesBMSourcing\image.jpeg")
# Just to observe the preview update
print("image path is selected successfully")
time.sleep(3)
#Enter data in the aadhaar and select the KYC images back and front
#select the primary KYC field section
driver.find_element(By.XPATH,"/html/body/div[1]/div/section/div[2]/div/div/div[2]/div[2]").click()
driver.find_element(By.ID,"primaryKYCNumber").click()
driver.find_element(By.ID,"primaryKYCNumber").send_keys("997979991669")
time.sleep(2)
#click on the aadhaar verification button
driver.find_element(By.ID,"verifyAadhaarButton").click()
#click on the popup
driver.find_element(By.XPATH,"/html/body/div[6]/div[2]/div/div/div/div/div/div/div/div[2]").click()
time.sleep(2)
driver.find_element(By.XPATH,"/html/body/div[6]/div[2]/div/div/div/div/div/div/div/div[4]/button").click()
#select the Back and Front aadhaar image
wait = WebDriverWait(driver, 10)
file_input = wait.until(EC.presence_of_element_located((By.ID, "primaryKYCFrontInput")))
# Make the input element visible
driver.execute_script("arguments[0].style.display = 'block';", file_input)
driver.execute_script("arguments[0].style.visibility = 'visible';", file_input)
driver.execute_script("arguments[0].style.opacity = '1';", file_input)
# Send the file path directly to the input element
file_input.send_keys(r"C:\Users\Abhishek Yadav\Pictures\ImagesBMSourcing\Aadhaar front.jpeg")
# Just to observe the preview update
print("Aadhaar front image path is selected successfully")
time.sleep(3)
#click on the popup after uploading the Front Image
driver.find_element(By.XPATH,"/html/body/div[6]/div[2]/div/div/div/div/div/div/div/div[2]").click()
time.sleep(1)
#click on close button
driver.find_element(By.XPATH,"/html/body/div[6]/div[2]/div/div/div/div/div/div/div/div[4]/button").click()
time.sleep(2)

#select the aadhaar back image
wait = WebDriverWait(driver, 10)
file_input = wait.until(EC.presence_of_element_located((By.ID, "primaryKYCBackInput")))
# Make the input element visible
driver.execute_script("arguments[0].style.display = 'block';", file_input)
driver.execute_script("arguments[0].style.visibility = 'visible';", file_input)
driver.execute_script("arguments[0].style.opacity = '1';", file_input)
# Send the file path directly to the input element
file_input.send_keys(r"C:\Users\Abhishek Yadav\Pictures\ImagesBMSourcing\AADHAAR back.jpg")
# Just to observe the preview update
print("Aadhaar Back image path is selected successfully")
time.sleep(7)
#select the Secondary KYC as PAN from the Dropdown

dropdown = Select(driver.find_element(By.ID, "secondaryKYC"))
dropdown.select_by_value('1422')
time.sleep(4)
print("Secondary KYC is selected")

#Enter the PAN number
driver.find_element(By.ID,"secondaryKYCNumber").click()
driver.find_element(By.ID,"secondaryKYCNumber").send_keys("BEKPA7980N")
time.sleep(2)
#scroll down to check further
scroll_pause_time = 1  # Pause time between scrolls
scroll_height = driver.execute_script("return document.body.scrollHeight")

current_position = 0
increment = 50  # Number of pixels to scroll each time

while current_position < scroll_height:
    driver.execute_script(f"window.scrollTo(0, {current_position});")
    time.sleep(scroll_pause_time)
    current_position += increment
    scroll_height = driver.execute_script("return document.body.scrollHeight")  # update in case it changes

#select the Pan Back and Front images
wait = WebDriverWait(driver, 10)
file_input = wait.until(EC.presence_of_element_located((By.ID, "secondaryKYCFrontInput")))
# Make the input element visible
driver.execute_script("arguments[0].style.display = 'block';", file_input)
driver.execute_script("arguments[0].style.visibility = 'visible';", file_input)
driver.execute_script("arguments[0].style.opacity = '1';", file_input)
# Send the file path directly to the input element
file_input.send_keys(r"C:\Users\Abhishek Yadav\Pictures\ImagesBMSourcing\pan-card-front.jpg")
# Just to observe the preview update
print("Pan front image path is selected successfully")
time.sleep(3)
#select the Pan Back Image
wait = WebDriverWait(driver, 10)
file_input = wait.until(EC.presence_of_element_located((By.ID, "secondaryKYCBackInput")))
# Make the input element visible
driver.execute_script("arguments[0].style.display = 'block';", file_input)
driver.execute_script("arguments[0].style.visibility = 'visible';", file_input)
driver.execute_script("arguments[0].style.opacity = '1';", file_input)
# Send the file path directly to the input element
file_input.send_keys(r"C:\Users\Abhishek Yadav\Pictures\ImagesBMSourcing\pan-card-back.jpg")
# Just to observe the preview update
print("Pan Back image path is selected successfully")
time.sleep(3)
#click on Borrowers basic details section
driver.find_element(By.XPATH,"/html/body/div[1]/div/section/div[3]/div/div/div[1]/div").click()
#Enter First and Last name
driver.find_element(By.ID,"firstName").click()
driver.find_element(By.ID,"firstName").send_keys("Sita")
driver.find_element(By.ID,"lastName").click()
driver.find_element(By.ID,"lastName").send_keys("Debi")
#select DOB
dob_input_str = "08/21/1991"
dob_iso = datetime.strptime(dob_input_str, "%m/%d/%Y").strftime("%m/%d/%Y")

wait = WebDriverWait(driver, 10)
elem = wait.until(EC.element_to_be_clickable((By.ID, "dob")))

# clear and type ISO string (you may need to send Keys.TAB to close picker)
elem.clear()
elem.send_keys(dob_iso)
print("dob is selected")

#elem.send_keys(Keys.TAB)
#click on the Mobile no field
driver.find_element(By.ID,"mobileNumber").click()
driver.find_element(By.ID,"mobileNumber").send_keys("9051910924")
#click on the Mobile Verification number
driver.find_element(By.ID,"verifyMobileButton").click()
time.sleep(4)
#click on the popup
driver.find_element(By.XPATH,"/html/body/div[1]/div/section/div[2]/div/div/div[2]/div[3]/div/div[1]/h3").click()
#enter OTP
driver.implicitly_wait(15)
#click on verify button
#driver.find_element(By.ID,"verifyOtpButtonMSG91").click()
#click on the Popup
#driver.find_element(By.XPATH,"/html/body/div[6]/div[2]/div/div/div/div/div/div/div/div[2]").click()
#click on the Close button
driver.find_element(By.XPATH,"/html/body/div[1]/div/section/div[2]/div/div/div[2]/div[3]/div/div[1]/span").click()
time.sleep(7)
#scroll down
scroll_pause_time = 1  # Pause time between scrolls
scroll_height = driver.execute_script("return document.body.scrollHeight")

current_position = 0
increment = 100  # Number of pixels to scroll each time

while current_position < scroll_height:
    driver.execute_script(f"window.scrollTo(0, {current_position});")
    time.sleep(scroll_pause_time)
    current_position += increment
    scroll_height = driver.execute_script("return document.body.scrollHeight")  # update in case it changes
#slect married from the dropdown
wait = WebDriverWait(driver, 10)
# Step 1: Click the Select2 container to open dropdown
select2_container = wait.until(EC.element_to_be_clickable((By.ID, "select2-maritalStatus-container")))
select2_container.click()
# Step 2: Wait for dropdown options to appear and select "Married"
married_option = wait.until(EC.element_to_be_clickable((By.XPATH, "//li[contains(text(),'Married')]")))
married_option.click()
print("martial status us selected")
#enter Mother name
driver.find_element(By.ID,"motherName").click()
driver.find_element(By.ID,"motherName").send_keys("Dhara Debi")
#enter mother age
driver.find_element(By.ID,"motherAge").click()
driver.find_element(By.ID,"motherAge").send_keys("70")
#select the Religion
wait = WebDriverWait(driver, 10)
# Step 1: Click the Select2 container for Religion
religion_container = wait.until(EC.element_to_be_clickable((By.ID, "select2-clientReligion-container")))
religion_container.click()
# Step 2: Wait for dropdown options to load and select "Hindu"
hindu_option = wait.until(EC.element_to_be_clickable((By.XPATH, "//li[contains(text(),'Hindu')]")))
hindu_option.click()
print("Religion is selected")

#select the caste as OBC
wait = WebDriverWait(driver, 10)
# Step 1: Click the Select2 container for Caste
caste_container = wait.until(EC.element_to_be_clickable((By.ID, "select2-clientCaste-container")))
caste_container.click()
# Step 2: Wait for dropdown options and click "OBC"
obc_option = wait.until(EC.element_to_be_clickable((By.XPATH, "//li[contains(text(),'OBC')]")))
obc_option.click()
print("Caste is Selected")
time.sleep(3)

#Select the income details section
driver.find_element(By.XPATH,"/html/body/div[1]/div/section/div[4]/div/div/div[1]/div").click()
#select Dairy as Main Income from DD
wait = WebDriverWait(driver, 10)
# Step 1: Click the Select2 container for Income Source
income_source_container = wait.until(EC.element_to_be_clickable((By.ID, "select2-mainIncomeSource-container")))
income_source_container.click()
# Step 2: Wait for dropdown options and select "Dairy"
dairy_option = wait.until(EC.element_to_be_clickable((By.XPATH, "//li[contains(text(),'Dairy')]")))
dairy_option.click()
print("Main Income Type is selected")
time.sleep(2)

#Enter Main income amount
driver.find_element(By.ID,"mainIncomeAmount").click()
driver.find_element(By.ID,"mainIncomeAmount").send_keys("10000")
#click on the Permanent address section
driver.find_element(By.XPATH,"/html/body/div[1]/div/section/div[5]/div/div/div[1]/div/h1").click()
driver.find_element(By.ID,"addressLine1").click()
driver.find_element(By.ID,"addressLine1").send_keys("133 Sarth Bai Lane Ambawadi Ahmedabad")
#enter village
driver.find_element(By.ID,"village").click()
driver.find_element(By.ID,"village").send_keys("Sanand")
#enter city
driver.find_element(By.ID,"city").click()
driver.find_element(By.ID,"city").send_keys("Ahmedabad")
#enter pincode
driver.find_element(By.ID,"pincode").click()
driver.find_element(By.ID,"pincode").send_keys("380057")
#select the state from the dropdown
wait = WebDriverWait(driver, 10)
# Step 1: Click the Select2 container for State
state_container = wait.until(EC.element_to_be_clickable((By.ID, "select2-state-container")))
state_container.click()
# Step 2: Wait for dropdown options and select "Gujarat"
gujarat_option = wait.until(EC.element_to_be_clickable((By.XPATH, "//li[contains(text(),'Gujarat')]")))
gujarat_option.click()
print("State is selected from the dropdown")
time.sleep(3)
#select district as ahmedabad from DD
wait = WebDriverWait(driver, 10)
# Step 1: Click the Select2 container for District
district_container = wait.until(EC.element_to_be_clickable((By.ID, "select2-district-container")))
district_container.click()
# Step 2: Wait for dropdown options and select "Ahmedabad"
ahmedabad_option = wait.until(EC.element_to_be_clickable((By.XPATH, "//li[contains(text(),'Ahmedabad')]")))
ahmedabad_option.click()
print("District is being selected")
time.sleep(2)

#select the Taluka
wait = WebDriverWait(driver, 10)
# Step 1: Click the Select2 container for Taluka
taluka_container = wait.until(EC.element_to_be_clickable((By.ID, "select2-taluka-container")))
taluka_container.click()
# Step 2: Wait for dropdown options and select "Barwala"
barwala_option = wait.until(EC.element_to_be_clickable((By.XPATH, "//li[contains(text(),'Barwala')]")))
barwala_option.click()
print("Taluka is selected")
time.sleep(2)
#click on the current address section
driver.find_element(By.XPATH,"/html/body/div[1]/div/section/div[6]/div/div/div[1]/div[1]").click()
#click on the same as permanent checkbox
driver.find_element(By.XPATH,"/html/body/div[1]/div/section/div[6]/div/div/div[1]/div[3]/input").click()
#click on the Submit button
driver.find_element(By.ID,"submitBorrowerButton").click()
driver.implicitly_wait(4)

#click on the popup
driver.find_element(By.XPATH,"/html/body/div[6]/div[2]/div/div/div/div/div/div/div/div[2]").click()
driver.implicitly_wait(4)

#click on the close button in popup
driver.find_element(By.XPATH,"/html/body/div[6]/div[2]/div/div/div/div/div/div/div/div[4]/button").click()
time.sleep(3)
print("final popup is closed")

#scroll up functionality
scroll_pause_time = 1  # pause time between scrolls
scroll_height = driver.execute_script("return document.body.scrollHeight")

# Start from the bottom
current_position = scroll_height
increment = 500  # pixels to scroll each time

while current_position > 0:
    driver.execute_script(f"window.scrollTo(0, {current_position});")
    time.sleep(scroll_pause_time)
    current_position -= increment
    if current_position < 0:
        current_position = 0  # avoid negative value



#click on the logout button
driver.find_element(By.XPATH,"//a[normalize-space()='Sign out']").click()
print("the bm dashboard is successfully logout")
