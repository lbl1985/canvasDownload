from selenium import webdriver
from selenium.webdriver.common.by import By
from getpass import getpass
import time
import re

TARGET_LINK = "https://www.coursera.org/learn/risk-management-empathy-data/home/week/4"

driver = webdriver.Edge()
driver.get("https://www.coursera.org/?authMode=login")

driver.implicitly_wait(2)

user_name = driver.find_element(By.ID, "email")
pass_word = driver.find_element(By.ID, "password")

user_name.send_keys("herbert19lee@gmail.com")
pass_word.send_keys("OCamps@2013")

login_button = driver.find_element(By.XPATH, "//button[@type='submit']")
login_button.click()

driver.implicitly_wait(2)
getpass("wait for operations")

try:
    one_time_password = driver.find_element(By.ID, "one-time-password")    
    one_time_password.send_keys(getpass("Enter your OTP: "))
    login_button.click()
except:
    pass

TARGET_LINK = "https://www.coursera.org/learn/risk-management-empathy-data/home/week/1"

# Extract the root webpage address
match = re.search(r'https://www\..+?/', TARGET_LINK)
if match is not None:
    root_webpage_address = match.group(0)
    print(f"Root webpage address: {root_webpage_address}")
else:
    print("No root webpage address found in TARGET_LINK")
    
driver.get(TARGET_LINK)
getpass("wait for operations")

lesson_sessions = driver.find_elements(By.CLASS_NAME, 'rc-ModuleLessons')
lesson_sessions = [session for session in lesson_sessions if not session.text.startswith("About the Course")]

if len(lesson_sessions) > 0:
    for session in lesson_sessions:
        elements = session.find_elements(By.TAG_NAME, 'a')
        
        href = [element.get_attribute('href') for element in elements]
        href = [link for link in href if 'quiz' not in link]

        print(href)

        for link in href:
            driver.get(root_webpage_address[:-1] + link)
            time.sleep(2)
            getpass("wait for operations")

driver.se