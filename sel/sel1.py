from selenium import webdriver
from selenium.webdriver.common import keys

driver = webdriver.Firefox(executable_path='./geckodriver')


result = []


for htno in range(2317290,2317293):

    try:
        student = {}
        driver.get('http://www.results.manabadi.co.in/2020/sri-venkateswara-university-mca-5th-sem-dec-2019-exam-results-09022021.htm')
        driver.find_element_by_name('htno').send_keys(str(htno))
        driver.find_element_by_name('btnsubmit').click()
        res = driver.find_element_by_xpath('/html[1]/body[1]/div[1]/table[1]/tbody[1]/tr[1]/td[3]/table[2]/tbody[1]/tr[1]/td[1]/div[1]/div[1]/div[1]/table[1]/tbody[1]/tr[4]/td[2]')


        HTNO = driver.find_element_by_xpath('/html[1]/body[1]/div[1]/table[1]/tbody[1]/tr[1]/td[3]/table[2]/tbody[1]/tr[1]/td[1]/div[1]/div[1]/div[1]/table[1]/tbody[1]/tr[2]/td[1]/b[1]')
        r = driver.find_element_by_xpath('/html[1]/body[1]/div[1]/table[1]/tbody[1]/tr[1]/td[3]/table[2]/tbody[1]/tr[1]/td[1]/div[1]/div[1]/div[1]/table[1]/tbody[1]/tr[2]/td[2]')
        student['HTNO'] = r.text

        NAME = driver.find_element_by_xpath('/html[1]/body[1]/div[1]/table[1]/tbody[1]/tr[1]/td[3]/table[2]/tbody[1]/tr[1]/td[1]/div[1]/div[1]/div[1]/table[1]/tbody[1]/tr[3]/td[1]/b[1]')
        r = driver.find_element_by_xpath('/html[1]/body[1]/div[1]/table[1]/tbody[1]/tr[1]/td[3]/table[2]/tbody[1]/tr[1]/td[1]/div[1]/div[1]/div[1]/table[1]/tbody[1]/tr[3]/td[2]')
        student[NAME.text] = r.text

        GSGPA = driver.find_element_by_xpath('/html[1]/body[1]/div[1]/table[1]/tbody[1]/tr[1]/td[3]/table[2]/tbody[1]/tr[1]/td[1]/div[1]/div[1]/div[1]/table[1]/tbody[1]/tr[4]/td[1]/b[1]')
        r = driver.find_element_by_xpath('/html[1]/body[1]/div[1]/table[1]/tbody[1]/tr[1]/td[3]/table[2]/tbody[1]/tr[1]/td[1]/div[1]/div[1]/div[1]/table[1]/tbody[1]/tr[4]/td[2]')
        student[GSGPA.text] = r.text

        result.append(student)

        print('****************** student result ****************')
        print(student)

    except:
         print('skipping...',htno)

