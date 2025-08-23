from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import csv

# instantiate a Chrome options object
options = webdriver.ChromeOptions()
# set the options to use Chrome in headless mode
options.add_argument("--headless=new")

# initialize an instance of the chrome driver (browser) in headless mode
driver = webdriver.Chrome(
    options=options,
)

driver.maximize_window()


driver.get("https://www.scrapingcourse.com/ecommerce/product/chaz-kangeroo-hoodie/")

# wait up to 10 seconds until the document is fully ready
WebDriverWait(driver, 10).until(
    lambda driver: driver.execute_script("return document.readyState") == "complete"
)

# get the initial scroll height
last_height = driver.execute_script("return document.body.scrollHeight")

while True:
    # scroll to the bottom of the page
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")

    # wait for more elements to load after scrolling
    time.sleep(5)

    # get the new scroll height after scrolling
    new_height = driver.execute_script("return document.body.scrollHeight")

    # check if new content has loaded
    if new_height == last_height:
        # if no new content is loaded, break the loop
        break

    # update the last height
    last_height = new_height

# extract all the product containers
products = driver.find_elements(By.CSS_SELECTOR, ".product")

# get the element using the ID selector
summary_element = driver.find_element(By.CSS_SELECTOR, "#tab-description")

# screenshot the selected element
summary_element.screenshot("specific_screenshot.png")

# screenshot the visible part of the page
driver.save_screenshot("screenshot.png")

# declare an empty list to collect the extracted data
extracted_products = []

# loop through the product containers
for product in products:

    # extract the elements into a dictionary using the CSS selector
    product_data = {
        "name": product.find_element(By.CSS_SELECTOR, ".product-name").text,
        "price": product.find_element(By.CSS_SELECTOR, ".price").text,
        # "URL": product.find_element(
        #     By.CSS_SELECTOR, ".woocommerce-LoopProduct-link"
        # ).get_attribute("href"),
        # "image": product.find_element(By.CSS_SELECTOR, ".product-image").get_attribute(
        #     "src"
        # ),
    }

    # append the extracted data to the extracted_product list
    extracted_products.append(product_data)

# print the extracted data
print(extracted_products)

# # specify the CSV file name
# csv_file = "products.csv"

# # write the extracted data to the CSV file
# with open(csv_file, mode="w", newline="", encoding="utf-8") as file:
#     # write the headers
#     writer = csv.DictWriter(file, fieldnames=["Url", "Image", "Name", "Price"])
#     writer.writeheader()
#     # write the rows
#     writer.writerows(extracted_products)

# # confirm that the data has been written to the CSV file
# print(f"Data has been written to {csv_file}")

# release the resources allocated by Selenium and shut down the browser
driver.quit()
