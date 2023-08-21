
from bs4 import BeautifulSoup
import requests


url = 'https://www.geeksforgeeks.org/python-programming-examples/'

r = requests.get(url)

web_page = BeautifulSoup(r.content,features="lxml") 

all = web_page.find_all('h2')

for i in all:
	if i.next_element['name'] == 'regex' or i.next_element['name'] == 'file':
		# print(i.findNext('ol'))
		res = i.findNext('ol').find_all('a')
		for a in res:
			print(a['href'])
			fa = open('ddddddddddd.txt','a')
			fa.write(a['href']+'\n')
			fa.close()
		print('**************************************************')
	else:
		name = i.next_element['name']
		res = web_page.find_all('div', attrs={'class':name})
		for cnt in res:
			anc = cnt.find_all('a')
			for a in anc:
				print(a['href'])
				
				fa = open('ddddddddddd.txt','a')
				fa.write(a['href']+'\n')
				fa.close()
			print('*****************************')





