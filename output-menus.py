from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
import time
import os 

MENUS = ['menu', 'thanksgiving']
DIR_PATH = os.path.dirname(os.path.realpath(__file__))

def take_screenshot(html_file_path, output_file_path, resolution=(1920, 1080)):
    # Set up Chrome options
    chrome_options = Options()
    #chrome_options.add_argument("--headless")  # Run in headless mode (no browser UI)
    chrome_options.add_argument(f"--window-size={resolution[0]},{resolution[1]}")

    # Set up ChromeDriver
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=chrome_options)

    # Open the HTML file
    driver.get("file://" + html_file_path)

    # Wait for the page to load
    time.sleep(2)  # Adjust time as needed

    # Take screenshot
    driver.save_screenshot(output_file_path)

    # Close the browser
    driver.quit()

if __name__ == "__main__":
    for menu in MENUS:
        take_screenshot(f"{DIR_PATH}/html/{menu}.html", f"output-menus/{menu}.png")
