from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By 
import time

USERNAME = ""
PASSWORD = ""
PASSWORD2 = ""


PATH = ""
driver = webdriver.Chrome()

url = ""
driver.get(url)

def login():
    time.sleep(2)
    username_box = driver.find_element(By.ID, "username")
    password_box = driver.find_element(By.ID, "password")
    username_box.send_keys(USERNAME)
    password_box.send_keys(PASSWORD)
    password_box.send_keys(Keys.RETURN)
    time.sleep(3)
    try: 
        driver.find_element(By.CLASS_NAME, "")
        return False
    except:
        return True
      
    

def expanding_page():
    print("Inside expanding_page function")
    time.sleep(5)
    driver.find_element(By.XPATH, "").click()
    time.sleep(2)
    driver.find_element(By.XPATH, "").click()

def next_page(): 
    try: 
        driver.find_element(By.XPATH, "").click()
        return True 
    except: 
        return False


def ce_info():
    time.sleep(5)
    next_page_ = True
    while next_page_: 
        table_0 = driver.find_elements(By.CLASS_NAME, "")
        print(len(table_0))
        time.sleep(5)
        for elem in table_0:
            elem.click()
            time.sleep(3)
            section = driver.find_element(By.ID,"")
            rows = section.find_elements(By.CLASS_NAME, "")
            info = dict()
            course_title = elem.find_element(By.TAG_NAME, "").text
            completed_date = elem.find_element(By.TAG_NAME,"").text
            hours = elem.find_element(By.CLASS_NAME,"").text
            info["course_title"] = course_title
            info["completed_date"] = completed_date
            info["hours"] = hours
            for row in rows:
                entry = row.find_elements(By.CLASS_NAME, "")
                info[entry[0].text] = entry[1].text
            print(info, "\n")
        next_page_ = next_page()
    time.sleep(5)

def uploadingCE_stateOhio():
    date_completed = "10/12/2023"
    ethics = "5"
    supervision_training = "5"
    continuing_education = "5"

    driver.find_element(By.XPATH, "").click()
    time.sleep(4)
    driver.find_element(By.XPATH, "").click()
    
    date = driver.find_element(By.NAME, "")
    date.send_keys(date_completed) 
    date.send_keys(Keys.RETURN)
    
    driver.find_element(By.XPATH, "").click()
    time.sleep(1)
    ethics_field = driver.find_element(By.ID, "")
    print(ethics_field)
    ethics_field.send_keys(ethics) 
    driver.find_element(By.XPATH, "").click()
    time.sleep(1)
    super_training_field = driver.find_element(By.NAME, "") 
    super_training_field.send_keys(supervision_training)
    driver.find_element(By.XPATH, "").click()
    time.sleep(1)
    ce_field = driver.find_element(By.NAME, "") 
    ce_field.send_keys(continuing_education)
    driver.find_element(By.ID, "").click() #continue


print(login())
#expanding_page()
ce_info()
#time.sleep(5)
#uploadingCE_stateOhio() 
#time.sleep(5)

driver.close() 
driver.quit()