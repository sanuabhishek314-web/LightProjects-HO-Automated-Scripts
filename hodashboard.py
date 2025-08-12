from os import link
from selenium.webdriver.common.keys import Keys
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver import Keys
import time

from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Chrome()
driver.get("https://uat-new-ho.lightmicrofinance.com/")
driver.maximize_window()
driver.implicitly_wait(4)
driver.find_element(By.XPATH,"//input[@id='username']").send_keys("LMF09496")
driver.find_element(By.XPATH,"//input[@id='password']").send_keys("Sanuabhishek$#@050392")
driver.find_element(By.ID,"login_button").click()
time.sleep(11)
#Alert Code for switching to popup
alert=driver.switch_to.alert
print(alert.text)
alert.accept()

#Select the DBT module
driver.find_element(By.XPATH, "//a[@onclick=\"link('../dbt_module/index.php')\"]").click()

#click on the DBT section
driver.find_element(By.XPATH,"//iframe[@id='link']").click()
time.sleep(4)
#click on the client text field
searchbox=driver.find_element(By.ID,"clientId").click()
driver.find_element(By.XPATH,"//iframe[@id='link']").send_keys("758226")
time.sleep(2)
searchbox.send_keys("Enter"+Keys.ENTER)




#driver.find_element(By.XPATH,"/html[1]/body[1]/div[1]/div[1]/div[1]/div[2]/div[4]/a[1]").click()
#driver.find_element(By.XPATH,"//input[@id='clientId']").click()
#driver.find_element(By.XPATH,"//input[@id='clientId']").send_keys("758240")
#time.sleep(2)
#driver.find_element(By.XPATH,"//input[@id='clientId']").send_keys(Keys.ENTER)
#click on the Submit button
#driver.find_element(By.ID,"btnSubmit").click()


#Select the E-Sign Download Module
#driver.find_element(By.XPATH,"//a[normalize-space()='E-Sign Downloads']").click()
time.sleep(3)

#Select the NEFT module and select the Client Data
#driver.find_element(By.XPATH,"/html[1]/body[1]/div[1]/div[1]/div[1]/div[2]/div[22]/a[1]").click()
#driver.implicitly_wait(5)
#click on the white space

#driver.find_element(By.XPATH,"//body").click()
#click on the Grid
#driver.find_element(By.XPATH,"//tbody/tr[1]/td[6]").click()

#click on the search field
#driver.find_element(By.XPATH,"//input[@type='search']").click()
#driver.implicitly_wait(3)
#driver.find_element(By.XPATH,"/html[1]/body[1]/div[2]/div[1]/div[1]/div[1]/div[1]/div[1]/div[2]/div[1]/label[1]/input[1]").send_keys('bulk')
#time.sleep(3)
#click on the download button
#driver.find_element(By.XPATH,"//tbody/tr[1]/td[6]/a[1]/i[1]").click()
#time.sleep(18)







#select the Start Date field
#driver.find_element(By.XPATH,"/html[1]/body[1]/div[1]/div[1]/section[1]/form[1]/div[1]/div[3]/div[1]/div[1]/input[1]").click()
#client on triangle button to move back
#driver.find_element(By.XPATH,"//span[@class='ui-icon ui-icon-circle-triangle-w']").click()
#time.sleep(2)

#select the Date
#driver.find_element(By.XPATH,"//a[@class='ui-state-default ui-state-hover']").click()
#select the end date field
#driver.find_element(By.XPATH,"//input[@id='endDate']").click()
#time.sleep(2)
#select the End Date
#driver.find_element(By.XPATH,"//a[@class='ui-state-default ui-state-highlight ui-state-hover']").click()
#click on the search button
#driver.find_element(By.XPATH,"//button[@id='fetchButton']").click()



#Logout user Code
driver.find_element(By.XPATH,"//a[normalize-space()='Logout']").click()
print("Ho Dashboard is successfully logged out")

