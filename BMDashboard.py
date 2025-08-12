from datetime import time
from selenium.webdriver.support.ui import Select
import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Chrome()
driver.get("https://uat-bm.lightmicrofinance.com/index.php")
driver.maximize_window()
driver.implicitly_wait(3000)
#Login with valid credentials
driver.find_element(By.ID,"inputUsername").click()
driver.find_element(By.NAME,"inputUsername").send_keys("BMT1008")
driver.find_element(By.ID,"inputPassword").click()
driver.find_element(By.NAME,"inputPassword").send_keys("Light@123")
driver.find_element(By.XPATH,"//button[@type='submit']").click()
driver.implicitly_wait(4000)

#Expand Verification Entry section
driver.find_element(By.XPATH,"//li[1]//a[1]//i[2]").click()
#click on CLient Verification
driver.find_element(By.XPATH,"//a[normalize-space()='Client Verification']").click()




#click on select staff dropdown
driver.find_element(By.XPATH,"//span[@class='select2-selection__placeholder']").click()
#click on search field
driver.find_element(By.XPATH,"//input[@role='textbox']").click()
#driver.find_element(By.XPATH,"//input[@role='textbox']").send_keys("fet1003, fet1003")
search_input = driver.find_element(By.ID, "select2-staffId-results")

# Enter the search term to trigger auto-suggestions
search_input.send_keys("fet1003")

# Wait for the auto-suggest dropdown to appear (you may use a specific class or other locators)
wait = WebDriverWait(driver, 10)
results_list = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, "select2-staffId-results")))

# Extract the list of suggestions from the dropdown
results = results_list.find_elements(By.CSS_SELECTOR, "select2-staffId-result-jvpr-3866")

# Print the suggestions
for result in results:
    print(result.text)

# Select a suggestion (for demonstration, let's select the first one)
results[0].click()

# Wait for a while to see the selected option (you can remove this if not necessary)
import time
time.sleep(5)

driver.implicitly_wait(1000)

#dropdown.select_by_value('option1_value')
#time.sleep(5)



#logout
driver.find_element(By.XPATH,"//a[normalize-space()='Sign out']").click()
driver.refresh()
driver.quit()


print("print data after all scenarios get passed")



