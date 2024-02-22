#!/usr/bin/env python
# coding: utf-8

# In[9]:


import requests
from bs4 import BeautifulSoup as bs

page1 = requests.get('https://en.wikipedia.org/wiki/Main_Page')
soup1 = bs(page.content)
header1 = soup1.find_all(['h1','h2'])
h1 = []
for i in header1:
    h1.append(i.text)
print(f'Headers on the wikipedia page are: \n {h1}')


# In[13]:


page7 = requests.get('https://www.dineout.co.in/pune-restaurants/seafood-cuisine')
soup7 = BeautifulSoup(page7.content)

hotel = soup7.find('div', class_="restnt-info cursor")

print(hotel.text)

location = soup7.find('div', class_="restnt-loc ellipsis")
print(location.text)

cusine= soup7.find('span', class_="double-line-ellipsis")
print(cusine.text)

rating = soup7.find('div', class_="restnt-rating rating-5")
print(rating.text)

image = soup7.find('img', class_="no-img")
print(image['data-src'])


# In[14]:


page15 = requests.get('https://presidentofindia.nic.in/former-presidents')


soup15 = BeautifulSoup(page15.content)

presidents =[]
for i in soup15.find_all('div', class_="desc-sec"):
    presidents.append(i.text)

presidents


# In[ ]:




