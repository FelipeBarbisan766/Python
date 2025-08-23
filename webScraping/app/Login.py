from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import csv
from selenium.webdriver.chrome.options import Options

options = Options()
options = webdriver.ChromeOptions()
driver = webdriver.Chrome(
    options=options,
)
driver.maximize_window()
url = "http://62.72.8.70/"
driver.get(url)

wait = WebDriverWait(driver, 5)

email_input = wait.until(EC.visibility_of_element_located((By.ID,'email')))
password_input = wait.until(EC.visibility_of_element_located((By.ID,'senha')))
submit_button = wait.until(EC.element_to_be_clickable((By.XPATH,'//*[@id="root"]/main/section[1]/form/div[5]/button')))

email_input.send_keys("felipe.barbisan@fatec.sp.gov.br")

password_input.send_keys("123456789")

submit_button.click()

input('Stoping')
# release the resources allocated by Selenium and shut down the browser
driver.quit()
