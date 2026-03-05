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
driver.find_element(By.NAME,"inputUsername").send_keys("BMT1009")
driver.find_element(By.ID,"inputPassword").click()
driver.find_element(By.NAME,"inputPassword").send_keys("Light@123")
driver.find_element(By.XPATH,"//button[@type='submit']").click()
time.sleep(11)

#select the Reports section
driver.find_element(By.XPATH,"/html[1]/body[1]/div[1]/aside[1]/section[1]/ul[1]/li[2]/ul[1]/li[4]/a[1]/span[1]").click()
time.sleep(3)
#click on Reports
driver.find_element(By.XPATH,"//a[@href='view_reports.php']").click()
time.sleep(2)
#Now click onto the reports section
driver.find_element(By.XPATH,"/html[1]/body[1]/div[1]/div[1]/section[1]/div[2]/div[1]/div[1]").click()
time.sleep(3)
#click on search field
wait = WebDriverWait(driver, 10)
search_box = wait.until(EC.presence_of_element_located((By.XPATH, "/html[1]/body[1]/div[1]/div[1]/section[1]/div[2]/div[1]/div[1]/div[2]/label[1]/input[1]")))
search_box.send_keys("Client Details")
print("Client Details filtered")

#click onto the filter icon
driver.find_element(By.XPATH,"/html[1]/body[1]/div[1]/div[1]/section[1]/div[2]/div[1]/div[1]/table[1]/tbody[1]/tr[1]/td[3]/button[1]/i[1]").click()
time.sleep(4)
#click on the popup
driver.find_element(By.XPATH,"/html/body/div[1]/div/section/div[3]/div[7]/div/div/div[2]").click()
time.sleep(2)
#select from date
driver.find_element(By.XPATH,"/html/body/div[1]/div/section/div[3]/div[7]/div/div/div[2]/form/div/div[1]/input").click()
#click on back icon
driver.find_element(By.XPATH,"/html/body/div[5]/div/a[1]/span").click()
time.sleep(2)
#select the date
driver.find_element(By.XPATH,"/html/body/div[5]/table/tbody/tr[1]/td[1]/a").click()
#now click on To Date section
driver.find_element(By.XPATH,"/html/body/div[1]/div/section/div[3]/div[7]/div/div/div[2]/form/div/div[2]/input").click()
#select the calender
driver.find_element(By.XPATH,"/html/body/div[5]/div/div").click()
#select the to date from calender
driver.find_element(By.XPATH,"/html/body/div[5]/table/tbody/tr[1]/td[3]/a").click()
#click on downlaod report
driver.find_element(By.XPATH,"/html/body/div[1]/div/section/div[3]/div[7]/div/div/div[3]/button[2]").click()
time.sleep(4)
print("Report downloaded successfully")
#click on the Close ICOn
driver.find_element(By.XPATH,"/html/body/div[1]/div/section/div[3]/div[7]/div/div/div[1]/button/span").click()
search_box.clear()
search_box.send_keys("Client Wise Due")
print("Client Wise Due filtered")
#click on filter icon again
driver.find_element(By.XPATH,"/html[1]/body[1]/div[1]/div[1]/section[1]/div[2]/div[1]/div[1]/table[1]/tbody[1]/tr[1]/td[3]/button[1]/i[1]").click()
#click on the popup
driver.find_element(By.XPATH,"/html/body/div[1]/div/section/div[3]/div[6]/div/div/div[1]").click()
#click on To Date
driver.find_element(By.XPATH,"/html/body/div[1]/div/section/div[3]/div[6]/div/div/div[2]/form/div/div[1]/input").click()
#click on date calender
driver.find_element(By.XPATH,"/html/body/div[5]/div/div").click()
#click on back button in calender
driver.find_element(By.XPATH,'/html/body/div[5]/div/a[1]/span').click()
#select the date
driver.find_element(By.XPATH,"/html/body/div[5]/table/tbody/tr[1]/td[1]/a").click()
#click on download report
driver.find_element(By.XPATH,"/html/body/div[1]/div/section/div[3]/div[6]/div/div/div[3]/button[2]").click()
time.sleep(5)
print("Report downloaded successfully")
#click on close icon
driver.find_element(By.XPATH,"/html/body/div[1]/div/section/div[3]/div[6]/div/div/div[1]/button/span").click()
time.sleep(2)
search_box.clear()
search_box.send_keys("Daily Expected Disbursement")
#click on filter icon
driver.find_element(By.XPATH,'/html/body/div[1]/div/section/div[2]/div/div/table/tbody/tr/td[3]/button/i').click()
#click on the popup
driver.find_element(By.XPATH,'/html/body/div[1]/div/section/div[3]/div[2]/div/div/div[1]').click()
time.sleep(2)
#click on to date
driver.find_element(By.XPATH,"/html/body/div[1]/div/section/div[3]/div[2]/div/div/div[2]/form/div/div[1]/input").click()
#Click on calender
driver.find_element(By.XPATH,"/html/body/div[5]/div/div").click()
#click on back icon
driver.find_element(By.XPATH,"/html/body/div[5]/div/a[1]/span").click()
time.sleep(2)
#selecr the date
driver.find_element(By.XPATH,"/html/body/div[5]/table/tbody/tr[1]/td[1]/a").click()
time.sleep(2)
#click on Download Report button
driver.find_element(By.XPATH,"/html/body/div[1]/div/section/div[3]/div[2]/div/div/div[3]/button[2]").click()
print("Report Downloaded")
#click on close icon
driver.find_element(By.XPATH,"/html/body/div[1]/div/section/div[3]/div[2]/div/div/div[1]/button/span").click()
search_box.clear()
time.sleep(3)

search_box.send_keys("High Ticket All DD Date")

#click on filter icon
driver.find_element(By.XPATH,'/html/body/div[1]/div/section/div[2]/div/div/table/tbody/tr/td[3]/button/i').click()
time.sleep(4)
#click on the popup
driver.find_element(By.XPATH,'/html/body/div[1]/div/section/div[3]/div[5]/div/div/div[1]').click()
time.sleep(4)
#click on to date
driver.find_element(By.XPATH,"/html/body/div[1]/div/section/div[3]/div[5]/div/div/div[2]/form/div/div[1]/input").click()
#Click on calender
driver.find_element(By.XPATH,"/html/body/div[5]/div/div").click()
#click on back icon
driver.find_element(By.XPATH,"/html/body/div[5]/div/a[1]/span").click()
time.sleep(2)
#selecr the date
driver.find_element(By.XPATH,"/html/body/div[5]/table/tbody/tr[1]/td[1]/a").click()
time.sleep(5)
#click on Download Report button
driver.find_element(By.XPATH,"/html/body/div[1]/div/section/div[3]/div[5]/div/div/div[3]/button[2]").click()
print("Report Downloaded")
time.sleep(4)
#click on close icon
driver.find_element(By.XPATH,"/html/body/div[1]/div/section/div[3]/div[5]/div/div/div[1]/button/span").click()
time.sleep(3)
search_box.clear()

#search_box.send_keys("Loan Details")
#click on filter icon
#driver.find_element(By.XPATH,'/html/body/div[1]/div/section/div[2]/div/div/table/tbody/tr/td[3]/button/i').click()
#click on the popup
#driver.find_element(By.XPATH,'/html/body/div[1]/div/section/div[3]/div[7]/div/div/div[1]').click()
#time.sleep(3)
#click on to date
#driver.find_element(By.XPATH,"/html/body/div[1]/div/section/div[3]/div[7]/div/div/div[2]/form/div/div[1]/input").click()
#Click on calender
#driver.find_element(By.XPATH,"/html/body/div[5]/div/div").click()
#click on back icon
#driver.find_element(By.XPATH,"/html/body/div[5]/div/a[1]/span").click()
#time.sleep(2)
#selecr the date
#driver.find_element(By.XPATH,"/html/body/div[5]/table/tbody/tr[1]/td[1]/a").click()
#time.sleep(4)
#click on Download Report button
#driver.find_element(By.XPATH,"/html/body/div[1]/div/section/div[3]/div[7]/div/div/div[3]/button[2]").click()
#print("Report Downloaded")
#time.sleep(4)
#click on close icon
#driver.find_element(By.XPATH,"/html/body/div[1]/div/section/div[3]/div[2]/div/div/div[1]/button/span").click()

#search_box.clear()
time.sleep(2)

search_box.send_keys("Loan Submitted Client Wise")

#click on filter icon
driver.find_element(By.XPATH,'/html/body/div[1]/div/section/div[2]/div/div/table/tbody/tr/td[3]/button/i').click()
time.sleep(4)
#click on the popup
driver.find_element(By.XPATH,'/html/body/div[1]/div/section/div[3]/div[1]/div/div/div[1]').click()
time.sleep(2)
#click on to date
driver.find_element(By.XPATH,"/html/body/div[1]/div/section/div[3]/div[1]/div/div/div[2]/form/div/div[1]/input").click()
#Click on calender
driver.find_element(By.XPATH,"/html/body/div[5]/div/div").click()
#click on back icon
driver.find_element(By.XPATH,"/html/body/div[5]/div/a[1]/span").click()
time.sleep(2)
#selecr the date
driver.find_element(By.XPATH,"/html/body/div[5]/table/tbody/tr[1]/td[1]/a").click()
time.sleep(5)
#click on Download Report button
driver.find_element(By.XPATH,"/html/body/div[1]/div/section/div[3]/div[1]/div/div/div[3]/button[2]").click()
print("Report Downloaded")
time.sleep(4)
#click on close button in popup
driver.find_element(By.XPATH,"/html/body/div[1]/div/section/div[3]/div[1]/div/div/div[3]/button[1]").click()
time.sleep(3)
search_box.clear()

search_box.send_keys("QR And CB Entry Verification")
print("Data is being filtered")
#click on filter icon
driver.find_element(By.XPATH,'/html/body/div[1]/div/section/div[2]/div/div/table/tbody/tr/td[3]/button/i').click()
#click on the popup
driver.find_element(By.XPATH,'/html/body/div[1]/div/section/div[3]/div[3]/div/div/div[2]/form').click()
time.sleep(2)
#click on to date
driver.find_element(By.XPATH,"/html/body/div[1]/div/section/div[3]/div[3]/div/div/div[2]/form/div/div[1]/input").click()
#Click on calender
driver.find_element(By.XPATH,"/html/body/div[5]/div/div/span[2]").click()
#click on back icon
driver.find_element(By.XPATH,"/html/body/div[5]/div/a[1]/span").click()
time.sleep(3)
#selecr the date
driver.find_element(By.XPATH,"/html/body/div[5]/table/tbody/tr[1]/td[1]/a").click()
time.sleep(5)
#click on Download Report button
driver.find_element(By.XPATH,"/html/body/div[1]/div/section/div[3]/div[3]/div/div/div[3]/button[2]").click()
print("Report Downloaded")
time.sleep(5)
#click on close button
driver.find_element(By.XPATH,"/html/body/div[1]/div/section/div[3]/div[3]/div/div/div[3]/button[1]").click()
time.sleep(3)
search_box.clear()

search_box.send_keys("Regular Transaction Data")
print("Data is being filtered")
#click on filter icon
driver.find_element(By.XPATH,'/html/body/div[1]/div/section/div[2]/div/div/table/tbody/tr/td[3]/button/i').click()
#click on the popup
driver.find_element(By.XPATH,'/html/body/div[1]/div/section/div[3]/div[4]/div/div/div[2]/form').click()
time.sleep(3)
#click on to date
driver.find_element(By.XPATH,"/html/body/div[1]/div/section/div[3]/div[4]/div/div/div[2]/form/div/div[1]/input").click()
#Click on calender
driver.find_element(By.XPATH,"/html/body/div[5]/div/div/span[1]").click()
#click on back icon
driver.find_element(By.XPATH,"/html/body/div[5]/div/a[1]/span").click()
time.sleep(2)
#selecr the date
driver.find_element(By.XPATH,"/html/body/div[5]/table/tbody/tr[1]/td[1]/a").click()
time.sleep(5)
#click on Download Report button
driver.find_element(By.XPATH,"/html/body/div[1]/div/section/div[3]/div[4]/div/div/div[3]/button[2]").click()
print("Report Downloaded")
time.sleep(4)
#click on close button
driver.find_element(By.XPATH,"/html/body/div[1]/div/section/div[3]/div[4]/div/div/div[3]/button[1]").click()
time.sleep(4)
search_box.clear()
# CLick on dashboard
driver.find_element(By.XPATH,"/html/body/div[1]/header/a/span[2]").click()
#select the reports again
#Expand Reports section
driver.find_element(By.XPATH,"/html/body/div[1]/aside/section/ul/li[2]/ul/li[4]/a/span").click()
time.sleep(2)
#click on reports
driver.find_element(By.XPATH,"/html/body/div[1]/aside/section/ul/li[2]/ul/li[4]/ul/li/a").click()
time.sleep(2)
#click on the reports section
driver.find_element(By.XPATH,"/html/body/div[1]/div/section/div[2]/div/div").click()
time.sleep(3)
print("Reports is being selected again")
wait=WebDriverWait(driver,10)
search_box2=wait.until(EC.presence_of_element_located((By.XPATH,"/html/body/div[1]/div/section/div[2]/div/div/div[2]/label/input")))
search_box2.send_keys("Staff Wise Portfolio")
time.sleep(3)
print("Clicked on Filter button")
#click on filter icon
driver.find_element(By.XPATH,'/html/body/div[1]/div/section/div[2]/div/div/table/tbody/tr/td[3]/button/i').click()
#click on the popup
driver.find_element(By.XPATH,'/html/body/div[1]/div/section/div[3]/div[7]/div/div/div[2]/form').click()
time.sleep(4)
#click on to date
driver.find_element(By.XPATH,"/html/body/div[1]/div/section/div[3]/div[7]/div/div/div[2]/form/div/div[1]/input").click()
#Click on calender
driver.find_element(By.XPATH,"/html/body/div[5]/div/div/span[1]").click()
#click on back icon
driver.find_element(By.XPATH,"/html/body/div[5]/div/a[1]/span").click()
time.sleep(3)
#selecr the date
driver.find_element(By.XPATH,"/html/body/div[5]/table/tbody/tr[1]/td[1]/a").click()
time.sleep(4)
#click on Download Report button
driver.find_element(By.XPATH,"/html/body/div[1]/div/section/div[3]/div[7]/div/div/div[3]/button[2]").click()
print("Report Downloaded")
time.sleep(3)
#click on close button
driver.find_element(By.XPATH,"/html/body/div[1]/div/section/div[3]/div[7]/div/div/div[3]/button[1]").click()
time.sleep(4)
search_box2.clear()
print("Filter field is cleared")
#click on the logout button
driver.find_element(By.XPATH,"//a[normalize-space()='Sign out']").click()
print("the bm dashboard is successfully logout")

