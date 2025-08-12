from appium import webdriver
from appium.webdriver.common.appiumby import AppiumBy
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Desired Capabilities
desired_caps = {
    "platformName": "Android",
    "platformVersion": "14",  # change as per your emulator/device
    "deviceName": "Redmi Note 12 5G",
    "appPackage": "com.dhwaniris.lmfi_field_uat",  # or your app's package
    "appActivity": "Add Client-Online",  # or main activity of your app
    "automationName": "UiAutomation",
    "noReset": True
}

# Appium server URL
driver = webdriver.Remote("http://localhost:4723/wd/hub", desired_caps)

wait = WebDriverWait(driver, 20)
element = wait.until(EC.presence_of_element_located((AppiumBy.ID, "com.example.app:id/button_id")))
element.click()

finally:
    driver.quit()


def webdriver():
    return None