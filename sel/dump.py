from selenium import webdriver
import os
import requests
import time


# access chrome driver
driver = webdriver.Chrome(executable_path='./chromedriver')
driver.maximize_window()

# url = 'https://www.carerisksolutions.com/file-share'
url = 'https://icraanalytics.com/Home/MldValuation#!#divMlddDetails'


driver.get(url)

time.sleep(10)

# scroll down until reach the xpath
# driver.execute_script("window.scrollTo(0, window.scrollY + 1000)")

company_name = 'Aditya Birla Finance Limited'


driver.find_element_by_xpath('/html/body/div[1]/section[2]/div/div[1]/div/form/div/div/div[1]/div[1]/div/md-autocomplete/md-autocomplete-wrap/input').send_keys(company_name)

time.sleep(5)


driver.find_element_by_xpath('/html/body/md-virtual-repeat-container/div/div[2]/ul/li/md-autocomplete-parent-scope/span').click()

time.sleep(5)

driver.find_element_by_id('btnSearch').click()

time.sleep(10)
driver.find_element_by_xpath('//*[@id="divMlddDetails"]/div/div/table/tbody/tr[1]/td[3]/a').click()
time.sleep(10)



