from __future__ import unicode_literals
import spacy
import quoteScraper
# from textblob import TextBlob
import random

nlp = spacy.load('en')
wordDict={'verbs':[],'nouns':[],'adjs':[],'advs':[],'prons':[]}

def getName(name):
    quoteFile = open(quoteScraper.scrape(name),"r")
    texts = quoteFile.read()

    doc = nlp(texts.decode('utf8'))
    sentences_as_list = list(doc.sents)
    # print len(sentences_as_list)

    for item in doc:
        if item.tag_ == 'NN':
            wordDict['nouns'].append(item.text)
        elif item.pos_ == 'VERB':
            wordDict['verbs'].append(item.lemma_)
        elif item.pos_ == 'ADJ':
            wordDict['adjs'].append(item.text)
        elif item.tag_ == 'RB':
            wordDict['advs'].append(item.text)
        elif item.pos_ == 'PRON':
            wordDict['prons'].append(item.text)

def getQA(name):
    getName(name)
    questions=[]
    answers=[]
    for i in range(10):
        question_list=[random.choice(wordDict['adjs']),random.choice(wordDict['nouns']),random.choice(wordDict['verbs']),random.choice(wordDict['advs']),random.choice(wordDict['adjs']),random.choice(wordDict['prons']),random.choice(wordDict['verbs']),random.choice(wordDict['advs'])]

        question=" ".join(question_list)

        answer_list=[random.choice(wordDict['adjs']),random.choice(wordDict['nouns']),random.choice(wordDict['verbs']),random.choice(wordDict['adjs']),random.choice(wordDict['nouns'])]


        answer=" ".join(answer_list)
        answer=answer[0].upper()+answer[1:]+'.'
        # answer = TextBlob(answer).correct()

        question="What if "+question+"?"
        # question=TextBlob(question).correct()

        questions.append(question)
        answers.append(answer)
    return questions, answers
    # print answer

# b = TextBlob(generated)
# print b.correct()
