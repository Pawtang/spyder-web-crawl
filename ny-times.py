# -*- coding: utf-8 -*-
from bs4 import BeautifulSoup
import requests
#For names:
import nltk
import os
nltk.download('popular')
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

print(headlines)

#Identify names:
names = []

st = StanfordNERTagger('/Users/mahendrabilagi/Desktop/stanford-ner-2017-06-09/classifiers/english.all.3class.distsim.crf.ser.gz',
           '/Users/mahendrabilagi/Desktop/stanford-ner-2017-06-09/stanford-ner.jar')

for i in headlines:
    text = headlines[i]
    
    for sent in nltk.sent_tokenize(text):
        tokens = nltk.tokenize.word_tokenize(sent)
        tags = st.tag(tokens)
        for tag in tags:
            if tag[1]=='PERSON': names.append(tag)

print(names)

