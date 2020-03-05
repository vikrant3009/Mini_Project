# -*- coding: utf-8 -*-
"""
Created on Wed Mar  4 18:50:25 2020

@author: VIKRANT
"""

import bs4
import requests

stock_name= 'sensex'
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
    print("\n-------This is page "+ str(i+1) + "  -------------")
    for i in range(25):  
        news_id = "newslist-" + str(i)
        news.append(soup.find('li',{"class":"clearfix", "id":news_id}).h2.text)
        dnt.append(soup.find('li',{"class":"clearfix", "id":news_id}).span.text)
    for i in range(25):
        print("****************************************")
        print(dnt[i] + " : \t" + news[i])
    print("*-*-*-*-*-*-*-*-*-*-*-*-**-*-*-*-*-*-*-*")
    print("---------------------------------------")
    
