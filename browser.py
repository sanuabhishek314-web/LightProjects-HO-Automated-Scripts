from selenium import webdriver
from selenium.webdriver.edge.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

# Path to the Edge Driver executable
edge_driver_path = "D:\Edge/msedgedriver.exe"
# Create a service object
service = Service(edge_driver_path)
# Create a new Edge session
driver = webdriver.Edge(service=service)
time.sleep(5)

driver.get("https://www.google.com")
driver.maximize_window()


print("Edge Executed Successfully")
driver.quit()
time.sleep(10)

#New Chrome Browser executed
driver = webdriver.Chrome()
driver.get("https://www.speedtest.net/")
driver.maximize_window()
driver.implicitly_wait(4)
driver.close()

print("chrome executed successfully")




