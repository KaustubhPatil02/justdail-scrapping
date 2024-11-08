from selenium import webdriver
from selenium.webdriver.common.by import By
import time

# Set up the WebDriver (replace with the path to your WebDriver executable if necessary)
driver = webdriver.Chrome()

# Open the Justdial page (replace with the actual URL)
url = "https://www.justdial.com/jdmart/Mumbai/Occasionz-Events-Near-Shalom-Residency-Mira-Road-East/022PXX22-XX22-120123220004-D6Y2_BZDET/catalogue?nid=11236154"
driver.get(url)
time.sleep(3)  # Give the page time to load

try:
    # Locate the Address heading element
    address_heading_element = driver.find_element(By.XPATH, "//div[@role='heading' and contains(@class, 'rightaside_title') and text()='Address']")
    print("Address Heading found:", address_heading_element.text)

    # Locate the actual address content element
    address_content_element = driver.find_element(By.XPATH, "//address[contains(@class, 'aside_address')]")
    print("Address Content found:", address_content_element.text)

    # Locate the Contact element using XPath
    contact_element = driver.find_element(By.XPATH, "//div[contains(@class, 'aside_address') and contains(@class, 'color111') and text()='Contact']")
    print("Contact element found:", contact_element.text)

    # Locate the phone number element
    phone_number_element = driver.find_element(By.XPATH, "//div[@id='catalogue_addr_shownum']//div[contains(@class, 'font16') and contains(@class, 'color007')]")
    print("Phone Number found:", phone_number_element.text)

except Exception as e:
    print("Error finding an element:", e)

# Close the browser
driver.quit()
