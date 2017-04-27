import requests
from bs4 import BeautifulSoup
import sys
from selenium import webdriver    #open webdriver for specific browser
from selenium.webdriver.common.keys import Keys   # for necessary browser action
from selenium.webdriver.common.by import By    # For selecting html code
import time
import os.path

def getQuotes(driver,quotes):
    quoteLinks=driver.find_elements_by_class_name("b-qt");
    for i in range(len(quoteLinks)):
        quote=quoteLinks[i].text
        # print quote
        quotes.append(quote)

def getFilename(nameStr):
    return "txt/"+nameStr.lower().replace(" ","_")+".txt"

def scrape(nameStr):
    if(os.path.exists(getFilename(nameStr))):
        print "File already exists"
    else:
        url="https://www.brainyquote.com/quotes/authors/"+getFilename(nameStr)[4]+"/"+getFilename(nameStr)[4:-4]+".html"
        driver = webdriver.Firefox()
        driver.get(url)

        for i in range(0,20):
        	driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        	time.sleep(1)

        quotes=[]
        getQuotes(driver,quotes)
        txtFile = open(getFilename(nameStr), 'w')
        for item in quotes:
          txtFile.write("%s\n" % item)

    return getFilename(nameStr)




# lines=[]
#
# for sentence in rickScripts:
#     sentence=sentence.replace('"','')
#     lines.append(sentence)
#
# print '\n'.join(markov.word_level_generate(lines, 3, count=8))
