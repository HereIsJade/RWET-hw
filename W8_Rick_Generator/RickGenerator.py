import requests
from bs4 import BeautifulSoup
import sys
import markov

links=[]
rickScripts=[]
searchUrl="http://rickandmorty.wikia.com/wiki/Special:Search?search=transcript"
def getLinks(pageNum):
    url=searchUrl+"&page="+str(pageNum)
    html=requests.get(url).text
    soup=BeautifulSoup(html,'html.parser')
    anchors = soup.find_all('a', {'class': 'result-link', 'href': True})
    for anchor in anchors:
        if '/Transcript' in anchor['href']:
            link=anchor['href']
            if link not in links:
                links.append(link)


def get_total_pages(url):
    html=requests.get(url).text
    soup=BeautifulSoup(html,'html.parser')
    total_pages=soup.select('.paginator-page')[-1].text
    total_pages=int(total_pages)
    return total_pages


def getTranscripts(url):
    html=requests.get(url).text
    soup=BeautifulSoup(html,'html.parser')
    div=soup.findAll('div',attrs={"id":"mw-content-text"})
    for tag in div:
        pTags = tag.find_all("p")
    for p in pTags:
        if 'Rick:' in p.text:
            #get rid of "Rick: " and "\n"
            rickScripts.append(p.text[6:].strip())

for num in range(1,get_total_pages(searchUrl)+1):
    getLinks(num)

for num in range(len(links)):
    getTranscripts(links[num])

# Rough scripts list. Each entry contains multiple sentences, need further "split by period" manipulations
# lines=[]
# for script in rickScripts:

print len(rickScripts)


lines=[]

for sentence in rickScripts:
    sentence=sentence.replace('"','')
    lines.append(sentence)

print '\n'.join(markov.word_level_generate(lines, 3, count=8))
