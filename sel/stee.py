from selenium import webdriver
from selenium.webdriver.common import keys

import requests
from bs4 import BeautifulSoup as bs

import time
import os


search_input = input('Type defect here:')
output_path_directory = input('Crete a folder:')
output_path_directory = os.getcwd()+'/'+output_path_directory

if not os.path.isdir(output_path_directory):
    os.mkdir(output_path_directory)


driver = webdriver.Firefox(executable_path='./geckodriver')

driver.maximize_window()


url = 'https://www.google.com/search?q='+search_input

driver.get(url)
driver.find_element_by_xpath("//a[contains(text(),'Images')]").click()


# driver.execute_script("window.scrollTo(0,document.body.scrollHeight);")
def  scroll_to_end():
    lenOfPage = driver.execute_script("window.scrollTo(0, document.body.scrollHeight);var lenOfPage=document.body.scrollHeight;return lenOfPage;")
    match=False
    while(match==False):
        lastCount = lenOfPage
        time.sleep(3)
        lenOfPage = driver.execute_script("window.scrollTo(0, document.body.scrollHeight);var lenOfPage=document.body.scrollHeight;return lenOfPage;")
        if lastCount==lenOfPage:
            match=True


scroll_to_end()


all = driver.find_elements_by_xpath("//img")

print(all)
print(len(all))

count = 0


for i in all:
    src = i.get_attribute('src')
    print(src)
    if not src == None:
        if src.startswith('http'):
            image_data = requests.get(src).content
            print(image_data)
            print(type(image_data),image_data[0:5])
            fw = open(output_path_directory + '/' + str(count) + '.jpg', 'wb')
            fw.write(image_data)
            fw.close()
                

        count += 1
        print(count)



