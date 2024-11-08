from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

# Set up the WebDriver (replace with the path to your WebDriver executable if necessary)
driver = webdriver.Chrome()

# Open the Justdial page (replace with the actual URL)
url = "https://www.justdial.com/Mumbai/Hotels/nct-10255012"
driver.get(url)

# Wait for the contact numbers to load using WebDriverWait
try:
    # Wait until the contact numbers are loaded in the page
    WebDriverWait(driver, 10).until(
        EC.presence_of_all_elements_located((By.XPATH, "//span[@class='jsx-915cb403736563fc callcontent callNowAnchor']"))
    )

    # Locate all contact number elements using the correct XPath
    contact_number_elements = driver.find_elements(By.XPATH, "//span[@class='jsx-915cb403736563fc callcontent callNowAnchor']")
    
    # Check if any contact numbers were found
    if contact_number_elements:
        for index, contact_number_element in enumerate(contact_number_elements, start=1):
            # Extract the contact number text directly from the element using 'textContent'
            contact_number = contact_number_element.get_attribute('textContent')
            print(f"Contact Number {index} found: {contact_number.strip()}")
    else:
        print("No contact numbers found.")

except Exception as e:
    print("Error finding contact numbers:", e)

# Close the browser
driver.quit()



# from selenium import webdriver
# from selenium.webdriver.common.by import By
# import time

# # Set up the WebDriver (replace with the path to your WebDriver executable if necessary)
# driver = webdriver.Chrome()

# # Open the Justdial page (replace with the actual URL)
# url = "https://www.justdial.com/jdmart/Mumbai/KSYNERGY-INTEGRATED-MARKETING-COMMUNICATIONS-INDIA-PVT-LTD-Near-Mcdonald-Malad-West/022PXX22-XX22-200205140515-P9V2_BZDET/catalogue?nid=11236154"
# driver.get(url)
# time.sleep(3)  # Give the page time to load

# try:
#     # Locate the contact number element using the provided XPath
#     contact_number_element = driver.find_element(By.XPATH, "//*[@id='022PXX22.XX22.230131161808.L7B4']/div/div[2]/div[4]/div[1]/div[1]/div")
    
#     # Print the contact number
#     print("Contact Number found:", contact_number_element.text)

# except Exception as e:
#     print("Error finding the contact number:", e)

# # Close the browser
# driver.quit()
