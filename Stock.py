# -*- coding: utf-8 -*-
"""
Created on Thu Mar  5 15:53:30 2020

@author: VIKRANT
"""


import bs4
import requests

stock_name= 'RELIANCE'
link = "https://in.finance.yahoo.com/quote/" + stock_name +".NS/history"
res = requests.get(link)
print(res)

soup = bs4.BeautifulSoup(res.text, 'lxml')
        
price = []
dnt = []
#price.append(soup.find('tr',{"class":"BdT Bdc($seperatorColor) Ta(end) Fz(s) Whs(nw)", "data-reactid":"49"}))
#price.append(soup.find('td',{"class":"Py(10px) Ta(start) Pend(10px)" , "data-reactid":"52"}).span.text)

for i in range(51,1402,15):
    dnt.append(soup.find('span',{"data-reactid":str(i)}).text)
    price.append(soup.find('span', {"data-reactid":str(i+10)}).text)
    
for i in range(len(price)):
    print(dnt[i] + " : \t" + price[i])
