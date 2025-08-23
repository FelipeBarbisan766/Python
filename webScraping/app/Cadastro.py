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
url = "http://62.72.8.70/registro"
driver.get(url)

wait = WebDriverWait(driver, 8)

name_input = wait.until(EC.visibility_of_element_located((By.ID,'name')))
email_input = wait.until(EC.visibility_of_element_located((By.ID,'email')))
password_input = wait.until(EC.visibility_of_element_located((By.ID,'senha')))
submit_button = wait.until(EC.element_to_be_clickable((By.XPATH,'//*[@id="root"]/main/section[1]/form/div[6]/button')))

name_input.send_keys("Felipe Adrian Lourenco Barbisan")

email_input.send_keys("felipe.barbisan@fatec.sp.gov.br")

password_input.send_keys("123456789")

submit_button.click()

input('Stoping')
# release the resources allocated by Selenium and shut down the browser
driver.quit()
 