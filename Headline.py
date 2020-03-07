 # -*- coding: utf-8 -*-
"""
Created on Wed Mar  4 18:50:25 2020

@author: VIKRANT
"""
#my name is vikrant
import bs4
import requests
import nltk
from nltk.sentiment.vader import SentimentIntensityAnalyzer

stock_name= 'reliance'
for i in range(7):
    if i==0:
        link = "https://www.moneycontrol.com/news/tags/" + stock_name +".html"
        res = requests.get(link)
    else:
        page = "/page-" + str(i+1) + "/"
        link = "https://www.moneycontrol.com/news/tags/" + stock_name +".html" + page
        res = requests.get(link)
    
    soup = bs4.BeautifulSoup(res.text, 'lxml')
        
    news = []
    dnt = []
    #print("\n-------This is page "+ str(i+1) + "  -------------")
    for i in range(25):  
        news_id = "newslist-" + str(i)
        news.append(soup.find('li',{"class":"clearfix", "id":news_id}).h2.text)
        dnt.append(soup.find('li',{"class":"clearfix", "id":news_id}).span.text[:-13])
   # for i in range(25):
      #  print("****************************************")
     #   print(dnt[i] + " : \t" + news[i])
    #print("*-*-*-*-*-*-*-*-*-*-*-*-**-*-*-*-*-*-*-*")
   # print("---------------------------------------")
    

#import nltk
#from nltk.sentiment.vader import SentimentIntensityAnalyzer
sia = SentimentIntensityAnalyzer()
score = []

for i in range(7):
    for i in range(25):
        score.append(sia.polarity_scores(news[i])['compound'])

for i in range(7):
    for i in range(25):
        print(dnt[i] +" : " + str(score[i]) + " : " + news[i])
        


for i in range(7):
    for i in range(25):
        datevalue = dnt[i][-4:]
        if dnt[i][0:3] == 'Jan':
            datevalue = datevalue + '01' + dnt[i][-8:-6]
        elif dnt[i][0:3] == 'Feb':
            datevalue = datevalue + '02' + dnt[i][-8:-6]
        elif dnt[i][0:3] == 'Mar':
            datevalue = datevalue + '03' + dnt[i][-8:-6]
        elif dnt[i][0:3] == 'Apr':
            datevalue = datevalue + '04' + dnt[i][-8:-6]
        elif dnt[i][0:3] == 'May':
            datevalue = datevalue + '05' + dnt[i][-8:-6]
        elif dnt[i][0:3] == 'Jun':
            datevalue = datevalue + '06' + dnt[i][-8:-6]
        elif dnt[i][0:3] == 'Jul':
            datevalue = datevalue + '07' + dnt[i][-8:-6]
        elif dnt[i][0:3] == 'Aug':
            datevalue = datevalue + '08' + dnt[i][-8:-6]
        elif dnt[i][0:3] == 'Sep':
            datevalue = datevalue + '09' + dnt[i][-8:-6]
        elif dnt[i][0:3] == 'Oct':
            datevalue = datevalue + '10' + dnt[i][-8:-6]
        elif dnt[i][0:3] == 'Nov':
            datevalue = datevalue + '11' + dnt[i][-8:-6]
        elif dnt[i][0:3] == 'Dec':
            datevalue = datevalue + '12' + dnt[i][-8:-6]