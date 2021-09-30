# -*- coding: utf-8 -*-
from bs4 import BeautifulSoup
import requests
#For names:
import nltk
import os
#nltk.download('popular')
from nltk.tag.stanford import StanfordNERTagger
#-----------------------------------------------------------------------

headers = {'User-Agent':'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_2) AppleWebKit/601.3.9 (KHTML, like Gecko) Version/9.0.2 Safari/601.3.9'}
url='https://www.nytimes.com/'
response=requests.get(url,headers=headers)

soup=BeautifulSoup(response.content,'lxml')

headlines = []

for item in soup.select('.story-wrapper'):
	try:
		headline = item.find('h3').get_text()
		headlines.append(headline)
	except Exception as e:
		#raise e
		print('')

for headline in headlines:
    print(headline)

#Identify names:
names = []

st = StanfordNERTagger(r'C:\Users\bendi\AppData\Roaming\nltk_data\stanford-ner-2020-11-17\classifiers\english.all.3class.distsim.prop',
           r'C:\Users\bendi\AppData\Roaming\nltk_data\stanford-ner-2020-11-17.jar')

for i in headlines:
    text = headlines[i]
    
    for sent in nltk.sent_tokenize(text):
        tokens = nltk.tokenize.word_tokenize(sent)
        tags = st.tag(tokens)
        for tag in tags:
            if tag[1]=='PERSON': names.append(tag)

print(names)

