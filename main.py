from time import sleep
from cred import username, password
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options

chr_options = Options()
chr_options.add_experimental_option("detach", True)
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=chr_options)
driver.get("https://www.netflix.com/login")
sleep(1)
driver.find_element(By.XPATH, "/html/body/div[1]/div/div[3]/div/div/div[1]/form/div[1]/div[1]/div/label/input").send_keys(username)
sleep(1)
driver.find_element(By.XPATH, "/html/body/div[1]/div/div[3]/div/div/div[1]/form/div[2]/div[1]/div/label/input").send_keys(password)
sleep(1)
driver.find_element(By.CLASS_NAME, "btn").click()
