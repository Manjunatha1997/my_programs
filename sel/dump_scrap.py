



from selenium import webdriver
import os
import requests
import time


# access chrome driver
driver = webdriver.Chrome(executable_path='./chromedriver')
driver.maximize_window()

# url = 'https://www.carerisksolutions.com/file-share'
# url = 'https://icraanalytics.com/Home/MldValuation#!#divMlddDetails'
url = 'https://www.crisil.com/'


driver.get(url)

driver.find_element_by_xpath('/html/body/header/div[4]/div/div[2]/div/div[2]/div/input').send_keys('Aditya Birla Finance Limited')

time.sleep(10)

