from selenium import webdriver
import os
import requests
import time


username = input('enter insta username:')

if not os.path.isdir(username):
    os.mkdir(username)

driver = webdriver.Firefox(executable_path='./geckodriver')
url = 'https://www.instagram.com/'+username

driver.get(url)

# divs = driver.find_elements_by_xpath('/html/body/div[1]/section/main/div/div[2]/article/div/div/div[1]/div[1]/a/div/div[1]')

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



divs = driver.find_elements_by_class_name('FFVAD')
# divs = driver.find_elements_by_xpath('/html/body/div[1]/section/main/div/div[2]/article/div/div/div[1]/div[1]/a/div/div[1]/')


count = 0

for i in divs:
    print(i.get_attribute('src'))
    image_src = i.get_attribute('src')
    image_data = requests.get(image_src).content

    fw = open(username + '/' + str(count) + '.jpg', 'wb')
    fw.write(image_data)
    fw.close()
    count += 1


print(len(divs))
