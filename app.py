from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Set up the WebDriver (replace with the path to your WebDriver executable if necessary)
driver = webdriver.Chrome()

# Function to scrape contact details
def scrape_contacts(url):
    # Open the Justdial page
    driver.get(url)
    print("Page loaded.")  # Debugging statement

    try:
        # Wait until the listings are present in the HTML
        listings = WebDriverWait(driver, 10).until(
            EC.presence_of_all_elements_located((By.CLASS_NAME, 'store-details'))  # Replace with correct class name
        )
        print(f"Found {len(listings)} listings.")  # Debugging statement

        contacts = []
        for listing in listings:
            try:
                # Extract the business name
                name = listing.find_element(By.CLASS_NAME, 'name-class').text  # Replace with actual class
                print(f"Business name found: {name}")  # Debugging statement

                # Extract the contact details
                contact = listing.find_element(By.CLASS_NAME, 'contact-class').text  # Replace with actual class
                print(f"Contact found: {contact}")  # Debugging statement
                
                contacts.append({'Name': name, 'Contact': contact})
            except Exception as e:
                print("Error extracting data:", e)  # Print any exceptions for debugging
                pass

    except Exception as e:
        print("No listings found or page took too long to load.", e)
        contacts = []

    return contacts

# Usage
url = "https://www.justdial.com/Mumbai/Corporate-Party-Organisers/nct-11236154"  # Replace with actual URL
contacts = scrape_contacts(url)

# Output contacts in the terminal
for contact in contacts:
    print(f"Business Name: {contact['Name']}")
    print(f"Contact: {contact['Contact']}")
    print("-" * 30)  # Separator for readability

# Close the browser
driver.quit()
