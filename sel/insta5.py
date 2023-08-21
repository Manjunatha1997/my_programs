from selenium import webdriver
import os
import requests
import time
# import System

username = input('enter insta username:')


if not os.path.isdir(username):
    os.mkdir(username)

# System.setProperty("webdriver.gecko.driver","C:\Users\Manju\Downloads\geckodriver-v0.31.0-win64.exe")


# driver = webdriver.Chrome(executable_path=r'D:\python_programs\sel\chromedriver.exe')
driver = webdriver.Firefox(executable_path=r"C:\Users\Manju\Downloads\geckodriver-v0.31.0-win64\geckodriver.exe")

url = 'https://www.instagram.com/'+username

print(url)

driver.get(url)

count = 0

res = []

def  scroll_to_end():
    lenOfPage = driver.execute_script("window.scrollTo(0, document.body.scrollHeight);var lenOfPage=document.body.scrollHeight;return lenOfPage;")
    match=False
    while(match==False):
        lastCount = lenOfPage
        time.sleep(1)
        res.extend(driver.find_elements_by_class_name('FFVAD'))

        lenOfPage = driver.execute_script("window.scrollTo(0, document.body.scrollHeight);var lenOfPage=document.body.scrollHeight;return lenOfPage;")
        if lastCount==lenOfPage:
            match=True


scroll_to_end()

# res = driver.find_elements_by_class_name('FFVAD')

print(len(res))
for i in res:
    print(i)



res = driver.find_elements_by_tag_name('img')

while True:
    count += 1
    div = driver.find_element_by_class_name('FFVAD')
    image_src = div.get_attribute('src')
    image_data = requests.get(image_src).content

    fw = open(username + '/' + str(count) + '.jpg', 'wb')
    fw.write(image_data)
    fw.close()
    driver.execute_script("window.scrollTo(0, 1000);")
    time.sleep(1)
    driver.execute_script("window.scrollBy(0,2000)", "")
    time.sleep(4)




# for i in divs:
#     print(i.get_attribute('src'))
#     image_src = i.get_attribute('src')
#     image_data = requests.get(image_src).content

#     fw = open(username + '/' + str(count) + '.jpg', 'wb')
#     fw.write(image_data)
#     fw.close()
#     count += 1

#
# print(len(divs))
