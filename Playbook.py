from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from chromedriver_py import binary_path
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
import time


service_object = Service(binary_path)
driver = webdriver.Chrome(service=service_object)
service = Service(executable_path="/Users/leapfrog/Documents/bin/chromedriver.exe")
driver = webdriver.Chrome(service=service)
# Input the link
url = "https://app.develop.nodalsolutions.com"
driver.maximize_window()
driver.get(url)
driver.find_element(By.ID, 'email').send_keys("anjeelatandukar+22aug@lftechnology.com")
driver.find_element(By.ID, 'password').send_keys("testing@1")
driver.find_element(By.XPATH, '//*[@id="root"]/div[1]/div/div[2]/div/form/div[3]/button').click()
driver.find_element(By.XPATH, '//*[@id="root"]/div[1]/nav/div/div/div[1]/ul/li[3]/a').click()

print(driver.title)
driver.find_element(By.XPATH, '//*[@id="root"]/div[1]/main/div/div[1]/a').click()
driver.find_element(By.XPATH, '//*[@id="playbookName"]').send_keys("Demo3")
driver.find_element(By.XPATH, '//*[@id="root"]/form/main/div/div[2]/div/button').click()

driver.find_element(By.XPATH, '//*[@id="np_00021"]').click()
wait = WebDriverWait(driver, 3)



#For decision point 1 to 46
def run_43_times() -> object:
    count = 0
    while True:
        buttons = driver.find_elements(By.XPATH, '//*[@class="btn btn--secondary ml-4x"]')

        print(len(buttons))

        for button in buttons:
            print("---------The number of buttons is : --------------")
        try:

            element = wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@class="btn btn--secondary ml-4x"]')))

            # if count == 47:
            #      print("I am at 45 now select the country")
            # else:
            if len(driver.find_elements(By.XPATH,
                                        '//*[@class="btn btn--secondary ml-4x"]')) > 0:  # pay attention: find_element*s*
                # driver.implicitly_wait(30)
                # time.sleep(1)
                driver.find_element(By.XPATH, '//*[@class="btn btn--secondary ml-4x"]').click()  # pay atten

            # element.click()
            time.sleep(2)
            if count == 53:
                print("I am at 45 now select the country")
                return
            count = count + 1

        # write code to select from the dropdown

        except TimeoutException as e:
            print(e)
            break
run_43_times()

#For dropdown state1(decision point 47)
driver.find_element(By.XPATH, '//*[@class="add__custom__text"]').click()
driver.find_element(By.XPATH, '//*[@class="stateDropdown searchDropdown__input-container css-ackcql"]')
driver.implicitly_wait(5)
# driver.implicitly_wait(5)
driver.find_element(By.XPATH, '//*[@class="stateDropdown searchDropdown__input"]').send_keys("Alaska")
driver.find_element(By.XPATH, '//*[@class="stateDropdown searchDropdown__input"]').send_keys(Keys.ENTER)
driver.find_element(By.XPATH,'//*[@class="btn btn--secondary modal__footer--undefined"]').click()
driver.find_element(By.XPATH,'//*[@id="root"]/main/div/aside/div[2]/div[3]/button[3]').click()
time.sleep(2)
#for normal decision point 48
driver.find_element(By.XPATH,'//*[@id="root"]/main/div/aside/div[2]/div[3]/button[3]').click()
time.sleep(5)
#For dropdown state2(decision point 49)
driver.find_element(By.XPATH,'//*[@class="add__custom__text"]').click()
driver.find_element(By.XPATH,'//*[@class="stateDropdown searchDropdown__input-container css-ackcql"]')

driver.implicitly_wait(5)
driver.find_element(By.ID, 'react-select-7-input').send_keys("Alaska")
driver.find_element(By.ID, 'react-select-7-input').send_keys(Keys.ENTER)
driver.find_element(By.XPATH,'//*[@class="btn btn--secondary modal__footer--undefined"]').click()
driver.find_element(By.XPATH,'//*[@id="root"]/main/div/aside/div[2]/div[3]/button[3]').click()
#for Remaining 6 decision point(50-55)
def run_08_times() -> object:
    count = 0
    while True:
        buttons = driver.find_elements(By.XPATH, '//*[@class="btn btn--secondary ml-4x"]')

        print(len(buttons))

        for button in buttons:
            print("---------The number of buttons is : --------------")
        try:

            element = wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@class="btn btn--secondary ml-4x"]')))

            if len(driver.find_elements(By.XPATH,
                                        '//*[@class="btn btn--secondary ml-4x"]')) > 0:  # pay attention: find_element*s*
                # driver.implicitly_wait(30)
                # time.sleep(1)
                driver.find_element(By.XPATH, '//*[@class="btn btn--secondary ml-4x"]').click()  # pay atten

            # element.click()
            time.sleep(2)
            if count == 7:
                print("I am at 7 now")
                return
            count = count + 1

        # write code to select from the dropdown

        except TimeoutException as e:
            print(e)
            break
run_08_times()
#button for not adding more playbook
driver.find_element(By.XPATH,'//*[@class="btn btn--outlined btn--outlined-secondary w-100"]').click()
#button for save playbook
driver.find_element(By.XPATH,'//*[@class="btn btn--secondary w-100 mb-4x"]').click()
# #button for approve playbook
# driver.find_element(By.XPATH,'//*[@class="btn btn--secondary w-100"]').click()
# #button for confirmation of approve playbook
driver.find_element(By.XPATH,'//*[@class="btn btn--secondary ml-4x"]').click()
time.sleep(2)
#To go back to playbook
driver.find_element(By.XPATH,'//*[@class="btn--outlined btn--outlined-secondary w-100 mb-8x"]').click()
