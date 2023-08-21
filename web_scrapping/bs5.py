import requests
from bs4 import BeautifulSoup as bs
import os

r = requests.get('https://www.cottonworks.com/resources/defects-glossary/')
web_page = bs(r.content)

output_path_directory = './testing1/'


filters = web_page.select('form#fabric-type select option')
filters = filters[1:]
filter_types = [filt['value'] for filt in filters]
print(filter_types)

root_url = 'https://www.cottonworks.com/resources/defects-glossary/'

for lnk in filter_types:

    print(lnk)
    lnk = lnk.replace(" ","+")
    print(lnk)
    link = root_url+'?fabtype='+lnk
    print(link)

    print(output_path_directory+lnk.replace('+',''))
    if not os.path.isdir(output_path_directory+lnk.replace('+','')):
        os.mkdir(output_path_directory+lnk.replace('+',''))
    print('**************************************************************************')


    r = requests.get(link)
    web_page = bs(r.content)

    divs = web_page.find_all('div', attrs={'class': 'defect-thumb'})

    count = 0
    img_count = 0

    for i in divs:

        defect_name = web_page.select('div.defect-thumb ul li span')[count].string
        image_url = web_page.select('div.defect-thumb a img')[img_count]
        image_url = image_url['src']
        image_data = requests.get(image_url).content

        print(output_path_directory+lnk+'/'+defect_name)

        sub_folder = output_path_directory+lnk.replace('+','')+'/'+defect_name


        if os.path.isdir(sub_folder):
            # os.mkdir(output_path_directory+lnk+defect_name+str(img_count))
            fw = open(sub_folder+'/'+str(img_count)+'image.jpg','wb')
            fw.write(image_data)
            fw.close()

        else:
            os.mkdir(sub_folder)
            fw = open(sub_folder + '/'+str(img_count)+'image.jpg','wb')
            fw.write(image_data)
            fw.close()

        count += 3
        img_count += 1
