import urllib
import json
import sys
import random

keywords=['and',       'del',       'from',      'not',       'while',
'as',        'elif',      'global',    'or',        'with',
'assert',    'else',     'if',       'pass',      'yield',
'break',     'except',   'import',    'print',
'class',     'exec',      'in',        'raise',
'continue',  'finally',   'is',        'return',
'def',       'for',       'lambda',    'try']


# print keywords
kWordsTxt = set()

for line in sys.stdin:
    line = line.strip()
    words = line.split(" ")
    for word in words:
        if word in keywords:
            kWordsTxt.add(word)

print kWordsTxt

api_key = "a2a73e7b926c924fad7001ca3111acd55af2ffabf50eb4ae5"

for kWord in kWordsTxt:
    # print kWord
    url = "http://api.wordnik.com:80/v4/word.json/"+kWord+"/examples?includeDuplicates=false&useCanonical=false&skip=0&limit=5&api_key="+api_key
    doc_str = urllib.urlopen(url).read()
    doc_data = json.loads(doc_str)
    examples=doc_data['examples']
    rand_example=random.choice(examples)['text']
    print '**'+kWord+"** "+rand_example
