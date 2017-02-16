import time
import requests
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

base_url='http://hellopoetry.com/words/33964/thursday/poems/'
# driver = webdriver.Firefox()
# driver.get(base_url)
# elm=driver.find_element_by_tag_name('html')
# elm.send_keys(Keys.END)
# driver.execute_script("window.scrollTo(0, Y)")

searchstr="thursday"

def get_poems(url,num=0):
    html=requests.get(url).text
    soup=BeautifulSoup(html,'html.parser')
    # thursdays=soup.find_all('p')
    poem=soup.select('p')[num].text
    print num,"\t"
    # print poem.split('.')
    if "." in poem:
        for line in poem.split('.'):
            if "thursday" in line:
                print line
                continue
            if "Thursday" in line:
                print line
                continue



for num in range(0,16):
    get_poems(base_url,num)
    time.sleep(0.8)

driver.quit()
