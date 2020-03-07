# -*- coding: utf-8 -*-
"""
Created on Fri Mar  6 15:46:18 2020

@author: VIKRANT
"""



import bs4
import requests

stock_name= 'RELIANCE'
link = "https://in.finance.yahoo.com/quote/" + stock_name +".NS/history"
res = requests.get(link)
print(res)

soup = bs4.BeautifulSoup(res.text, 'lxml')
        
dnt = []
#price.append(soup.find('tr',{"class":"BdT Bdc($seperatorColor) Ta(end) Fz(s) Whs(nw)", "data-reactid":"49"}))
#price.append(soup.find('td',{"class":"Py(10px) Ta(start) Pend(10px)" , "data-reactid":"52"}).span.text)

for i in range(51,1402,15):
    dnt.append(soup.find('span',{"data-reactid":str(i)}).text)
    
print(dnt[1])

monthvalue = {'Jan':'01', 'Feb':'02', 'Mar':'03', 'Apr':'04', 'May':'05', 'Jun':'06', 'Jul':'07', 'Aug':'08', 'Sep':'09', 'Oct':'10', 'Nov':'11', 'Dec':'12'}

datevalue = dnt[1][-4:]
if dnt[1][3:6] == 'Jan':
    datevalue = datevalue + '01' + dnt[1][:2]
elif dnt[1][3:6] == 'Feb':
    datevalue = datevalue + '02' + dnt[1][:2]
elif dnt[1][3:6] == 'Mar':
    datevalue = datevalue + '03' + dnt[1][:2]
elif dnt[1][3:6] == 'Apr':
    datevalue = datevalue + '04' + dnt[1][:2]
elif dnt[1][3:6] == 'May':
    datevalue = datevalue + '05' + dnt[1][:2]
elif dnt[1][3:6] == 'Jun':
    datevalue = datevalue + '06' + dnt[1][:2]
elif dnt[1][3:6] == 'Jul':
    datevalue = datevalue + '07' + dnt[1][:2]
elif dnt[1][3:6] == 'Aug':
    datevalue = datevalue + '08' + dnt[1][:2]
elif dnt[1][3:6] == 'Sep':
    datevalue = datevalue + '09' + dnt[1][:2]
elif dnt[1][3:6] == 'Oct':
    datevalue = datevalue + '10' + dnt[1][:2]
elif dnt[1][3:6] == 'Nov':
    datevalue = datevalue + '11' + dnt[1][:2]
elif dnt[1][3:6] == 'Dec':
    datevalue = datevalue + '12' + dnt[1][:2]
    


        