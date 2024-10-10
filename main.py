from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
import time

chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)
print("Automatic Job Application via LinkedIn")
user_email = input("Enter your LinkedIn Email Address : ")
user_password = input("Enter your LinkedIn Password : ")
driver = webdriver.Chrome(options=chrome_options)
driver.get(
    "https://www.linkedin.com/jobs/search/?f_LF=f_AL&geoId=102257491"
    "&keywords=python%20developer"
    "&location=United%20States&geoId=103644278"
    "&redirect=false&position=1&pageNum=0"
)
# Explicit wait for email input
time.sleep(2)
try:
    sign_in = driver.find_element(By.XPATH, '/html/body/div[1]/header/nav/div/a[2]')
    sign_in.click()

    email = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH, "/html/body/div/main/div[2]/div[1]/form/div[1]/input"))
    )
    email.send_keys(user_email)

    password = driver.find_element(By.XPATH, '//*[@id="password"]')
    password.send_keys(user_password)

    login = driver.find_element(By.XPATH, "/html/body/div/main/div[2]/div[1]/form/div[3]/button")
    login.click()
    time.sleep(1)
    chat_down = driver.find_element(By.XPATH, "/html/body/div[5]/div[4]/aside[1]/div[1]/header/div[3]/button[2]")
    chat_down.click()

    easy_apply = driver.find_element(By.XPATH, "/html/body/div[5]/div[3]/div[4]/div/div/main/div/div[2]/div[2]/div/div[2]/div/div[1]/div/div[1]/div/div[1]/div[1]/div[6]/div/div/div/button")
    easy_apply.click()
    time.sleep(1)
    next_button = driver.find_element(By.XPATH, "/html/body/div[3]/div/div/div[2]/div/div[2]/form/footer/div[2]/button")
    next_button.click()

    review_button = driver.find_element(By.XPATH, "/html/body/div[3]/div/div/div[2]/div/div[2]/form/footer/div[2]/button[2]")
    review_button.click()

except:
    sign_in = driver.find_element(By.XPATH, '/html/body/nav/div/a[2]')
    sign_in.click()
    email = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH, "/html/body/div/main/div[2]/div[1]/form/div[1]/input"))
    )
    email.send_keys(user_email)

    password = driver.find_element(By.XPATH, '//*[@id="password"]')
    password.send_keys(user_password)

    login = driver.find_element(By.XPATH, "/html/body/div/main/div[2]/div[1]/form/div[3]/button")
    login.click()
    time.sleep(6)
    chat_down = driver.find_element(By.XPATH, "/html/body/div[5]/div[4]/aside[1]/div[1]/header/div[3]/button[2]")
    chat_down.click()

    jobs = driver.find_element(By.XPATH, "/html/body/div[5]/header/div/nav/ul/li[3]/a")
    jobs.click()
    time.sleep(3)

    search = driver.find_element(By.XPATH, "/html/body/div[5]/header/div/div/div/div[2]/div[2]/div/div/input[1]")
    search.send_keys("Python Developer")

    location = driver.find_element(By.XPATH, "/html/body/div[5]/header/div/div/div/div[2]/div[3]/div/div/input[2]")
    location.send_keys("United States")
    search.send_keys(Keys.ENTER)
    time.sleep(5)

    easy_apply_f = driver.find_element(By.XPATH, "/html/body/div[5]/div[3]/div[4]/section/div/section/div/div/div/ul/li[8]/div/button")
    easy_apply_f.click()

    easy_apply = driver.find_element(By.XPATH, "/html/body/div[5]/div[3]/div[4]/div/div/main/div/div[2]/div[2]/div/div[2]/div/div[1]/div/div[1]/div/div[1]/div[1]/div[6]/div/div/div/button")
    easy_apply.click()
    time.sleep(1.01)
    next_button = driver.find_element(By.XPATH, "/html/body/div[3]/div/div/div[2]/div/div[2]/form/footer/div[2]/button")
    next_button.click()

    review_button = driver.find_element(By.XPATH, "/html/body/div[3]/div/div/div[2]/div/div[2]/form/footer/div[2]/button[2]")
    review_button.click()
