import re
import requests
from bs4 import BeautifulSoup as bs

site = 'https://www.instagram.com/majnu_manju/'

r = requests.get(site)

web_page = bs(r.content)

print(web_page)





