# -*- coding: utf-8 -*-
"""
Created on Thu Mar  5 15:53:30 2020

@author: VIKRANT
"""


import bs4
import requests

stock_name= 'ASHOKLEY'
link = "https://in.finance.yahoo.com/quote/" + stock_name +".NS/history?p=" + stock_name +".NS&.tsrc=fin-srch"
res = requests.get(link)
print(res)

soup = bs4.BeautifulSoup(res.text, 'lxml')
        
price = []
dnt = []
#price.append(soup.find('tr',{"class":"BdT Bdc($seperatorColor) Ta(end) Fz(s) Whs(nw)", "data-reactid":"49"}))
#price.append(soup.find('td',{"class":"Py(10px) Ta(start) Pend(10px)" , "data-reactid":"52"}).span.text)
price.append(soup.find('span',{"data-reactid":"53"}))
print(price)
    