import requests
from bs4 import BeautifulSoup as bs
import os

r = requests.get('https://www.google.com/search?channel=fs&sxsrf=ALeKk03OeUqZwyO3DIWR6lprvh8Cj7QyVg:1613659686040&source=univ&tbm=isch&q=burr+defects+on+steel&client=ubuntu&sa=X&ved=2ahUKEwj4l__i1vPuAhU77HMBHQskAtkQ7Al6BAgnEEw&biw=1322&bih=667')



web_page = bs(r.content)

print('please wait')
images = web_page.find_all('img')

print(images)
print(len(images))


