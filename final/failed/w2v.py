import quoteScraper
from __future__ import unicode_literals
import spacy

nlp = spacy.load('en')
doc = nlp(open(quoteScraper.scrape("Donald Trump")).read().decode('utf8'))

def sentvec(s):
    sent = nlp(s)
    return meanv([w.vector for w in sent])


sentences = list(doc.sents)

def spacy_closest_sent(space, input_str, n=10):
    input_vec = sentvec(input_str)
    return sorted(space,
                  key=lambda x: cosine(np.mean([w.vector for w in x], axis=0), input_vec),
                  reverse=True)[:n]

for sent in spacy_closest_sent(sentences, "My favorite food is strawberry ice cream."):
    print sent.text
    print "---"
