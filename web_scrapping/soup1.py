import requests
from bs4 import BeautifulSoup as bs
import os

url = 'https://www.cottonworks.com/resources/defects-glossary/'
output_directory = '/home/manju/fabrics/'
r = requests.get(url)
web_page = bs(r.content)


divs = web_page.find_all('div', attrs={'class':'defect-thumb'})


folders = [i.ul.li.text for i in divs]

print(folders)
print(len(folders))
print(len(set(folders)))


# def get_image_link():
#     div_tags = web_page.find_all('div',attrs={'class':'defect-thumb'})
#     for i in div_tags:
#         image_link = i.a.img['src']
#         return image_link
#
# links = get_image_link()
# print(links)
# exit()

for folder in folders:
    if os.path.isdir(output_directory+folder):
        div_tags = web_page.find_all('div', attrs={'class': 'defect-thumb'})
        for i in div_tags:
            image_link = i.a.img['src']
            image_content = requests.get(image_link).content
            print('creating in if')
            fw = open(output_directory+folder+'/'+'image.jpg','wb')
            fw.write(image_content)
            fw.close()
    else:
        os.mkdir(output_directory+folder)
        div_tags = web_page.find_all('div', attrs={'class': 'defect-thumb'})
        for i in div_tags:
            image_link = i.a.img['src']
            image_content = requests.get(image_link).content
            print('crating in else')
            fw = open(output_directory + folder+'/'+'image.jpg', 'wb')
            fw.write(image_content)
            fw.close()
