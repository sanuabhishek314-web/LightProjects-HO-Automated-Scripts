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
driver.find_element(By.NAME,"inputUsername").send_keys("BMT1007")
driver.find_element(By.ID,"inputPassword").click()
driver.find_element(By.NAME,"inputPassword").send_keys("Light@123")
driver.find_element(By.XPATH,"//button[@type='submit']").click()
time.sleep(11)

#select the Collection Section
driver.find_element(By.XPATH,"/html/body/div[1]/aside/section/ul/li[2]/ul/li[3]/a/span").click()
time.sleep(3)
#select the Digital Receipt Module
driver.find_element(By.XPATH,"/html/body/div[1]/aside/section/ul/li[2]/ul/li[3]/ul/li[1]/a").click()
time.sleep(3)
print("Digital Receipt Module is selected")
#click on the Digital Verification section
driver.find_element(By.XPATH,"/html/body/div[1]/div[2]/div/form/table/tbody/tr/td[1]").click()
time.sleep(3)

#select the staff from the dropdown
wait=WebDriverWait(driver,20)
staff_dropdown = wait.until(EC.element_to_be_clickable((
    By.XPATH,
    "//label[normalize-space()='Select Staff']/following::span[contains(@class,'select2-selection')][1] | //td[contains(normalize-space(),'Select Staff')]//span[contains(@class,'select2-selection')][1]"
)))
staff_dropdown.click()

staff_selected_ok = False
for _ in range(3):
    staff_dropdown.click()

    staff_search = None
    staff_search_locators = [
        "//span[contains(@class,'select2-container--open')]//input[@type='search']",
        "//div[contains(@class,'open')]//input[@type='search']",
        "//input[@aria-label='Search' and not(contains(@style,'display: none'))]",
    ]

    for locator in staff_search_locators:
        elems = driver.find_elements(By.XPATH, locator)
        visible_elems = [e for e in elems if e.is_displayed()]
        if visible_elems:
            staff_search = visible_elems[0]
            break

    if staff_search is not None:
        staff_search.click()
        staff_search.send_keys(Keys.CONTROL, "a")
        staff_search.send_keys(Keys.DELETE)
        staff_search.send_keys("fet1005")
    else:
        ActionChains(driver).move_to_element(staff_dropdown).click().send_keys("fet1005").perform()

    option_clicked = False
    option_candidates = driver.find_elements(
        By.XPATH,
        "//span[contains(@class,'select2-container--open')]//*[self::li or self::div][contains(@class,'results__option') or @role='option'][not(contains(translate(normalize-space(.),'ABCDEFGHIJKLMNOPQRSTUVWXYZ','abcdefghijklmnopqrstuvwxyz'),'no results')) and contains(translate(normalize-space(.),'ABCDEFGHIJKLMNOPQRSTUVWXYZ','abcdefghijklmnopqrstuvwxyz'),'fet1005')]",
    )

    for option in option_candidates:
        if not option.is_displayed():
            continue
        try:
            ActionChains(driver).move_to_element(option).click().perform()
            option_clicked = True
            break
        except Exception:
            try:
                driver.execute_script("arguments[0].click();", option)
                option_clicked = True
                break
            except Exception:
                continue

    if not option_clicked and staff_search is not None:
        try:
            staff_search.send_keys(Keys.ARROW_DOWN)
            staff_search.send_keys(Keys.ENTER)
        except Exception:
            pass

    driver.find_element(By.TAG_NAME, "body").click()
    time.sleep(1)

    selected_value_elements = driver.find_elements(
        By.XPATH,
        "//label[normalize-space()='Select Staff']/following::span[contains(@class,'select2-selection__rendered')][1] | //td[contains(normalize-space(),'Select Staff')]//span[contains(@class,'select2-selection__rendered')][1] | //label[normalize-space()='Select Staff']/following::input[1] | //td[contains(normalize-space(),'Select Staff')]/following::button[1]",
    )
    selected_values = []
    for elem in selected_value_elements:
        txt = (elem.text or "").strip()
        val = (elem.get_attribute("value") or "").strip()
        title = (elem.get_attribute("title") or "").strip()
        selected_values.extend([txt, val, title])

    if any("fet1005" in s.lower() for s in selected_values if s):
        staff_selected_ok = True
        break

if not staff_selected_ok:
    raise Exception("Staff not selected correctly. Current value: Select Staff")

print("Staff is being selected")
time.sleep(5)

#select the Center from the dropdown
click_center=wait.until(EC.element_to_be_clickable((
    By.XPATH,
    "//label[normalize-space()='Select Center']/following::span[contains(@class,'select2-selection')][1] | //td[contains(normalize-space(),'Select Center')]//span[contains(@class,'select2-selection')][1]"
)))
center_selected_ok = False
for _ in range(3):
    click_center.click()

    search_center = None
    center_search_locators = [
        "//span[contains(@class,'select2-container--open')]//input[@type='search']",
        "//div[contains(@class,'open')]//input[@type='search']",
        "//input[@aria-label='Search' and not(contains(@style,'display: none'))]",
    ]
    for locator in center_search_locators:
        elems = driver.find_elements(By.XPATH, locator)
        visible_elems = [e for e in elems if e.is_displayed()]
        if visible_elems:
            search_center = visible_elems[0]
            break

    if search_center is not None:
        search_center.click()
        search_center.send_keys(Keys.CONTROL, "a")
        search_center.send_keys(Keys.DELETE)
        search_center.send_keys("chas")
    else:
        ActionChains(driver).move_to_element(click_center).click().send_keys("chas").perform()

    center_clicked = False
    center_candidates = driver.find_elements(
        By.XPATH,
        "//span[contains(@class,'select2-container--open')]//*[self::li or self::div][contains(@class,'results__option') or @role='option'][not(contains(translate(normalize-space(.),'ABCDEFGHIJKLMNOPQRSTUVWXYZ','abcdefghijklmnopqrstuvwxyz'),'no results')) and contains(translate(normalize-space(.),'ABCDEFGHIJKLMNOPQRSTUVWXYZ','abcdefghijklmnopqrstuvwxyz'),'chas')]",
    )

    for option in center_candidates:
        if not option.is_displayed():
            continue
        try:
            ActionChains(driver).move_to_element(option).click().perform()
            center_clicked = True
            break
        except Exception:
            try:
                driver.execute_script("arguments[0].click();", option)
                center_clicked = True
                break
            except Exception:
                continue

    if not center_clicked and search_center is not None:
        try:
            search_center.send_keys(Keys.ARROW_DOWN)
            search_center.send_keys(Keys.ENTER)
        except Exception:
            pass

    driver.find_element(By.TAG_NAME, "body").click()
    time.sleep(1)

    center_selected = wait.until(EC.visibility_of_element_located((
        By.XPATH,
        "//label[normalize-space()='Select Center']/following::span[contains(@class,'select2-selection__rendered')][1] | //td[contains(normalize-space(),'Select Center')]//span[contains(@class,'select2-selection__rendered')][1]"
    )))
    center_text = center_selected.text.strip().lower()
    if center_text and center_text != "select center" and "chas" in center_text:
        center_selected_ok = True
        break

if not center_selected_ok:
    raise Exception("Center not selected correctly. Current value: Select Center")

print("Center is being selected")
time.sleep(3)

#click on the Get Collection button
wait.until(EC.element_to_be_clickable((By.ID,"btnGetData"))).click()
time.sleep(5)

#select client Nishisha Jain checkbox
nishisha_row = wait.until(EC.presence_of_element_located((
    By.XPATH,
    "//table//tr[td[contains(translate(normalize-space(.),'ABCDEFGHIJKLMNOPQRSTUVWXYZ','abcdefghijklmnopqrstuvwxyz'),'nishisha jain')]]"
)))
nishisha_checkbox = nishisha_row.find_element(By.XPATH, ".//td[1]//input[@type='checkbox']")
if not nishisha_checkbox.is_selected():
    driver.execute_script("arguments[0].click();", nishisha_checkbox)
time.sleep(1)

#click on the Save all / Approve button section
save_all_btn = wait.until(EC.element_to_be_clickable((
    By.XPATH,
    "//input[@value='Save All'] | //button[normalize-space()='Save All']"
)))
save_all_btn.click()
print("Data is being saved")
time.sleep(5)

#check the same Nishisha Jain checkbox again
nishisha_row = wait.until(EC.presence_of_element_located((
    By.XPATH,
    "//table//tr[td[contains(translate(normalize-space(.),'ABCDEFGHIJKLMNOPQRSTUVWXYZ','abcdefghijklmnopqrstuvwxyz'),'nishisha jain')]]"
)))
nishisha_checkbox = nishisha_row.find_element(By.XPATH, ".//td[1]//input[@type='checkbox']")
if not nishisha_checkbox.is_selected():
    driver.execute_script("arguments[0].click();", nishisha_checkbox)
time.sleep(1)

#click on the Approve All button
approve_all_btn = wait.until(EC.element_to_be_clickable((
    By.XPATH,
    "//input[@value='Approve All'] | //button[normalize-space()='Approve All']"
)))
approve_all_btn.click()
print("Data is being Approved success")
time.sleep(3)
#alert accept
#WebDriverWait(driver,10).until(EC.alert_is_present())
#alert=driver.switch_to.alert
#print(alert.text)
#alert.accept()
#time.sleep(2)

#click on the back button in the page
driver.find_element(By.XPATH,"//a[@title='Back to dashboard']").click()
time.sleep(3)
#alert accept
#WebDriverWait(driver,10).until(EC.alert_is_present())
#alert=driver.switch_to.alert
#print(alert.text)
#alert.accept()
#time.sleep(6)

#click on the logout button
driver.find_element(By.XPATH,"//a[normalize-space()='Sign out']").click()
print("the bm dashboard is successfully logout")



