#Add Reference Mobile Number and Branch Performance (Collection DB, BM Dashboard, Cluster DB, Division DB)
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

#select the Client Sourcing Section
driver.find_element(By.XPATH,"/html/body/div[1]/aside/section/ul/li[2]/ul/li[9]/a/span").click()
time.sleep(2)

#click on the Add Reference Mobile Number
driver.find_element(By.XPATH,"/html/body/div[1]/aside/section/ul/li[2]/ul/li[9]/ul/li[3]/a").click()
time.sleep(2)
#select the Center the from the Dropdown
wait = WebDriverWait(driver, 10)
# Click on the Select2 dropdown
center_dropdown = wait.until(EC.element_to_be_clickable((By.ID, "select2-centerId-container")))
center_dropdown.click()
# Now select the desired option (example: "Ahmedabad Center")
option_to_select = wait.until(EC.element_to_be_clickable((By.XPATH, "//li[contains(text(),'April')]")))
option_to_select.click()

print("Center selected successfully!")

#select the client from the Dropdown
wait = WebDriverWait(driver, 15)

# Step 1: Click only the Client dropdown (using its container ID parent)
client_dropdown = wait.until(EC.element_to_be_clickable((By.XPATH, "//span[@id='select2-clientId-container']/ancestor::span[@class='select2-selection select2-selection--single']")))
client_dropdown.click()
# Step 2: Search for "Ishan Patil"
search_input = wait.until(EC.presence_of_element_located((By.XPATH, "//input[@class='select2-search__field']")))
search_input.send_keys("Ishan Patil")
# Step 3: Select the correct option
option = wait.until(EC.element_to_be_clickable((By.XPATH, "//li[contains(text(),'Ishan Patil')]")))
option.click()
print("✅ Client is being selected successfully.")

#click onto the Submit button
driver.find_element(By.XPATH,"/html/body/div[1]/div/section/div[2]/div/div/div[2]/div[4]/button").click()
time.sleep(4)
#click on the Client Section
driver.find_element(By.XPATH,"/html/body/div[1]/div/section/div[2]/div/div/div[3]/div[1]").click()
#click on the Edit button of the 1st added data
driver.find_element(By.ID,"openUpdate-1").click()
driver.implicitly_wait(4)
#click on the Person Name field
driver.find_element(By.ID,"personName-1").click()
driver.find_element(By.ID,"personName-1").send_keys("Kunal")
#click on the Update Button
driver.find_element(By.ID,"edit-1").click()
time.sleep(4)
#click on the Popup
driver.find_element(By.XPATH,"/html/body/div[6]/div[2]/div/div/div/div/div/div/div").click()
#click on the Close button in the popup
driver.find_element(By.XPATH,"/html/body/div[6]/div[2]/div/div/div/div/div/div/div/div[4]/button").click()
time.sleep(3)
print("Reference Data is being Updated successfully")
driver.refresh()

#select the Branch Performance Section
driver.find_element(By.XPATH,"/html/body/div/aside/section/ul/li[2]/ul/li[10]/a/span").click()
time.sleep(3)
#click on the Collection Dashboard
driver.find_element(By.XPATH,"/html/body/div[1]/aside/section/ul/li[2]/ul/li[10]/ul/li[1]/a").click()
driver.implicitly_wait(8)
driver.refresh()
print("Collection Dashboard is displayed")
#click on the Dashboard on the top
driver.find_element(By.XPATH,"/html/body/div/header/a/span[2]").click()
time.sleep(3)
#Expand Branch Performance Again
wait = WebDriverWait(driver, 20)
driver.find_element(By.XPATH,"//span[normalize-space()='Branch Performance']").click()
time.sleep(2)

#click on the BM Dashboard
driver.find_element(By.XPATH,"/html/body/div[1]/aside/section/ul/li[2]/ul/li[10]/ul/li[2]/a").click()
time.sleep(2)
#click on the BM dashboard section
driver.find_element(By.XPATH,"/html/body/div[1]/div/section/div[2]/div/div/table/tbody/tr[1]/td[2]").click()
#click on the Info Icon
driver.find_element(By.XPATH,"/html/body/div[1]/div/section/div[2]/div/div/table/tbody/tr[1]/td[2]/span").click()
time.sleep(3)
print("BM Dashboard Data is being Displayed")
#Expand Branch Performance Again
driver.find_element(By.XPATH,"/html/body/div/aside/section/ul/li[2]/ul/li[10]/a/span").click()
time.sleep(2)
#select the Cluster Dashboard
driver.find_element(By.XPATH,"/html/body/div[1]/aside/section/ul/li[2]/ul/li[10]/ul/li[3]/a").click()
time.sleep(3)
#click on the Cluster section
driver.find_element(By.XPATH,"/html/body/div[1]/div/section/div[2]/div/div/table/tbody/tr[2]/td[3]").click()
#click on the Info Icon
driver.find_element(By.XPATH,"/html/body/div[1]/div/section/div[2]/div/div/table/tbody/tr[2]/td[3]/span").click()
driver.implicitly_wait(2)
print("Cluster Dashboard data is being displayed")
driver.refresh()
#Expand Branch Performance Again
driver.find_element(By.XPATH,"/html/body/div/aside/section/ul/li[2]/ul/li[10]/a/span").click()
time.sleep(2)
#select the division dashboard
driver.find_element(By.XPATH,"/html/body/div[1]/aside/section/ul/li[2]/ul/li[10]/ul/li[4]/a").click()
#select the division section
driver.find_element(By.XPATH,"/html/body/div[1]/div/section/div[2]/div/div/table/tbody/tr[2]/td[2]").click()
#click on the info icon
driver.find_element(By.XPATH,"/html/body/div[1]/div/section/div[2]/div/div/table/tbody/tr[2]/td[2]/span").click()
time.sleep(2)
print("Division dashboard data is being displayed")



#click on the logout button
driver.find_element(By.XPATH,"//a[normalize-space()='Sign out']").click()
print("the bm dashboard is successfully logout")
