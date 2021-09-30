# -*- coding: utf-8 -*-
from bs4 import BeautifulSoup
import requests
#For names:
import nltk
import os
java_path = r'C:\Program Files\Java\jre1.8.0_301\bin\java.exe'
os.environ['JAVAHOME'] = java_path
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
print("End of headlines")
names = []

st = StanfordNERTagger(r'C:\Users\bendi\AppData\Roaming\nltk_data\stanford-ner-2020-11-17\classifiers\english.all.3class.distsim.crf.ser.gz',
           r'C:\Users\bendi\AppData\Roaming\nltk_data\stanford-ner-2020-11-17\stanford-ner-4.2.0.jar')

for text in headlines:

    for sent in nltk.sent_tokenize(text):
        tokens = nltk.tokenize.word_tokenize(sent)
        tags = st.tag(tokens)
        print(tags)
        currentindex = -1
        for i in range(0,len(tags)):
            if i > currentindex and tags[i][1] == 'PERSON':
                fullname = tags[i][0]
                while i+1 < len(tags) and tags[i+1][1] == 'PERSON':
                    i += 1
                    currentindex = i
                    fullname = fullname + ' ' + tags[i][0]
                names.append(fullname)


        # for tag in tags:
        #     if tag[1]=='PERSON': 
        #         names.append(tag[0])

print(names)

