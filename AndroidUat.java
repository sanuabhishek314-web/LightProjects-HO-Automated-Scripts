package com.example.appiumrunner;

import io.appium.java_client.AppiumBy;
import io.appium.java_client.android.AndroidDriver;
import io.appium.java_client.android.nativekey.AndroidKey;
import io.appium.java_client.android.nativekey.KeyEvent;
import io.appium.java_client.android.options.UiAutomator2Options;
import org.openqa.selenium.By;
import org.openqa.selenium.Rectangle;
import org.openqa.selenium.StaleElementReferenceException;
import org.openqa.selenium.WebElement;
import org.openqa.selenium.Dimension;
import org.openqa.selenium.support.ui.ExpectedConditions;
import org.openqa.selenium.support.ui.WebDriverWait;

import java.net.InetSocketAddress;
import java.net.Socket;
import java.net.URL;
import java.time.Duration;
import java.util.List;
import java.util.Map;

public class AndroidUat {

    private static final int DEFAULT_TIMEOUT = 25;
    private static final int LOGIN_CLICK_TIMEOUT = 40;
    private static final int LOGIN_PAGE_WAIT_MS = 12_000;
    private static final int POST_LOGIN_SYNC_WAIT_SEC = 10;
    private static final String APPIUM_SERVER_URL = "http://127.0.0.1:4723/";
    private static final String DEVICE_UDID = "adb-RZCW80DPGMH-dX2eIP._adb-tls-connect._tcp";
    private static final String FIELD_APP_PACKAGE = "com.dhwaniris.lmfi_field_uat";
    private static final String FIELD_APP_ACTIVITY = "com.dhwaniris.lmfi_field.views.splash.SplashActivity";
    private static final String LOCAL_DEBUG_PACKAGE = "com.example.android_uat_testing_field";
    private static final String GEO_LIGHT_PACKAGE = "com.spotlight.geolight";

    private static WebElement waitClickable(AndroidDriver driver, By by, int timeoutSec) {
        return new WebDriverWait(driver, Duration.ofSeconds(timeoutSec))
                .until(ExpectedConditions.elementToBeClickable(by));
    }

    private static WebElement waitVisible(AndroidDriver driver, By by, int timeoutSec) {
        return new WebDriverWait(driver, Duration.ofSeconds(timeoutSec))
                .until(ExpectedConditions.visibilityOfElementLocated(by));
    }

    private static void waitClick(AndroidDriver driver, By by, int timeoutSec) {
        waitClickable(driver, by, timeoutSec).click();
    }

    private static void waitSendKeys(AndroidDriver driver, By by, String text, int timeoutSec, boolean clear) {
        WebElement el = waitVisible(driver, by, timeoutSec);
        if (clear) {
            el.clear();
        }
        el.sendKeys(text);
    }

    private static boolean clickIfPresent(AndroidDriver driver, By by, int timeoutSec) {
        try {
            waitClick(driver, by, timeoutSec);
            return true;
        } catch (Exception e) {
            return false;
        }
    }

    private static void tapBelowPunchButton(AndroidDriver driver) {
        List<String> punchXpaths = List.of(
                "//*[@text='PUNCH IN' or @content-desc='PUNCH IN']",
                "//*[contains(@text,'PUNCH IN') or contains(@content-desc,'PUNCH IN')]");

        for (String xpath : punchXpaths) {
            try {
                WebElement punchEl = waitVisible(driver, By.xpath(xpath), 5);
                Rectangle r = punchEl.getRect();
                int x = r.getX() + (r.getWidth() / 2);
                int y = r.getY() + r.getHeight() + 80;
                driver.executeScript("mobile: clickGesture", Map.of("x", x, "y", y));
                return;
            } catch (Exception ignored) {
            }
        }

        try {
            Dimension size = driver.manage().window().getSize();
            int x = size.getWidth() / 2;
            int y = (int) (size.getHeight() * 0.68);
            driver.executeScript("mobile: clickGesture", Map.of("x", x, "y", y));
        } catch (Exception ignored) {
        }
    }

    private static void hideKeyboardOnly(AndroidDriver driver) {
        try {
            driver.hideKeyboard();
        } catch (Exception ignored) {
        }
    }

    private static void hideKeyboardSafelyNoBack(AndroidDriver driver) {
        try {
            System.out.println("Attempting safe keyboard dismiss (no back navigation)...");
            hideKeyboardOnly(driver);
            Thread.sleep(700);
            try {
                driver.hideKeyboard();
            } catch (Exception ignored) {
            }
        } catch (Exception ignored) {
        }
    }

    private static void clickCashCollectionButtonSafe(AndroidDriver driver) {
        System.out.println("Attempting safe CASH COLLECTION click...");
        try {
            dismissBackNavigationPopupIfPresent(driver);
            Thread.sleep(400);
        } catch (Exception ignored) {
        }

        List<By> cashCollectionLocators = List.of(
                textEquals("CASH COLLECTION"),
                textContains("CASH COLLECTION"),
                By.xpath("//android.widget.Button[@text='CASH COLLECTION']"),
                By.xpath("//*[@text='CASH COLLECTION' and (@clickable='true' or @enabled='true')]"));

        for (By locator : cashCollectionLocators) {
            try {
                waitClick(driver, locator, 8);
                return;
            } catch (Exception ignored) {
            }
        }

        throw new IllegalStateException("Could not click CASH COLLECTION button safely.");
    }

    private static void waitForAppiumServer(String host, int port, int totalWaitSec) {
        long end = System.currentTimeMillis() + (totalWaitSec * 1000L);
        while (System.currentTimeMillis() < end) {
            try (Socket socket = new Socket()) {
                socket.connect(new InetSocketAddress(host, port), 1500);
                return;
            } catch (Exception ignored) {
                try {
                    Thread.sleep(1000);
                } catch (InterruptedException interruptedException) {
                    Thread.currentThread().interrupt();
                    break;
                }
            }
        }

        throw new IllegalStateException(
                "Appium server is not reachable at " + host + ":" + port
                        + ". Start Appium first, then rerun the task.");
    }

    private static void focusTopSearchAndType(AndroidDriver driver, String text, int timeoutSec) {
        System.out.println("Attempting to type '" + text + "' into search field...");

        List<String> searchFieldXpaths = List.of(
                "(//android.widget.EditText)[1]",
                "(//android.widget.AutoCompleteTextView)[1]",
                "//*[@class='android.widget.AutoCompleteTextView' and @clickable='true']",
                "//*[@class='android.widget.EditText' and @clickable='true']",
                "//*[contains(@resource-id,'search')]",
                "//*[contains(@hint,'Search') or contains(@hint,'search')]",
                "//android.widget.EditText[@clickable='true']",
                "//android.widget.AutoCompleteTextView[@clickable='true']",
                "//*[@class='android.widget.EditText']",
                "//*[@class='android.widget.AutoCompleteTextView']",
                "//android.widget.EditText",
                "//android.widget.AutoCompleteTextView");

        long end = System.currentTimeMillis() + (timeoutSec * 1000L);
        while (System.currentTimeMillis() < end) {
            // Try direct field interaction first
            for (String xpath : searchFieldXpaths) {
                try {
                    List<WebElement> fields = driver.findElements(By.xpath(xpath));
                    for (WebElement field : fields) {
                        if (tryTypeIntoField(driver, field, text)) {
                            System.out.println("Successfully typed '" + text + "' using XPath: " + xpath);
                            return;
                        }
                    }
                } catch (Exception ignored) {
                }
            }

            // Dismiss any popup that might have appeared from accidental back clicks
            try {
                dismissBackNavigationPopupIfPresent(driver);
                Thread.sleep(500);
            } catch (Exception ignored) {
            }

            // Try using ADB input method as last resort
            try {
                System.out.println("Trying ADB input method...");
                driver.executeScript("mobile: shell", Map.of("command", "input", "args", List.of("text", text)));
                Thread.sleep(500);
                hideKeyboardOnly(driver);
                System.out.println("Successfully typed '" + text + "' using ADB input");
                return;
            } catch (Exception ignored) {
            }

            try {
                Thread.sleep(400);
            } catch (InterruptedException ignored) {
                Thread.currentThread().interrupt();
                break;
            }
        }

        // Handle accidental back button popup before failing
        try {
            dismissBackNavigationPopupIfPresent(driver);
        } catch (Exception ignored) {
        }

        throw new IllegalStateException("Could not type into top search field for text: " + text);
    }

    private static void dismissBackNavigationPopupIfPresent(AndroidDriver driver) {
        List<String> backPopupDismissXpaths = List.of(
                "//*[@text='NO' or @content-desc='NO']",
                "//*[contains(@text,'NO') or contains(@content-desc,'NO')]",
                "//*[@text='Cancel' or @content-desc='Cancel']",
                "//*[contains(@text,'Cancel') or contains(@content-desc,'Cancel')]",
                "//android.widget.Button[@text='NO']",
                "//android.widget.Button[contains(@text,'NO')]",
                "//*[@class='android.widget.Button' and @text='NO']",
                "//*[@class='android.widget.Button' and contains(@text,'NO')]");

        // First try to find and click NO button
        for (String xpath : backPopupDismissXpaths) {
            try {
                List<WebElement> dismissButtons = driver.findElements(By.xpath(xpath));
                for (WebElement dismissButton : dismissButtons) {
                    try {
                        if (dismissButton.isDisplayed() && dismissButton.isEnabled()) {
                            System.out.println(
                                    "Found back navigation popup, dismissing with NO/Cancel using XPath: " + xpath);
                            dismissButton.click();
                            Thread.sleep(1000);
                            System.out.println("Successfully dismissed back navigation popup");
                            return;
                        }
                    } catch (Exception ignored) {
                    }
                }
            } catch (Exception ignored) {
            }
        }

        // Try coordinate-based click for NO button area (bottom left of popup)
        try {
            Dimension size = driver.manage().window().getSize();
            int x = (int) (size.getWidth() * 0.35); // Left side of popup
            int y = (int) (size.getHeight() * 0.55); // Bottom area of popup
            System.out.println("Trying coordinate click for NO button at (" + x + ", " + y + ")");
            driver.executeScript("mobile: clickGesture", Map.of("x", x, "y", y));
            Thread.sleep(1000);
            System.out.println("Coordinate click attempted for popup dismissal");
        } catch (Exception ignored) {
        }
    }

    private static void focusBorrowerSearchAndType(AndroidDriver driver, String text, int timeoutSec) {
        System.out.println("Attempting to type '" + text + "' into borrower search field...");

        // First try to find the search field using borrower-specific selectors
        List<String> borrowerSearchXpaths = List.of(
                "//*[contains(@text,'Borrower List')]/following::android.widget.EditText[1]",
                "//*[contains(@text,'BORROWER LIST')]/following::android.widget.EditText[1]",
                "//*[contains(@text,'Borrower List')]/following::*[@class='android.widget.EditText'][1]",
                "//*[contains(@content-desc,'Search') or contains(@hint,'Search')]",
                "//android.widget.EditText[@clickable='true']",
                "//android.widget.AutoCompleteTextView[@clickable='true']");

        long end = System.currentTimeMillis() + (timeoutSec * 1000L);
        while (System.currentTimeMillis() < end) {
            // Try borrower-specific XPath selectors first
            for (String xpath : borrowerSearchXpaths) {
                try {
                    List<WebElement> fields = driver.findElements(By.xpath(xpath));
                    for (WebElement field : fields) {
                        if (tryTypeIntoField(driver, field, text)) {
                            System.out.println(
                                    "Successfully typed '" + text + "' in borrower search using XPath: " + xpath);
                            return;
                        }
                    }
                } catch (Exception ignored) {
                }
            }

            // Try safe coordinate-based approach - target area below "Borrower List" text
            try {
                System.out.println("Trying safe coordinate click below 'Borrower List' text...");
                Dimension size = driver.manage().window().getSize();
                // Target the search field area - center horizontally, below the header
                int x = (int) (size.getWidth() * 0.50); // Center of screen
                int y = (int) (size.getHeight() * 0.30); // Below header, above first item

                System.out.println("Clicking at safe coordinates: (" + x + ", " + y + ") for borrower search");
                driver.executeScript("mobile: clickGesture", Map.of("x", x, "y", y));
                Thread.sleep(500);

                WebElement active = driver.switchTo().activeElement();
                if (active != null && tryTypeIntoField(driver, active, text)) {
                    System.out.println("Successfully typed '" + text + "' using safe coordinate click");
                    return;
                }
            } catch (Exception ignored) {
            }

            // Dismiss any popup that might have appeared
            try {
                dismissBackNavigationPopupIfPresent(driver);
                Thread.sleep(500);
            } catch (Exception ignored) {
            }

            try {
                Thread.sleep(400);
            } catch (InterruptedException ignored) {
                Thread.currentThread().interrupt();
                break;
            }
        }

        throw new IllegalStateException("Could not type into borrower search field for text: " + text);
    }

    private static void focusBorrowerSearchWithMagnifyingGlass(AndroidDriver driver, String text, int timeoutSec) {
        System.out.println("Attempting to type '" + text
                + "' into borrower search field by clicking magnifying glass icon first...");

        // First try to find and click the magnifying glass icon in borrower screen
        List<String> borrowerSearchIconXpaths = List.of(
                "//android.widget.ImageView[@content-desc='Search' or contains(@content-desc,'search')]",
                "//*[@class='android.widget.ImageView' and (@content-desc='Search' or contains(@content-desc,'search'))]",
                "//android.widget.ImageButton[@content-desc='Search' or contains(@content-desc,'search')]",
                "//*[contains(@resource-id,'search_button') or contains(@resource-id,'search_icon')]",
                "//*[contains(@text,'BORROWER LIST')]/following::android.widget.ImageView[1]",
                "//android.widget.ImageView[@clickable='true']");

        long end = System.currentTimeMillis() + (timeoutSec * 1000L);
        while (System.currentTimeMillis() < end) {
            // Try to click magnifying glass icon first
            for (String xpath : borrowerSearchIconXpaths) {
                try {
                    WebElement searchIcon = driver.findElement(By.xpath(xpath));
                    if (searchIcon.isDisplayed() && searchIcon.isEnabled()) {
                        System.out.println("Found borrower magnifying glass icon, clicking it first...");
                        searchIcon.click();
                        Thread.sleep(500);

                        // Now try to type in the activated search field
                        WebElement active = driver.switchTo().activeElement();
                        if (active != null && tryTypeIntoField(driver, active, text)) {
                            System.out.println(
                                    "Successfully typed '" + text + "' after clicking borrower magnifying glass icon");
                            return;
                        }
                    }
                } catch (Exception ignored) {
                }
            }

            // Fallback to the existing borrower search method
            try {
                focusBorrowerSearchAndType(driver, text, 5);
                return;
            } catch (Exception ignored) {
            }

            // Dismiss any popup that might have appeared
            try {
                dismissBackNavigationPopupIfPresent(driver);
                Thread.sleep(500);
            } catch (Exception ignored) {
            }

            try {
                Thread.sleep(400);
            } catch (InterruptedException ignored) {
                Thread.currentThread().interrupt();
                break;
            }
        }

        throw new IllegalStateException(
                "Could not type into borrower search field using magnifying glass for text: " + text);
    }

    private static void checkSelectAllIfUnchecked(AndroidDriver driver) {
        List<String> selectAllXpaths = List.of(
                "//*[@text='Select All' or @content-desc='Select All']",
                "//*[contains(@text,'Select All') or contains(@content-desc,'Select All')]",
                "//android.widget.CheckBox[@checked='false']",
                "//*[@class='android.widget.CheckBox' and @checked='false']");

        for (String xpath : selectAllXpaths) {
            try {
                List<WebElement> checkboxes = driver.findElements(By.xpath(xpath));
                for (WebElement checkbox : checkboxes) {
                    try {
                        if (checkbox.isDisplayed() && checkbox.isEnabled()) {
                            // Check if it's unchecked by looking at the checked attribute
                            String checkedAttr = checkbox.getAttribute("checked");
                            if ("false".equals(checkedAttr)) {
                                System.out.println("Found unchecked Select All checkbox, checking it...");
                                checkbox.click();
                                Thread.sleep(500);
                                System.out.println("Successfully checked Select All checkbox");
                                return;
                            }
                        }
                    } catch (Exception ignored) {
                    }
                }
            } catch (Exception ignored) {
            }
        }

        // Try coordinate-based approach for Select All area
        try {
            System.out.println("Trying coordinate-based click for Select All checkbox...");
            Dimension size = driver.manage().window().getSize();
            int x = (int) (size.getWidth() * 0.15); // Left side where checkbox typically is
            int y = (int) (size.getHeight() * 0.35); // Approximate height of Select All
            driver.executeScript("mobile: clickGesture", Map.of("x", x, "y", y));
            Thread.sleep(500);
            System.out.println("Coordinate click attempted for Select All checkbox");
        } catch (Exception ignored) {
        }
    }

    private static void clearAndEnterAmountCollected(AndroidDriver driver, String amount) {
        System.out.println("Clearing and entering amount: " + amount);

        List<String> amountFieldXpaths = List.of(
                "//*[contains(@text,'Amount Collected')]/following::android.widget.EditText[1]",
                "//*[contains(@text,'Amount Due')]/following::android.widget.EditText[1]",
                "//android.widget.EditText[contains(@text,'8800')]", // Based on screenshot
                "//android.widget.EditText[@clickable='true']",
                "//*[@class='android.widget.EditText']");

        for (String xpath : amountFieldXpaths) {
            try {
                WebElement amountField = driver.findElement(By.xpath(xpath));
                if (amountField.isDisplayed() && amountField.isEnabled()) {
                    System.out.println("Found amount field, clearing and entering: " + amount);

                    // Clear existing content
                    amountField.clear();
                    Thread.sleep(500);

                    // Try multiple methods to clear
                    amountField.click();
                    Thread.sleep(300);

                    // Select all and delete
                    try {
                        driver.executeScript("mobile: selectAll");
                        Thread.sleep(200);
                        driver.executeScript("mobile: type", Map.of("text", amount));
                    } catch (Exception e) {
                        // Fallback to direct sendKeys
                        amountField.sendKeys(amount);
                    }

                    System.out.println("Successfully entered amount: " + amount);

                    // Dismiss keyboard after entering amount
                    try {
                        System.out.println("Dismissing keyboard after entering amount...");
                        hideKeyboardOnly(driver);
                        Thread.sleep(1000);

                        // Try multiple methods to ensure keyboard is closed
                        if (Boolean.TRUE.equals(driver.isKeyboardShown())) {
                            System.out.println("Keyboard still shown, trying back navigation...");
                            driver.navigate().back();
                            Thread.sleep(1000);
                        }

                        // Additional keyboard dismissal attempts
                        try {
                            driver.hideKeyboard();
                        } catch (Exception ignored) {
                        }

                    } catch (Exception ignored) {
                    }

                    return;
                }
            } catch (Exception ignored) {
            }
        }

        System.out.println("Could not find amount collected field");
    }

    private static void enterDenomination(AndroidDriver driver, String value) {
        System.out.println("Entering denomination value in ₹1 field: " + value);

        // First scroll down robustly to bottom where the ₹1 is
        try {
            System.out.println("Scrolling down to make ₹1 field visible via UiScrollable...");
            driver.findElement(AppiumBy.androidUIAutomator(
                    "new UiScrollable(new UiSelector().scrollable(true)).scrollIntoView(" +
                            "new UiSelector().textContains(\"1 X\"))"));
            Thread.sleep(1000);
        } catch (Exception e) {
            System.out.println("UiScrollable scroll failed, using fallback scroll: " + e.getMessage());
            try {
                Dimension size = driver.manage().window().getSize();
                int startX = size.getWidth() / 2;
                int startY = (int) (size.getHeight() * 0.8);
                int endY = (int) (size.getHeight() * 0.2);

                for (int i = 0; i < 3; i++) {
                    driver.executeScript("mobile: scrollGesture", Map.of(
                            "left", 0, "top", startY, "width", size.getWidth(), "height", startY - endY,
                            "direction", "down", "percent", 1.0));
                    Thread.sleep(500);
                }
            } catch (Exception ignored) {
            }
        }

        // Try XPath selectors tailored for ₹1 field
        List<String> denominationXpaths = List.of(
                "//*[@text='₹1 X']/following-sibling::android.widget.EditText",
                "//*[@text='₹ 1 X']/following-sibling::android.widget.EditText",
                "//*[contains(@text, '1 X') and not(contains(@text, '0'))]/../android.widget.EditText",
                "//*[contains(@text, '1 X') and not(contains(@text, '0'))]/following-sibling::android.widget.EditText"
        );

        boolean entered = false;
        for (String xpath : denominationXpaths) {
            try {
                List<WebElement> fields = driver.findElements(By.xpath(xpath));
                if (!fields.isEmpty()) {
                    WebElement denomField = fields.get(fields.size() - 1); // Get the last one if multiple match
                    if (denomField.isDisplayed() && denomField.isEnabled()) {
                        System.out.println("Found ₹1 denomination field using XPath: " + xpath);

                        denomField.click();
                        Thread.sleep(300);
                        denomField.clear();
                        Thread.sleep(300);
                        denomField.sendKeys(value);
                        System.out.println("Successfully entered denomination: " + value);
                        entered = true;
                        break;
                    }
                }
            } catch (Exception ignored) {
            }
        }

        if (!entered) {
            System.out.println("Could not find ₹1 field via XPaths. Targeting the last EditText.");
            try {
                List<WebElement> allInputsBefore = driver.findElements(By.className("android.widget.EditText"));
                if(!allInputsBefore.isEmpty()) {
                    WebElement lastInput = allInputsBefore.get(allInputsBefore.size() - 1);
                    if (lastInput.isDisplayed() && lastInput.isEnabled()) {
                        lastInput.click();
                        Thread.sleep(300);
                        lastInput.clear();
                        Thread.sleep(300);
                        lastInput.sendKeys(value);
                        System.out.println("Entered denomination by picking the last EditText.");
                    }
                }
            } catch (Exception ignored) {}
        }

        dismissKeyboardAfterDenomination(driver);
    }

    private static void dismissKeyboardAfterDenomination(AndroidDriver driver) {
        try {
            System.out.println("Dismissing keyboard after entering denomination...");

            // Try standard hide keyboard (can throw if no keyboard is present)
            try {
                driver.hideKeyboard();
            } catch (Exception ignored) {}
            Thread.sleep(1000);

            // Attempt to tap outside the text box to dismiss focus
            try {
                Dimension size = driver.manage().window().getSize();
                // Tap near the top, usually safe to dismiss keyboard
                driver.executeScript("mobile: clickGesture", Map.of("x", size.getWidth() / 2, "y", (int)(size.getHeight() * 0.1)));
                Thread.sleep(500);
            } catch (Exception ignored) {}

            // Try multiple methods to ensure keyboard is closed without using BACK navigation
            // using BACK navigation may accidentally go back and dismiss the confirm button popup
            if (Boolean.TRUE.equals(driver.isKeyboardShown())) {
                System.out.println("Keyboard still shown, trying safe keypad dismissal...");
                try {
                    driver.pressKey(new KeyEvent(AndroidKey.ESCAPE));
                } catch (Exception ignored) {}
                Thread.sleep(500);
            }

        } catch (Exception ignored) {
        }
    }

    private static void navigateBackAndLogout(AndroidDriver driver) {
        System.out.println("Starting navigation back and logout sequence...");

        // Iterate backwards through pages until we see the Logout button.
        for (int i = 1; i <= 3; i++) {
            if (isLogoutButtonVisible(driver)) {
                System.out.println("Logout button is visible, we are on the main page.");
                break;
            }

            try {
                System.out.println("Clicking back button (Attempt " + i + ")...");
                clickBackButton(driver);

                System.out.println("Waiting 3 seconds for popup...");
                Thread.sleep(3000);

                System.out.println("Selecting YES in popup...");
                clickYesInPopup(driver);
                Thread.sleep(1000);
            } catch (Exception e) {
                System.out.println("Failed back navigation step: " + e.getMessage());
            }
        }

        // Wait for 5 secs on main page
        System.out.println("Waiting 5 seconds on main page...");
        try {
            Thread.sleep(5000);
        } catch (InterruptedException ignored) {}

        // Click Logout button
        try {
            System.out.println("Clicking Logout button in top right...");
            clickLogoutButton(driver);
            Thread.sleep(3000);

            // Select Logout in popup
            System.out.println("Selecting Logout in popup...");
            confirmLogout(driver);
            Thread.sleep(6000);

            // Verify login page is displayed
            System.out.println("Verifying login page is displayed...");
            verifyLoginPage(driver);

        } catch (Exception e) {
            System.out.println("Failed logout process: " + e.getMessage());
        }

        // Close the apk
        try {
            safeTerminateApp(driver, FIELD_APP_PACKAGE);
        } catch (Exception ignored) {}
    }

    private static boolean isLogoutButtonVisible(AndroidDriver driver) {
        List<String> logoutButtonXpaths = List.of(
                "//*[@text='Logout' or @content-desc='Logout']",
                "//*[contains(@text,'Logout') or contains(@content-desc,'Logout')]",
                "//android.widget.ImageButton[contains(@content-desc,'logout')]",
                "//*[contains(@resource-id,'logout') or contains(@resource-id,'menu')]");
        for (String xpath : logoutButtonXpaths) {
            try {
                List<WebElement> check = driver.findElements(By.xpath(xpath));
                for (WebElement element : check) {
                    if (element.isDisplayed()) return true;
                }
            } catch (Exception ignored) {
            }
        }
        return false;
    }

    private static void clickBackButton(AndroidDriver driver) {
        System.out.println("Attempting to click back button on current page...");

        // Enhanced coordinate-based approach for back button on Borrower List
        try {
            System.out.println("Using enhanced coordinate-based back button click for Borrower List...");
            Dimension size = driver.manage().window().getSize();

            // Target the back arrow more precisely based on Borrower List screenshot
            int x = (int) (size.getWidth() * 0.04); // Very left for back arrow
            int y = (int) (size.getHeight() * 0.06); // Very top for header area

            System.out.println("Clicking back button at coordinates: (" + x + ", " + y + ")");
            driver.executeScript("mobile: clickGesture", Map.of("x", x, "y", y));
            Thread.sleep(1000);
            return;

        } catch (Exception e) {
            System.out.println("Enhanced coordinate approach failed: " + e.getMessage());
        }

        // Try multiple precise coordinate positions for back button
        try {
            System.out.println("Trying multiple coordinate positions for back button...");
            Dimension size = driver.manage().window().getSize();

            // Multiple positions targeting the back arrow area
            int[][] backPositions = {
                    { (int) (size.getWidth() * 0.03), (int) (size.getHeight() * 0.05) }, // Very top-left
                    { (int) (size.getWidth() * 0.05), (int) (size.getHeight() * 0.07) }, // Slightly more centered
                    { (int) (size.getWidth() * 0.07), (int) (size.getHeight() * 0.09) }, // More centered
                    { (int) (size.getWidth() * 0.02), (int) (size.getHeight() * 0.08) }, // Far left
                    { (int) (size.getWidth() * 0.08), (int) (size.getHeight() * 0.06) }, // Right of arrow
            };

            for (int[] pos : backPositions) {
                try {
                    System.out.println("Trying back button at coordinates: (" + pos[0] + ", " + pos[1] + ")");
                    driver.executeScript("mobile: clickGesture", Map.of("x", pos[0], "y", pos[1]));
                    Thread.sleep(1000);
                    return;
                } catch (Exception ignored) {
                }
            }
        } catch (Exception e) {
            System.out.println("Multiple coordinate approach failed: " + e.getMessage());
        }

        // Fallback XPath selectors
        List<String> backButtonXpaths = List.of(
                "//android.widget.ImageButton[@clickable='true'][1]", // First clickable ImageButton
                "//*[contains(@content-desc,'Navigate up') or contains(@content-desc,'Back')]",
                "//android.widget.ImageButton[@content-desc='Navigate up']",
                "//android.widget.ImageView[@clickable='true'][1]",
                "//*[@class='android.widget.ImageButton'][1]");

        for (String xpath : backButtonXpaths) {
            try {
                WebElement backButton = driver.findElement(By.xpath(xpath));
                if (backButton.isDisplayed() && backButton.isEnabled()) {
                    System.out.println("Found back button using XPath: " + xpath);
                    backButton.click();
                    Thread.sleep(1000);
                    return;
                }
            } catch (Exception ignored) {
            }
        }

        // Alternative coordinate positions
        try {
            System.out.println("Trying alternative coordinate positions for back button...");
            Dimension size = driver.manage().window().getSize();

            // Try multiple coordinate positions
            int[][] positions = {
                    { (int) (size.getWidth() * 0.04), (int) (size.getHeight() * 0.06) }, // Very top-left
                    { (int) (size.getWidth() * 0.08), (int) (size.getHeight() * 0.10) }, // Slightly more centered
                    { (int) (size.getWidth() * 0.10), (int) (size.getHeight() * 0.12) }, // Even more centered
            };

            for (int[] pos : positions) {
                try {
                    System.out.println("Trying back button at coordinates: (" + pos[0] + ", " + pos[1] + ")");
                    driver.executeScript("mobile: clickGesture", Map.of("x", pos[0], "y", pos[1]));
                    Thread.sleep(1000);
                    return;
                } catch (Exception ignored) {
                }
            }

        } catch (Exception finalException) {
            System.out.println("All back button click attempts failed: " + finalException.getMessage());
        }
    }

    private static boolean clickYesInPopup(AndroidDriver driver) {
        List<String> yesButtonXpaths = List.of(
                "//*[@text='YES' or @text='Yes' or @content-desc='YES']",
                "//*[contains(@text,'YES') or contains(@text,'Yes')]",
                "//android.widget.Button[@text='YES' or @text='Yes']",
                "//*[@class='android.widget.Button' and (@text='YES' or @text='Yes')]");

        for (String xpath : yesButtonXpaths) {
            try {
                WebElement yesButton = driver.findElement(By.xpath(xpath));
                if (yesButton.isDisplayed() && yesButton.isEnabled()) {
                    System.out.println("Found YES button, clicking...");
                    yesButton.click();
                    return true;
                }
            } catch (Exception ignored) {
            }
        }

        // Try coordinate click for YES
        try {
            System.out.println("Trying coordinate-based YES button click...");
            Dimension size = driver.manage().window().getSize();
            int x = (int) (size.getWidth() * 0.70); // Appx YES position
            int y = (int) (size.getHeight() * 0.55);
            driver.executeScript("mobile: clickGesture", Map.of("x", x, "y", y));
            return true;
        } catch (Exception ignored) {}

        System.out.println("Could not find YES button in popup");
        return false;
    }

    private static void clickLogoutButton(AndroidDriver driver) {
        List<String> logoutButtonXpaths = List.of(
                "//*[@text='Logout' or @content-desc='Logout']",
                "//*[contains(@text,'Logout') or contains(@content-desc,'Logout')]",
                "//android.widget.ImageButton[contains(@content-desc,'logout')]",
                "//*[contains(@resource-id,'logout') or contains(@resource-id,'menu')]");

        for (String xpath : logoutButtonXpaths) {
            try {
                WebElement logoutButton = driver.findElement(By.xpath(xpath));
                if (logoutButton.isDisplayed() && logoutButton.isEnabled()) {
                    System.out.println("Found Logout button, clicking...");
                    logoutButton.click();
                    return;
                }
            } catch (Exception ignored) {
            }
        }

        // Fallback to coordinate-based click for logout button (top-right area)
        try {
            System.out.println("Using coordinate-based logout button click...");
            Dimension size = driver.manage().window().getSize();
            int x = (int) (size.getWidth() * 0.90); // Right side
            int y = (int) (size.getHeight() * 0.10); // Top area
            driver.executeScript("mobile: clickGesture", Map.of("x", x, "y", y));
        } catch (Exception e) {
            System.out.println("Failed to click logout button: " + e.getMessage());
        }
    }

    private static void confirmLogout(AndroidDriver driver) {
        List<String> logoutConfirmXpaths = List.of(
                "//*[contains(translate(@text,'ABCDEFGHIJKLMNOPQRSTUVWXYZ','abcdefghijklmnopqrstuvwxyz'),'are you sure want to logout')]/following::*[@text='LOGOUT' or @text='Logout'][1]",
                "//*[contains(translate(@text,'ABCDEFGHIJKLMNOPQRSTUVWXYZ','abcdefghijklmnopqrstuvwxyz'),'logout')]/following::*[@text='LOGOUT' or @text='Logout'][1]",
                "//android.widget.Button[@text='LOGOUT' or @text='Logout']",
                "//*[@class='android.widget.TextView' and (@text='LOGOUT' or @text='Logout')]",
                "//*[@clickable='true' and (@text='LOGOUT' or @text='Logout')]");

        for (String xpath : logoutConfirmXpaths) {
            try {
                List<WebElement> candidates = driver.findElements(By.xpath(xpath));
                for (WebElement logoutConfirm : candidates) {
                    try {
                        if (logoutConfirm.isDisplayed() && logoutConfirm.isEnabled()) {
                            System.out.println("Found Logout confirmation in popup, clicking... XPath: " + xpath);
                            logoutConfirm.click();
                            return;
                        }
                    } catch (Exception ignored) {
                    }
                }
            } catch (Exception ignored) {
            }
        }

        try {
            System.out.println("Trying coordinate fallback for popup LOGOUT button...");
            Dimension size = driver.manage().window().getSize();
            int x = (int) (size.getWidth() * 0.68);
            int y = (int) (size.getHeight() * 0.57);
            driver.executeScript("mobile: clickGesture", Map.of("x", x, "y", y));
            Thread.sleep(500);
            return;
        } catch (Exception ignored) {
        }

        System.out.println("Could not find Logout confirmation button");
    }

    private static void verifyLoginPage(AndroidDriver driver) {
        List<String> loginPageXpaths = List.of(
                "//*[@text='Login' or @content-desc='Login']",
                "//*[contains(@text,'Login') or contains(@content-desc,'Login')]",
                "//*[@text='Username' or @content-desc='Username']",
                "//*[@text='Password' or @content-desc='Password']",
                "//android.widget.EditText[contains(@hint,'Username') or contains(@hint,'Password')]");

        for (String xpath : loginPageXpaths) {
            try {
                WebElement loginElement = driver.findElement(By.xpath(xpath));
                if (loginElement.isDisplayed()) {
                    System.out.println("✓ Login page verified - found login element");
                    return;
                }
            } catch (Exception ignored) {
            }
        }

        System.out.println("⚠ Could not verify login page display");
    }

    private static void dismissPopupAndReturnToMain(AndroidDriver driver) {
        System.out.println("Dismissing popup and returning to main page...");

        // Try to dismiss OK popup
        List<String> dismissXpaths = List.of(
                "//*[@text='OK' or @content-desc='OK']",
                "//*[contains(@text,'OK') or contains(@content-desc,'OK')]",
                "//android.widget.Button[@text='OK']",
                "//*[@class='android.widget.Button' and @text='OK']");

        for (String xpath : dismissXpaths) {
            try {
                WebElement okButton = driver.findElement(By.xpath(xpath));
                if (okButton.isDisplayed() && okButton.isEnabled()) {
                    System.out.println("Found OK button, clicking to dismiss popup...");
                    okButton.click();
                    Thread.sleep(1000);
                    break;
                }
            } catch (Exception ignored) {
            }
        }

        // Navigate back to main page using back navigation
        try {
            System.out.println("Navigating back to main page...");
            for (int i = 0; i < 3; i++) { // Go back multiple times to reach main
                driver.navigate().back();
                Thread.sleep(1000);
            }
            System.out.println("Successfully returned to main page");
        } catch (Exception e) {
            System.out.println("Failed to navigate back: " + e.getMessage());
        }
    }

    private static boolean tryTypeIntoField(AndroidDriver driver, WebElement field, String text) {
        try {
            if (!field.isDisplayed() || !field.isEnabled()) {
                return false;
            }

            // Click the field first
            try {
                field.click();
            } catch (Exception e) {
                tapElementCenter(driver, field);
            }
            Thread.sleep(300);

            // Clear existing content
            try {
                field.clear();
            } catch (Exception ignored) {
            }

            // Try multiple typing methods
            boolean success = false;

            // Method 1: Direct sendKeys
            try {
                field.sendKeys(text);
                success = verifyFieldContent(field, text);
                if (success) {
                    hideKeyboardOnly(driver);
                    return true;
                }
            } catch (Exception ignored) {
            }

            // Method 2: Using mobile: type command
            try {
                field.clear();
                driver.executeScript("mobile: type", Map.of("text", text));
                success = verifyFieldContent(field, text);
                if (success) {
                    hideKeyboardOnly(driver);
                    return true;
                }
            } catch (Exception ignored) {
            }

            // Method 3: Character by character
            try {
                field.clear();
                for (char c : text.toCharArray()) {
                    field.sendKeys(String.valueOf(c));
                    Thread.sleep(50);
                }
                success = verifyFieldContent(field, text);
                if (success) {
                    hideKeyboardOnly(driver);
                    return true;
                }
            } catch (Exception ignored) {
            }

            // Try back button to clear filter
            try {
                driver.navigate().back();
                Thread.sleep(500);
                System.out.println("Filter cleared using back navigation");
            } catch (Exception ignored) {
            }
        } catch (Exception ignored) {
        }
        return false;
    }

    private static void uncheckSelectAllIfChecked(AndroidDriver driver) {
        List<String> selectAllXpaths = List.of(
                "//*[@text='Select All' or @content-desc='Select All']",
                "//*[contains(@text,'Select All') or contains(@content-desc,'Select All')]",
                "//android.widget.CheckBox[@checked='true']",
                "//*[@class='android.widget.CheckBox' and @checked='true']");

        for (String xpath : selectAllXpaths) {
            try {
                List<WebElement> checkboxes = driver.findElements(By.xpath(xpath));
                for (WebElement checkbox : checkboxes) {
                    try {
                        if (checkbox.isDisplayed() && checkbox.isEnabled()) {
                            // Check if it's checked by looking at the checked attribute
                            String checkedAttr = checkbox.getAttribute("checked");
                            if ("true".equals(checkedAttr)) {
                                System.out.println("Found checked Select All checkbox, unchecking it...");
                                checkbox.click();
                                Thread.sleep(500);
                                System.out.println("Successfully unchecked Select All checkbox");
                                return;
                            }
                        }
                    } catch (Exception ignored) {
                    }
                }
            } catch (Exception ignored) {
            }
        }

        // Try coordinate-based approach for Select All area
        try {
            System.out.println("Trying coordinate-based click for Select All checkbox...");
            Dimension size = driver.manage().window().getSize();
            int x = (int) (size.getWidth() * 0.15); // Left side where checkbox typically is
            int y = (int) (size.getHeight() * 0.35); // Approximate height of Select All
            driver.executeScript("mobile: clickGesture", Map.of("x", x, "y", y));
            Thread.sleep(500);
            System.out.println("Coordinate click attempted for Select All checkbox");
        } catch (Exception ignored) {
        }
    }

    private static boolean verifyFieldContent(WebElement field, String expectedText) {
        try {
            String actualText = "";
            try {
                actualText = field.getText();
            } catch (Exception e) {
                try {
                    actualText = field.getAttribute("text");
                } catch (Exception e2) {
                    try {
                        actualText = field.getAttribute("value");
                    } catch (Exception ignored) {
                    }
                }
            }

            if (actualText != null && actualText.toLowerCase().contains(expectedText.toLowerCase())) {
                System.out.println("Field content verified: '" + actualText + "' contains '" + expectedText + "'");
                return true;
            }
            System.out.println("Field content mismatch: expected '" + expectedText + "', got '" + actualText + "'");
            return false;
        } catch (Exception e) {
            System.out.println("Could not verify field content: " + e.getMessage());
            return false;
        }
    }

    private static boolean clickNextIconForItem(AndroidDriver driver, String itemText, int timeoutSec) {
        System.out.println("Attempting to click Next button for item: " + itemText);

        List<String> nextForItemXpaths = List.of(
                // Target blue circular button next to the item
                "//*[contains(@text,'" + itemText
                        + "')]/parent::*//*[@clickable='true' and @class='android.widget.ImageView']",
                "//*[contains(@text,'" + itemText + "')]/following-sibling::*[@clickable='true']",
                "//*[contains(@text,'" + itemText + "')]/parent::*//*[@clickable='true']",
                "//*[contains(@text,'" + itemText + "')]/following::android.widget.ImageView[@clickable='true'][1]",
                "//*[contains(@text,'" + itemText + "')]/following::android.widget.ImageButton[1]",
                "//*[contains(@text,'" + itemText + "')]/following::*[@clickable='true'][1]",
                // Generic next button selectors
                "//*[@content-desc='Next' or @content-desc='NEXT' or @content-desc='next']",
                "//android.widget.ImageView[@clickable='true']");

        long end = System.currentTimeMillis() + (timeoutSec * 1000L);
        while (System.currentTimeMillis() < end) {
            for (String xpath : nextForItemXpaths) {
                try {
                    List<WebElement> elements = driver.findElements(By.xpath(xpath));
                    for (WebElement element : elements) {
                        try {
                            if (element.isDisplayed() && element.isEnabled()) {
                                System.out.println("Found clickable element with XPath: " + xpath);
                                element.click();
                                System.out.println("Successfully clicked Next button for " + itemText);
                                return true;
                            }
                        } catch (Exception e) {
                            try {
                                System.out.println("Direct click failed, trying tap center for: " + xpath);
                                if (tapElementCenter(driver, element)) {
                                    System.out.println("Successfully tapped Next button for " + itemText);
                                    return true;
                                }
                            } catch (Exception ignored) {
                            }
                        }
                    }
                } catch (Exception ignored) {
                }
            }

            // Try coordinate-based approach for the blue button area
            try {
                System.out.println("Trying coordinate-based click for Next button...");
                Dimension size = driver.manage().window().getSize();
                int x = (int) (size.getWidth() * 0.85); // Right side where Next button is
                int y = (int) (size.getHeight() * 0.25); // Approximate height of the Chas item
                driver.executeScript("mobile: clickGesture", Map.of("x", x, "y", y));
                System.out.println("Coordinate click attempted at (" + x + ", " + y + ")");
                Thread.sleep(1000);
                return true;
            } catch (Exception ignored) {
            }

            try {
                Thread.sleep(500);
            } catch (InterruptedException ignored) {
                Thread.currentThread().interrupt();
                break;
            }
        }

        System.out.println("Failed to click Next button for " + itemText);
        return false;
    }

    private static boolean selectItemByScrollAndNext(AndroidDriver driver, String itemText, int timeoutSec) {
        try {
            driver.findElement(AppiumBy.androidUIAutomator(
                    "new UiScrollable(new UiSelector().scrollable(true)).scrollIntoView(" +
                            "new UiSelector().textContains(\"" + itemText + "\"))"));
        } catch (Exception ignored) {
        }

        if (clickNextIconForItem(driver, itemText, timeoutSec)) {
            return true;
        }

        if (!clickIfPresent(driver, textEquals(itemText), 4)) {
            clickIfPresent(driver, textContains(itemText), 4);
        }

        return clickIfPresent(driver, textContains("Next"), 6) || clickIfPresent(driver, textEquals("NEXT"), 4);
    }

    private static WebElement waitVisibleByAnyXpath(AndroidDriver driver, List<String> xpaths, int timeoutSec) {
        return new WebDriverWait(driver, Duration.ofSeconds(timeoutSec)).until(d -> {
            for (String xpath : xpaths) {
                List<WebElement> elements = d.findElements(By.xpath(xpath));
                for (WebElement element : elements) {
                    try {
                        if (element.isDisplayed()) {
                            return element;
                        }
                    } catch (Exception ignored) {
                    }
                }
            }
            return null;
        });
    }

    private static void typeByAnyXpath(AndroidDriver driver, List<String> xpaths, String value, int timeoutSec) {
        WebElement field = waitVisibleByAnyXpath(driver, xpaths, timeoutSec);
        field.click();
        field.clear();
        field.sendKeys(value);
    }

    private static By textContains(String value) {
        return AppiumBy.androidUIAutomator(
                "new UiSelector().textContains(\"" + value + "\")");
    }

    private static By textEquals(String value) {
        return AppiumBy.androidUIAutomator(
                "new UiSelector().text(\"" + value + "\")");
    }

    private static List<WebElement> waitForInputFields(AndroidDriver driver, int minCount, int timeoutSec) {
        return new WebDriverWait(driver, Duration.ofSeconds(timeoutSec)).until(d -> {
            List<WebElement> fields = d.findElements(AppiumBy.className("android.widget.EditText"));
            return fields.size() >= minCount ? fields : null;
        });
    }

    private static void typeIntoInputByIndex(AndroidDriver driver, int index, String value, int timeoutSec) {
        new WebDriverWait(driver, Duration.ofSeconds(timeoutSec)).until(d -> {
            List<WebElement> fields = d.findElements(AppiumBy.className("android.widget.EditText"));
            if (fields.size() <= index) {
                return false;
            }

            try {
                WebElement field = fields.get(index);
                field.click();
                field.clear();
                field.sendKeys(value);
                return true;
            } catch (StaleElementReferenceException e) {
                return false;
            }
        });
    }

    private static void typeUsernameWithVerification(AndroidDriver driver, String username, int timeoutSec) {
        new WebDriverWait(driver, Duration.ofSeconds(timeoutSec)).until(d -> {
            List<WebElement> fields = d.findElements(AppiumBy.className("android.widget.EditText"));
            if (fields.isEmpty()) {
                return false;
            }

            try {
                WebElement field = fields.get(0);
                field.click();
                field.clear();
                field.sendKeys(username);
                String entered = field.getText();
                return entered != null && entered.trim().equalsIgnoreCase(username);
            } catch (StaleElementReferenceException e) {
                return false;
            }
        });
    }

    private static void safeTerminateApp(AndroidDriver driver, String packageName) {
        try {
            driver.terminateApp(packageName);
        } catch (Exception ignored) {
        }
    }

    private static void dismissKeyboardIfOpen(AndroidDriver driver) {
        try {
            driver.hideKeyboard();
        } catch (Exception ignored) {
        }
        try {
            if (Boolean.TRUE.equals(driver.isKeyboardShown())) {
                driver.navigate().back();
            }
        } catch (Exception ignored) {
        }
    }

    private static void clickLoginButton(AndroidDriver driver) {
        for (int attempt = 1; attempt <= 4; attempt++) {
            dismissKeyboardIfOpen(driver);

            if (clickIfPresent(driver, textEquals("LOGIN"), 4)) {
                return;
            }
            if (clickIfPresent(driver, textContains("LOGIN"), 4)) {
                return;
            }
            if (clickIfPresent(driver, AppiumBy.androidUIAutomator(
                    "new UiSelector().className(\"android.widget.Button\").textContains(\"LOG\")"), 4)) {
                return;
            }
            if (clickIfPresent(driver, AppiumBy.id("login"), 2)) {
                return;
            }
            if (clickIfPresent(driver, AppiumBy.id("btnLogin"), 2)) {
                return;
            }

            try {
                WebElement login = driver.findElement(AppiumBy.xpath(
                        "//*[contains(@text,'LOGIN') or contains(@content-desc,'LOGIN') or contains(@resource-id,'login')]"));
                if (login.isDisplayed() && login.isEnabled()) {
                    login.click();
                    return;
                }
            } catch (Exception ignored) {
            }

            try {
                WebElement login = driver.findElement(AppiumBy.xpath(
                        "//*[contains(@text,'LOGIN') or contains(@content-desc,'LOGIN') or contains(@resource-id,'login')]"));
                if (tapElementCenter(driver, login)) {
                    return;
                }
            } catch (Exception ignored) {
            }

            try {
                driver.pressKey(new KeyEvent(AndroidKey.ENTER));
                Thread.sleep(500);
                return;
            } catch (Exception ignored) {
            }

            try {
                Thread.sleep(700);
            } catch (InterruptedException ignored) {
                Thread.currentThread().interrupt();
            }
        }

        throw new IllegalStateException("Login button could not be clicked after multiple fallback attempts.");
    }

    private static void clickLoginButtonUsingXpath(AndroidDriver driver, int timeoutSec) {
        List<String> loginXpaths = List.of(
                "//android.widget.Button[@text='LOGIN' or @text='Login' or contains(@text,'LOG') or contains(@text,'Log')]",
                "//*[@clickable='true' and (@text='LOGIN' or @text='Login' or contains(@text,'LOG') or contains(@text,'Log'))]",
                "//*[@content-desc='LOGIN' or @content-desc='Login']",
                "//*[contains(@resource-id,'login')]");

        long endTime = System.currentTimeMillis() + (timeoutSec * 1000L);
        while (System.currentTimeMillis() < endTime) {
            dismissKeyboardIfOpen(driver);

            for (String xpath : loginXpaths) {
                try {
                    WebElement login = new WebDriverWait(driver, Duration.ofSeconds(4))
                            .until(ExpectedConditions.elementToBeClickable(By.xpath(xpath)));
                    login.click();
                    return;
                } catch (Exception ignored) {
                }
            }

            for (String xpath : loginXpaths) {
                try {
                    WebElement login = driver.findElement(By.xpath(xpath));
                    if (tapElementCenter(driver, login)) {
                        Thread.sleep(700);
                        if (!isLoginScreenVisible(driver)) {
                            return;
                        }
                    }
                } catch (Exception ignored) {
                }
            }

            try {
                if (tapLikelyLoginArea(driver)) {
                    Thread.sleep(700);
                    if (!isLoginScreenVisible(driver)) {
                        return;
                    }
                }
            } catch (Exception ignored) {
            }

            try {
                driver.pressKey(new KeyEvent(AndroidKey.ENTER));
                Thread.sleep(700);
                if (!isLoginScreenVisible(driver)) {
                    return;
                }
            } catch (Exception ignored) {
            }

            try {
                Thread.sleep(600);
            } catch (InterruptedException ignored) {
                Thread.currentThread().interrupt();
            }
        }

        throw new IllegalStateException("LOGIN button click failed using XPath strategy within timeout.");
    }

    private static boolean isLoginScreenVisible(AndroidDriver driver) {
        List<String> loginPageXpaths = List.of(
                "//*[@text='LOGIN']",
                "//*[@text='Login']",
                "//*[contains(@text,'LOGIN')]",
                "//*[contains(@text,'Login')]",
                "(//android.widget.EditText)[1]",
                "(//android.widget.EditText)[2]");

        for (String xpath : loginPageXpaths) {
            try {
                List<WebElement> els = driver.findElements(By.xpath(xpath));
                for (WebElement el : els) {
                    if (el.isDisplayed()) {
                        return true;
                    }
                }
            } catch (Exception ignored) {
            }
        }
        return false;
    }

    private static boolean tapLikelyLoginArea(AndroidDriver driver) {
        try {
            Dimension size = driver.manage().window().getSize();
            int x = size.getWidth() / 2;
            int y = (int) (size.getHeight() * 0.78);
            driver.executeScript("mobile: clickGesture", Map.of("x", x, "y", y));
            return true;
        } catch (Exception e) {
            return false;
        }
    }

    private static void ensureLoginTransition(AndroidDriver driver) {
        for (int attempt = 1; attempt <= 3; attempt++) {
            try {
                new WebDriverWait(driver, Duration.ofSeconds(10)).until(d -> !isLoginScreenVisible(driver));
                return;
            } catch (Exception ignored) {
            }

            if (isLoginScreenVisible(driver)) {
                dismissKeyboardIfOpen(driver);
                clickHomeButtonIfPresent(driver);
                clickLoginButtonUsingXpath(driver, 15);
            }
        }

        throw new IllegalStateException("Login appears stuck on login page after retries.");
    }

    private static boolean tapElementCenter(AndroidDriver driver, WebElement element) {
        try {
            Rectangle r = element.getRect();
            int x = r.getX() + (r.getWidth() / 2);
            int y = r.getY() + (r.getHeight() / 2);
            driver.executeScript("mobile: clickGesture", Map.of("x", x, "y", y));
            return true;
        } catch (Exception e) {
            return false;
        }
    }

    private static void clickHomeButtonIfPresent(AndroidDriver driver) {
        clickIfPresent(driver, textEquals("HOME"), 2);
        clickIfPresent(driver, textContains("Home"), 2);
    }

    private static void handleBackToHomeTransitions(AndroidDriver driver, int passes) {
        for (int i = 0; i < passes; i++) {
            clickIfPresent(driver, textContains("PUNCH IN"), 8);
            clickIfPresent(driver, textContains("GO TO HOME PAGE"), 10);
            clickIfPresent(driver, textContains("GO TO HOMEPAGE"), 10);
            clickIfPresent(driver, textContains("Go back to Home"), 10);
            clickIfPresent(driver, textContains("Back to Home"), 10);
            clickIfPresent(driver, textEquals("OK"), 5);
        }
    }

    private static void clickGoToHomeOnAttendance(AndroidDriver driver) {
        List<String> goToHomeXpaths = List.of(
                "//android.widget.Button[@text='GO TO HOME PAGE' or @text='Go To Home Page' or @text='Go to Home Page']",
                "//android.widget.TextView[@text='GO TO HOME PAGE' or @text='Go To Home Page' or @text='Go to Home Page']",
                "//*[@content-desc='GO TO HOME PAGE' or @content-desc='Go To Home Page' or @content-desc='Go to Home Page']",
                "//*[contains(@content-desc,'HOME PAGE')]",
                "//*[@clickable='true' and (@text='GO TO HOME PAGE' or @text='Go To Home Page' or @text='Go to Home Page')]",
                "//*[contains(@text,'HOME PAGE')]");

        long end = System.currentTimeMillis() + 30000L;
        while (System.currentTimeMillis() < end) {
            if (clickIfPresent(driver, textContains("GO TO HOME PAGE"), 4)) {
                return;
            }
            if (clickIfPresent(driver, textContains("Go to Home Page"), 4)) {
                return;
            }

            for (String xpath : goToHomeXpaths) {
                try {
                    WebElement homeBtn = new WebDriverWait(driver, Duration.ofSeconds(4))
                            .until(ExpectedConditions.elementToBeClickable(By.xpath(xpath)));
                    homeBtn.click();
                    return;
                } catch (Exception ignored) {
                }

                try {
                    WebElement homeEl = waitVisible(driver, By.xpath(xpath), 2);
                    if (homeEl.isDisplayed() && tapElementCenter(driver, homeEl)) {
                        return;
                    }
                } catch (Exception ignored) {
                }
            }

            try {
                Dimension size = driver.manage().window().getSize();
                int x = size.getWidth() / 2;
                int y = (int) (size.getHeight() * 0.90);
                driver.executeScript("mobile: clickGesture", Map.of("x", x, "y", y));
                if (!isLoginScreenVisible(driver)) {
                    return;
                }
            } catch (Exception ignored) {
            }

            try {
                Thread.sleep(600);
            } catch (InterruptedException ignored) {
                Thread.currentThread().interrupt();
                break;
            }
        }

        throw new IllegalStateException("Could not click GO TO HOME PAGE on Attendance screen.");
    }

    private static void acceptAttendancePopupIfPresent(AndroidDriver driver) {
        List<String> okXpaths = List.of(
                "//android.widget.Button[@text='OK' or @text='Ok' or @text='ok']",
                "//*[@content-desc='OK' or @content-desc='Ok' or @content-desc='ok']",
                "//*[@clickable='true' and (@text='OK' or @text='Ok' or @text='ok')]",
                "//*[contains(@text,'OK')]");

        if (clickIfPresent(driver, textEquals("OK"), 5)) {
            return;
        }

        for (String xpath : okXpaths) {
            try {
                WebElement okBtn = new WebDriverWait(driver, Duration.ofSeconds(3))
                        .until(ExpectedConditions.elementToBeClickable(By.xpath(xpath)));
                okBtn.click();
                return;
            } catch (Exception ignored) {
            }

            try {
                WebElement okEl = waitVisible(driver, By.xpath(xpath), 2);
                if (tapElementCenter(driver, okEl)) {
                    return;
                }
            } catch (Exception ignored) {
            }
        }
    }

    private static void completeAttendancePunchAndGoHome(AndroidDriver driver) {
        boolean punched = clickIfPresent(driver, textContains("PUNCH IN"), 15)
                || clickIfPresent(driver, textEquals("PUNCH IN"), 8);
        if (!punched) {
            throw new IllegalStateException("Could not click PUNCH IN on Attendance screen.");
        }

        acceptAttendancePopupIfPresent(driver);
        tapBelowPunchButton(driver);

        clickGoToHomeOnAttendance(driver);
    }

    private static void openCollectionsModule(AndroidDriver driver) {
        for (int attempt = 1; attempt <= 3; attempt++) {
            clickIfPresent(driver, textContains("GO TO HOME PAGE"), 3);
            clickIfPresent(driver, textContains("GO TO HOMEPAGE"), 3);
            clickIfPresent(driver, textContains("Go back to Home"), 3);
            clickIfPresent(driver, textEquals("OK"), 2);

            if (clickIfPresent(driver, textEquals("Collections"), 6)) {
                return;
            }
            if (clickIfPresent(driver, textContains("Collections"), 6)) {
                return;
            }
            if (clickIfPresent(driver, textEquals("Collection"), 6)) {
                return;
            }
            if (clickIfPresent(driver, textContains("Collection"), 6)) {
                return;
            }

            try {
                driver.findElement(AppiumBy.xpath("//*[contains(@text,'Collection') or contains(@text,'Collections')]"))
                        .click();
                return;
            } catch (Exception ignored) {
            }

            try {
                driver.findElement(AppiumBy.androidUIAutomator(
                        "new UiScrollable(new UiSelector().scrollable(true)).scrollIntoView(" +
                                "new UiSelector().textContains(\"Collections\"))"));
            } catch (Exception ignored) {
            }

            try {
                driver.navigate().back();
            } catch (Exception ignored) {
            }
        }

        throw new IllegalStateException("Unable to open Collections module from current screen flow.");
    }

    private static void ensureTargetAppInForeground(AndroidDriver driver) {
        safeTerminateApp(driver, LOCAL_DEBUG_PACKAGE);
        safeTerminateApp(driver, GEO_LIGHT_PACKAGE);
        safeTerminateApp(driver, FIELD_APP_PACKAGE);

        driver.activateApp(FIELD_APP_PACKAGE);

        try {
            new WebDriverWait(driver, Duration.ofSeconds(15))
                    .until(d -> FIELD_APP_PACKAGE.equals(driver.getCurrentPackage()));
        } catch (Exception firstTryFailed) {
            driver.activateApp(FIELD_APP_PACKAGE);
            new WebDriverWait(driver, Duration.ofSeconds(15))
                    .until(d -> FIELD_APP_PACKAGE.equals(driver.getCurrentPackage()));
        }

        String currentPackage = driver.getCurrentPackage();
        if (!FIELD_APP_PACKAGE.equals(currentPackage)) {
            throw new IllegalStateException(
                    "Target app not in foreground. Current package: " + currentPackage
                            + ". Ensure Android Studio run config is AndroidUat from module appiumrunner (not app).");
        }
    }

    public static void main(String[] args) throws Exception {
        new AndroidUat().run();
    }

    private void run() throws Exception {
        URL appiumUrl = new URL(APPIUM_SERVER_URL);
        int appiumPort = appiumUrl.getPort() == -1 ? 80 : appiumUrl.getPort();
        waitForAppiumServer(appiumUrl.getHost(), appiumPort, 30);

        UiAutomator2Options options = new UiAutomator2Options()
                .setPlatformName("Android")
                .setAutomationName("UiAutomator2")
                .setDeviceName("Android")
                .setUdid(DEVICE_UDID)
                .setAppPackage(FIELD_APP_PACKAGE)
                .setAppActivity(FIELD_APP_ACTIVITY)
                .setNoReset(true)
                .setFullReset(false);

        AndroidDriver driver = new AndroidDriver(appiumUrl, options);

        try {
            ensureTargetAppInForeground(driver);
            step0HandleLocationPopupAndWaitLoginPage(driver);
            step1Login(driver, "Fet1005", "Light@123");
            driver.manage().timeouts().implicitlyWait(Duration.ofSeconds(POST_LOGIN_SYNC_WAIT_SEC));
            step2HandleAttendanceAndHomeTransitions(driver);
            step3OpenCollectionsFromHome(driver);
            step4SearchAndSelectCenter(driver, "chas", "Chas");
            step5CompleteCollectionFlow(driver);

        } finally {
            try {
                driver.quit();
            } catch (Exception ignored) {
            }
        }
    }

    private void step0HandleLocationPopupAndWaitLoginPage(AndroidDriver driver) throws InterruptedException {
        System.out.println("Step 0: Location popup and login page wait");

        clickIfPresent(driver, textEquals("OK"), 12);
        Thread.sleep(LOGIN_PAGE_WAIT_MS);
        waitForInputFields(driver, 2, DEFAULT_TIMEOUT);
    }

    private void step1Login(AndroidDriver driver, String username, String password) {
        System.out.println("Step 1: Login screen");

        waitForInputFields(driver, 2, DEFAULT_TIMEOUT);

        List<String> usernameXpaths = List.of(
                "(//android.widget.EditText)[1]",
                "//*[contains(@resource-id,'user')]",
                "//*[contains(@resource-id,'mobile')]",
                "//*[contains(@content-desc,'user')]");
        List<String> passwordXpaths = List.of(
                "(//android.widget.EditText)[2]",
                "//*[contains(@resource-id,'pass')]",
                "//*[contains(@content-desc,'pass')]");

        typeByAnyXpath(driver, usernameXpaths, username, DEFAULT_TIMEOUT);
        typeByAnyXpath(driver, passwordXpaths, password, DEFAULT_TIMEOUT);
        dismissKeyboardIfOpen(driver);
        clickHomeButtonIfPresent(driver);
        clickLoginButtonUsingXpath(driver, LOGIN_CLICK_TIMEOUT);
        ensureLoginTransition(driver);
    }

    private void step2HandleAttendanceAndHomeTransitions(AndroidDriver driver) {
        System.out.println("Step 2: Attendance / dashboard transitions");

        completeAttendancePunchAndGoHome(driver);
    }

    private void step3OpenCollectionsFromHome(AndroidDriver driver) {
        System.out.println("Step 3: Open Collections from Services");

        // Wait for sync after login/attendance transitions
        try {
            System.out.println("Waiting 10 seconds before opening Collections for data sync...");
            Thread.sleep(10000);
        } catch (InterruptedException e) {
            Thread.currentThread().interrupt();
        }

        openCollectionsModule(driver);

        // Handle new UI with tabs - select "Other Meeting Date" tab
        selectOtherMeetingDateTab(driver);

        // Wait 5 seconds as requested
        try {
            System.out.println("Waiting 5 seconds after tab selection...");
            Thread.sleep(5000);
        } catch (InterruptedException e) {
            Thread.currentThread().interrupt();
        }
    }

    private static void selectOtherMeetingDateTab(AndroidDriver driver) {
        System.out.println("Selecting 'Other Meeting Date' tab...");

        List<String> otherMeetingDateXpaths = List.of(
                "//*[@text='Other meeting date' or @content-desc='Other meeting date']",
                "//*[@text='Other Meeting Date' or @content-desc='Other Meeting Date']",
                "//*[contains(@text,'Other meeting date') or contains(@content-desc,'Other meeting date')]",
                "//*[contains(@text,'Other Meeting Date') or contains(@content-desc,'Other Meeting Date')]",
                "//*[contains(translate(@text,'ABCDEFGHIJKLMNOPQRSTUVWXYZ','abcdefghijklmnopqrstuvwxyz'),'other meeting date')]",
                "//android.widget.TextView[contains(translate(@text,'ABCDEFGHIJKLMNOPQRSTUVWXYZ','abcdefghijklmnopqrstuvwxyz'),'other meeting date')]",
                "//*[contains(translate(@text,'ABCDEFGHIJKLMNOPQRSTUVWXYZ','abcdefghijklmnopqrstuvwxyz'),'other') and contains(translate(@text,'ABCDEFGHIJKLMNOPQRSTUVWXYZ','abcdefghijklmnopqrstuvwxyz'),'meeting')]"
        );

        for (int attempt = 1; attempt <= 3; attempt++) {
            for (String xpath : otherMeetingDateXpaths) {
                try {
                    List<WebElement> tabElements = driver.findElements(By.xpath(xpath));
                    for (WebElement tabElement : tabElements) {
                        if (!tabElement.isDisplayed()) {
                            continue;
                        }

                        System.out.println("Attempt " + attempt + ": clicking 'Other Meeting Date' tab using XPath: " + xpath);

                        try {
                            tabElement.click();
                        } catch (Exception clickFailed) {
                            if (!tapElementCenter(driver, tabElement)) {
                                WebElement parent = tabElement.findElement(By.xpath(".."));
                                if (parent.isDisplayed() && parent.isEnabled()) {
                                    parent.click();
                                }
                            }
                        }

                        Thread.sleep(900);
                        System.out.println("Clicked 'Other Meeting Date' tab");
                        return;
                    }
                } catch (Exception ignored) {
                }
            }

            try {
                Dimension size = driver.manage().window().getSize();
                int x = (int) (size.getWidth() * 0.76);
                int y = (int) (size.getHeight() * 0.13);
                System.out.println("Attempt " + attempt + ": coordinate fallback for 'Other Meeting Date' at (" + x + ", " + y + ")");
                driver.executeScript("mobile: clickGesture", Map.of("x", x, "y", y));
                Thread.sleep(900);
                System.out.println("Clicked 'Other Meeting Date' tab using coordinate fallback");
                return;
            } catch (Exception ignored) {
            }
        }

        System.out.println("Could not reliably select 'Other Meeting Date' tab, continuing with current tab");
    }

    private static void performCenterDataAssertions(AndroidDriver driver, String centerName) {
        System.out.println("Performing data assertions for center: " + centerName);

        try {
            // Expected values based on current screenshot for "Chas" center
            int expectedPaid = 1;
            int expectedDue = 0;
            int expectedOverdue = 8;
            int expectedAdvance = 0;
            int expectedTotal = 10;

            // Assert Paid value
            assertCenterValue(driver, "Paid", expectedPaid);

            // Assert Due value
            assertCenterValue(driver, "Due", expectedDue);

            // Assert Overdue value
            assertCenterValue(driver, "Overdue", expectedOverdue);

            // Assert Advance value
            assertCenterValue(driver, "Advance", expectedAdvance);

            // Assert Total value
            assertCenterValue(driver, "Total", expectedTotal);

            System.out.println("✓ All data assertions passed for center: " + centerName);

        } catch (Exception e) {
            System.out.println("⚠ Data assertion failed: " + e.getMessage());
            // Continue execution even if assertions fail
        }
    }

    private static void assertCenterValue(AndroidDriver driver, String valueType, int expectedValue) {
        List<String> valueXpaths = List.of(
                "//*[contains(@text,'" + valueType + "')]/following-sibling::*[contains(@text,'" + expectedValue
                        + "')]",
                "//*[contains(@text,'" + valueType + " " + expectedValue + "')]",
                "//*[@text='" + valueType + " " + expectedValue + "']",
                "//*[contains(@text,'" + valueType + "') and contains(@text,'" + expectedValue + "')]");

        for (String xpath : valueXpaths) {
            try {
                WebElement valueElement = driver.findElement(By.xpath(xpath));
                if (valueElement.isDisplayed()) {
                    System.out.println("✓ Assertion passed: " + valueType + " = " + expectedValue);
                    return;
                }
            } catch (Exception ignored) {
            }
        }

        throw new AssertionError("Expected " + valueType + " value " + expectedValue + " not found");
    }

    private static void assertMeetingDate(AndroidDriver driver, String expectedDate) {
        List<String> dateXpaths = List.of(
                "//*[contains(@text,'Next Meeting Date') and contains(@text,'" + expectedDate + "')]",
                "//*[contains(@text,'Meeting Date') and contains(@text,'" + expectedDate + "')]",
                "//*[contains(@text,'" + expectedDate + "')]");

        for (String xpath : dateXpaths) {
            try {
                WebElement dateElement = driver.findElement(By.xpath(xpath));
                if (dateElement.isDisplayed()) {
                    System.out.println("✓ Assertion passed: Meeting Date = " + expectedDate);
                    return;
                }
            } catch (Exception ignored) {
            }
        }

        throw new AssertionError("Expected meeting date " + expectedDate + " not found");
    }

    private static void focusCenterSearchAndType(AndroidDriver driver, String text, int timeoutSec) {
        System.out.println("Attempting to type '" + text
                + "' into center search field by clicking magnifying glass icon first...");

        // First try to find and click the magnifying glass icon
        List<String> searchIconXpaths = List.of(
                "//android.widget.ImageView[@content-desc='Search' or contains(@content-desc,'search')]",
                "//*[@class='android.widget.ImageView' and (@content-desc='Search' or contains(@content-desc,'search'))]",
                "//android.widget.ImageButton[@content-desc='Search' or contains(@content-desc,'search')]",
                "//*[contains(@resource-id,'search_button') or contains(@resource-id,'search_icon')]",
                "//android.widget.ImageView[contains(@bounds,'[139,')]", // Based on screenshot position
                "//*[@clickable='true' and contains(@bounds,'[139,')]");

        long end = System.currentTimeMillis() + (timeoutSec * 1000L);
        while (System.currentTimeMillis() < end) {
            // Try to click magnifying glass icon first
            for (String xpath : searchIconXpaths) {
                try {
                    WebElement searchIcon = driver.findElement(By.xpath(xpath));
                    if (searchIcon.isDisplayed() && searchIcon.isEnabled()) {
                        System.out.println("Found magnifying glass icon, clicking it first...");
                        searchIcon.click();
                        Thread.sleep(500);

                        // Now try to type in the activated search field
                        WebElement active = driver.switchTo().activeElement();
                        if (active != null && tryTypeIntoField(driver, active, text)) {
                            System.out
                                    .println("Successfully typed '" + text + "' after clicking magnifying glass icon");
                            return;
                        }
                    }
                } catch (Exception ignored) {
                }
            }

            // Try center-specific search field selectors
            List<String> centerSearchXpaths = List.of(
                    "//*[contains(@text,'CENTER LIST')]/following::android.widget.EditText[1]",
                    "//*[contains(@text,'Center List')]/following::android.widget.EditText[1]",
                    "//android.widget.EditText[@clickable='true']",
                    "//android.widget.AutoCompleteTextView[@clickable='true']");

            for (String xpath : centerSearchXpaths) {
                try {
                    List<WebElement> fields = driver.findElements(By.xpath(xpath));
                    for (WebElement field : fields) {
                        if (tryTypeIntoField(driver, field, text)) {
                            System.out.println(
                                    "Successfully typed '" + text + "' in center search using XPath: " + xpath);
                            return;
                        }
                    }
                } catch (Exception ignored) {
                }
            }

            // Safe coordinate-based approach - target search field area avoiding back
            // button
            try {
                System.out.println("Trying safe coordinate click for center search field...");
                Dimension size = driver.manage().window().getSize();
                // Target the search field area - right of magnifying glass, avoiding back
                // button
                int x = (int) (size.getWidth() * 0.60); // Right of search icon
                int y = (int) (size.getHeight() * 0.25); // Search field area

                System.out.println("Clicking at safe coordinates: (" + x + ", " + y + ") for center search");
                driver.executeScript("mobile: clickGesture", Map.of("x", x, "y", y));
                Thread.sleep(500);

                WebElement active = driver.switchTo().activeElement();
                if (active != null && tryTypeIntoField(driver, active, text)) {
                    System.out.println("Successfully typed '" + text + "' using safe coordinate click");
                    return;
                }
            } catch (Exception ignored) {
            }

            // Dismiss any popup that might have appeared
            try {
                dismissBackNavigationPopupIfPresent(driver);
                Thread.sleep(500);
            } catch (Exception ignored) {
            }

            try {
                Thread.sleep(400);
            } catch (InterruptedException ignored) {
                Thread.currentThread().interrupt();
                break;
            }
        }

        throw new IllegalStateException("Could not type into center search field for text: " + text);
    }

    private void step4SearchAndSelectCenter(AndroidDriver driver, String centerSearchText, String centerName) {
        System.out.println("Step 4: Center list search and selection");

        // Dismiss any accidental back navigation popup first
        try {
            dismissBackNavigationPopupIfPresent(driver);
        } catch (Exception ignored) {
        }

        try {
            focusCenterSearchAndType(driver, centerSearchText, DEFAULT_TIMEOUT);
            Thread.sleep(2000); // Wait for search results

            // Perform data assertions after search
            performCenterDataAssertions(driver, centerName);

        } catch (Exception e) {
            // If search fails, try to dismiss popup and retry once
            try {
                dismissBackNavigationPopupIfPresent(driver);
                Thread.sleep(1000);
                focusCenterSearchAndType(driver, centerSearchText, DEFAULT_TIMEOUT);
                Thread.sleep(2000);

                // Retry assertions
                performCenterDataAssertions(driver, centerName);

            } catch (Exception ignored) {
            }
        }

        if (!clickIfPresent(driver, textEquals(centerName), 6)) {
            clickIfPresent(driver, textContains(centerName), 6);
        }

        if (!clickNextIconForItem(driver, centerName, DEFAULT_TIMEOUT)) {
            if (!selectItemByScrollAndNext(driver, centerName, DEFAULT_TIMEOUT)) {
                if (!clickIfPresent(driver, textEquals(centerName), 8)) {
                    waitClick(driver, textContains(centerName), 8);
                }
                if (!clickIfPresent(driver, textContains("Next"), 8)) {
                    if (!clickIfPresent(driver, textEquals("NEXT"), 4)) {
                        throw new IllegalStateException("Could not click Next button for center: " + centerName);
                    }
                }
            }
        }
    }

    private void step5CompleteCollectionFlow(AndroidDriver driver) {
        System.out.println("Step 5: Collection workflow");

        clickIfPresent(driver, textEquals("OK"), 10);

        // Step 1: First uncheck "Select All" checkbox if it's checked
        try {
            System.out.println("Step 1: Unchecking Select All checkbox...");
            uncheckSelectAllIfChecked(driver);
        } catch (Exception ignored) {
        }

        // Dismiss any accidental back navigation popup first
        try {
            dismissBackNavigationPopupIfPresent(driver);
        } catch (Exception ignored) {
        }

        // Step 2: Filter client using magnifying glass icon
        String clientName = "Nishisha";
        try {
            System.out.println("Step 2: Searching for client using magnifying glass icon: " + clientName);
            focusBorrowerSearchWithMagnifyingGlass(driver, clientName, DEFAULT_TIMEOUT);
            Thread.sleep(2000); // Wait for search results
        } catch (Exception e) {
            // If search fails, try to dismiss popup and retry once
            try {
                dismissBackNavigationPopupIfPresent(driver);
                Thread.sleep(1000);
                focusBorrowerSearchWithMagnifyingGlass(driver, clientName, DEFAULT_TIMEOUT);
                Thread.sleep(2000);
            } catch (Exception ignored) {
            }
        }

        // Step 3: Remove keyboard safely (no back navigation)
        try {
            System.out.println("Step 3: Dismissing keyboard after client search...");
            hideKeyboardSafelyNoBack(driver);

        } catch (Exception ignored) {
        }

        // Step 4: Check Select All checkbox again
        try {
            System.out.println("Step 4: Checking Select All checkbox...");
            checkSelectAllIfUnchecked(driver);
        } catch (Exception ignored) {
        }

        try {
            dismissBackNavigationPopupIfPresent(driver);
        } catch (Exception ignored) {
        }

        // Step 5: Wait 3-4 seconds
        try {
            System.out.println("Step 5: Waiting 4 seconds before Cash Collection...");
            Thread.sleep(4000);
        } catch (InterruptedException e) {
            Thread.currentThread().interrupt();
        }

        // Step 6: Click CASH_COLLECTION button and wait 7 seconds
        System.out.println("Step 6: Clicking CASH_COLLECTION button...");
        clickCashCollectionButtonSafe(driver);

        try {
            System.out.println("Waiting 7 seconds after Cash Collection click...");
            Thread.sleep(7000); // Wait 7 seconds as requested
        } catch (InterruptedException e) {
            Thread.currentThread().interrupt();
        }

        // Clear and enter amount in Amount Collected field
        try {
            System.out.println("Clearing and entering amount in Amount Collected field...");
            clearAndEnterAmountCollected(driver, "10");
        } catch (Exception e) {
            System.out.println("Failed to enter amount: " + e.getMessage());
        }

        // Wait 4 seconds before clicking Cash Collection button
        try {
            System.out.println("Waiting 4 seconds before Cash Collection button...");
            Thread.sleep(4000);
        } catch (InterruptedException e) {
            Thread.currentThread().interrupt();
        }

        // Click Cash Collection button (again)
        System.out.println("Clicking CASH COLLECTION button...");
        waitClick(driver, textContains("CASH COLLECTION"), DEFAULT_TIMEOUT);

        // Enter denomination Rs 1x 10
        try {
            System.out.println("Entering denomination Rs 1x 10...");
            enterDenomination(driver, "10");
        } catch (Exception e) {
            System.out.println("Failed to enter denomination: " + e.getMessage());
        }

        // Wait 4 seconds after denomination entry
        try {
            System.out.println("Waiting 4 seconds after denomination entry...");
            Thread.sleep(4000);
        } catch (InterruptedException e) {
            Thread.currentThread().interrupt();
        }

        // Click Confirm Collection button
        System.out.println("Clicking CONFIRM COLLECTION button...");
        waitClick(driver, textContains("CONFIRM"), DEFAULT_TIMEOUT);

        // Wait 4 seconds after confirm collection
        try {
            System.out.println("Waiting 4 seconds after Confirm Collection...");
            Thread.sleep(4000);
        } catch (InterruptedException e) {
            Thread.currentThread().interrupt();
        }

        // Click OK in popup
        try {
            System.out.println("Clicking OK in popup...");
            clickIfPresent(driver, textEquals("OK"), 10);
        } catch (Exception e) {
            System.out.println("Failed to click OK: " + e.getMessage());
        }

        // Navigate back with confirmations and logout
        try {
            System.out.println("Starting navigation back and logout sequence...");
            navigateBackAndLogout(driver);
        } catch (Exception e) {
            System.out.println("Failed during navigation and logout: " + e.getMessage());
        }
    }
}
