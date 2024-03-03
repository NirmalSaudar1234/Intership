#!/usr/bin/env python
# coding: utf-8

# #### 1) Write a python program to display IMDB’s Top rated 100 Indian movies’ data
# https://www.imdb.com/list/ls056092300/ (i.e. name, rating, year ofrelease) and make data frame.

# In[133]:


import requests
from bs4 import BeautifulSoup
import pandas as pd
import re
page = requests.get('https://www.imdb.com/list/ls056092300/')
soup = BeautifulSoup(page.content)


movies =[]
for i in soup.find_all('h3', class_='lister-item-header'):
    movies.append(i.text.replace('\n',''))

year =[]
for i in soup.find_all('span', class_="lister-item-year text-muted unbold"):
    year.append(i.text.replace('\n',''))
    
rating =[]
for i in soup.find_all('div', class_="ipl-rating-star small"):
    rating.append(i.text.replace('\n',''))
    
imdb = pd.DataFrame({
'movie_name': movies,
'movie_year': year,
'imdb_ratings':rating,
})

imdb['movie_name'] = imdb['movie_name'].str.replace('[^a-zA-Z\s]', '',regex=True)

imdb.head(20)


# ### 2) Write a python program to scrape product name, price and discounts from
# https://peachmode.com/search?q=bags

# In[132]:


page = requests.get('https://peachmode.com/search?q=bags')
soup = BeautifulSoup(page.content)


product_name =[]
for i in soup.find_all('div', class_='product-title'):
    product_name.append(i.text)

discounted_price =[]
for i in soup.find_all('span', class_="discounted_price st-money money done"):
    discounted_price .append(i.text)
    
original_price =[]
for i in soup.find_all('span', class_="price st-money money done"):
    original_price.append(i.text)

print(product_name)   
print(discounted_price)
print(original_price)


# # 5) Write a python program to scrape house details from mentioned URL. It should include house title, location,area, EMI and price from https://www.nobroker.in/ .Enter three localities which are Indira Nagar, Jayanagar,Rajaji Nagar.
# 

# In[131]:


url = 'https://www.nobroker.in/property/sale/bangalore/multiple?searchParam=W3sibGF0IjoxMi45OTUwNTc3LCJsb24iOjc3LjUyMDczNzU5OTk5OTk5LCJwbGFjZUlkIjoiQ2hJSlViaVRNTEk5cmpzUlpPSy1TQUFDMFZZIiwicGxhY2VOYW1lIjoiSW5kaXJhIE5hZ2FyLCBIZWdnYW5haGFsbGkifSx7ImxhdCI6MTIuOTMwNzczNSwibG9uIjo3Ny41ODM4MzAyLCJwbGFjZUlkIjoiQ2hJSjJkZGxaNWdWcmpzUmgxQk9BYWYtb3JzIiwicGxhY2VOYW1lIjoiSmF5YW5hZ2FyIn0seyJsYXQiOjEyLjk5ODE3MzIsImxvbiI6NzcuNTUzMDQ0NTk5OTk5OTksInBsYWNlSWQiOiJDaElKeGZXNERQTTlyanNSS3NOVEctNXBfUVEiLCJwbGFjZU5hbWUiOiJSYWphamluYWdhciJ9XQ==&radius=2.0&city=bangalore&locality=Indira%20Nagar,%20Hegganahalli,Jayanagar,Rajajinagar'
house_title = []
location=[]
area=[]
emi=[]
price=[]

p = requests.get(url)
b = BeautifulSoup(p.content)


for i in b.find_all('span',class_="overflow-hidden overflow-ellipsis whitespace-nowrap max-w-80pe po:max-w-full"):
    house_title.append(i.text)
 
for i in b.find_all('div',class_="mt-0.5p overflow-hidden overflow-ellipsis whitespace-nowrap max-w-70 text-gray-light leading-4 po:mb-0.1p po:max-w-95"):
    location.append(i.text)


for i in b.find_all('div',class_="p-1.5p flex border-b border-b-solid border-cardbordercolor tp:py-1p tp:px-1.5p tp:border-b-0"):
    area.append(i.text.split("₹")[1].replace("sqftBuiltup",""))


for i in b.find_all('div',class_="p-1.5p flex border-b border-b-solid border-cardbordercolor tp:py-1p tp:px-1.5p tp:border-b-0"):
    emi.append(i.text.split("₹")[2].replace("/MonthEstimated EMI",""))  



for i in b.find_all('div',class_="p-1.5p flex border-b border-b-solid border-cardbordercolor tp:py-1p tp:px-1.5p tp:border-b-0"):
    price.append(i.text.split("₹")[3])  


df = pd.DataFrame(list(zip(house_title,location,area,emi,price)), columns=["Name of House","Location","Area","EMI","Price"])
print(df)






# # Q] Please visit https://www.keaipublishing.com/en/journals/artificial-intelligence-in-agriculture/most-downloaded-articles/ and scrap-

# In[130]:


page21 = requests.get('https://www.keaipublishing.com/en/journals/artificial-intelligence-in-agriculture/most-downloaded-articles/')
soup21 = BeautifulSoup(page21.content)

headlines = soup21.find('body').find_all('h2')
for x,y in enumerate(headlines):
    print(x,y.text.strip())
    
date = soup21.find('body').find_all('p',class_="article-date")
for x in date:
    print(x.text.strip())


authors = soup21.find('body').find_all('p',class_="article-authors")
for x in authors:
    print(x.text.strip())
    
    
keai = pd.DataFrame(list(zip(headlines,date,authors)), columns=['Paper_Titles','Date','imdb_ratings'])

print(keai)


# # Q1-Please visit https://www.cnbc.com/world/?region=world and scrap-

# In[129]:


import requests
import pandas as pd
from bs4 import BeautifulSoup
from datetime import date
today = date.today()
d = today.strftime("%m-%d-%y")
print("date =" ,d)
date = 10-27-21

cnbc = "https://www.cnbc.com/world/?region=world"
res = requests.get(cnbc)
soup = BeautifulSoup(res.content, 'html.parser')

headlines = soup.find('body').find_all('h2')
for x in headlines:
    print(x.text.strip())
    

links = soup.find_all('h2', class_="SectionWrapper-title")
for x in headlines:
    print(x.text.strip())
    
print(links)


# In[ ]:




