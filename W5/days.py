# from selenium import webdriver
# from selenium.webdriver.common.keys import Keys
import requests
from bs4 import BeautifulSoup
import pronouncing as pr
import random

# chromedriver = "/Users/Jade/Desktop/python/Detourning in-class/chromedriver"
# os.environ["webdriver.chrome.driver"] = chromedriver
# driver = webdriver.Chrome(chromedriver)
monday=[]
tuesday=[]
wednesday=[]
thursday=[]
friday=[]
saturday=[]
sunday=[]
def searchByDay(day,dlist):
    search_item=day
    url='http://sentence.yourdictionary.com/'+search_item
    html=requests.get(url).text
    soup=BeautifulSoup(html,'html.parser')
    sentences=soup.select('.li_content')
    for sentence in sentences:
        for part in sentence.text.split(','):
            if day in part:
                dlist.append(part)
    return dlist

def searchByPr(word):
    plist=pr.rhymes(word)
    return random.choice(plist)

searchByDay('Monday',monday)
searchByDay('Thursday',thursday)
searchByDay('Saturday',saturday)
searchByDay('Sunday',sunday)
# grey=pr.rhymes("grey")
# # print grey
# love=pr.rhymes('love')
# print love

f = open("test.txt","w")
f.write(random.choice(monday)+"\n")
f.write("Tuesday's "+searchByPr('grey')+" and Wednesday too\n")
f.write(random.choice(thursday)+"\n")
f.write("It's Friday, I'm "+searchByPr('love')+"\n\n")

f.write(random.choice(monday)+"\n")
f.write("Tuesday Wednesday break my "+searchByPr('heart')+"\n")
f.write(random.choice(thursday)+"\n")
f.write("It's Friday, I'm "+searchByPr('art')+"\n\n")

f.write(random.choice(saturday)+"\n")
f.write(random.choice(sunday)+"\n")
f.write("But Friday, Never "+searchByPr('tate')+"\n\n")
