import quoteScraper
import random
from textblob import TextBlob
import markov

lines=""

name="Taylor swift"
quoteFile = open(quoteScraper.scrape(name),"r")
texts = quoteFile.read()

blob = TextBlob(texts)

sentences=blob.sentences
for sentence in sentences:
    sentence=str(sentence)
    lines+=sentence
print lines

#
print '*****'.join(markov.word_level_generate(lines, 4, count=8))
