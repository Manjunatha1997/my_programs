import requests
from selenium import  webdriver
from bs4 import BeautifulSoup as bs
import time
import os


username = input('enter insta username:')

url = 'https://www.instagram.com/'+username

driver = webdriver.Firefox(executable_path='./geckodriver')

driver.get(url)
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
time.sleep(2)
print(driver.page_source)
web_page = bs(driver.page_source,'html.parser')

print(web_page)

img = web_page.find_all('img')
print(len(img))

# if not os.path.isdir(username):
#     os.mkdir(username)
#
# count = 0
# for image in img:
#     count += 1
#     image_data = image['src']
#     print(image_data)
#     data = requests.get(image_data).content
#     try:
#         fw = open(username+'/'+str(count)+'.jpg','wb')
#         fw.write(data)
#         fw.close()
#     except:
#         print(image_data,'********************')

