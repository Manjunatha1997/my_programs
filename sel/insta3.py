import requests
from bs4 import BeautifulSoup as bs
import os


# username = input('Enter User name:')

url = 'https://www.instagram.com/majnu_manju/'

r = requests.get(url)
web_page = bs(r.content)

print(web_page)

filters = web_page.select('img')


print(filters)

# images = []
# for img in web_page.find_all('article'):
#     images.append(img.get('src'))
#
# print(images)


