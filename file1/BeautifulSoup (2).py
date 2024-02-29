#!/usr/bin/env python
# coding: utf-8

# #### 1) Write a python program to display IMDB’s Top rated 100 Indian movies’ data
# https://www.imdb.com/list/ls056092300/ (i.e. name, rating, year ofrelease) and make data frame.

# In[7]:


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

# In[56]:


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


# #### 3) Write a python program to scrape cricket rankings from icc-cricket.com. You have to scrape:
# a) Top 10 ODI teams in men’s cricket along with the records for matches, points and rating.
# 
# b) Top 10 ODI Batsmen along with the records of their team and rating.
# 
# c) Top 10 ODI bowlers along with the records of their team and rating.

# # 4) Write a python program to scrape details of all the posts from https://www.patreon.com/coreyms .Scrape the heading, date, content and the likes for the video from the link for the youtube video from the post.
# 

# # 5) Write a python program to scrape house details from mentioned URL. It should include house title, location,area, EMI and price from https://www.nobroker.in/ .Enter three localities which are Indira Nagar, Jayanagar,Rajaji Nagar.
# 

# In[18]:


url = 'https://www.nobroker.in/'
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


df = pd.DataFrame({"Name of House":house_title,"Location":location,"Area":area,"EMI":emi,"Price":price})


print(df)






# # 6) Write a python program to scrape first 10 product details which include product name , price , Image URL from https://www.bewakoof.com/bestseller?sort=popular 

# In[20]:


page11 = requests.get('https://shop.bewakoof.com/search?q=bestsellers')
soup11 = BeautifulSoup(page.content)


product_name =[]
for i in soup.find_all('div', class_=" max-w-prose text-copy w-full overflow-hidden whitespace-nowrap text-ellipsis text-[#737373] text-[10px] pt-1 lg:text-[#676767] font-[familyRegular] lg:font-[familyMedium] lg:text-sm"):
    product_name.append(i.text)

price =[]
for i in soup.find_all('span', class_="text-[#0F0F0F] text-[10px] font-[familySemiBold] lg:font-[familyBold] lg:text-base productPrice"):
    discounted_price .append(i.text)
    
image =[]
for i in soup.find_all('span', class_="image-placeholder-bg h-full w-full object-cover"):
    original_price.append(i['data-src'])

print(product_name)   
print(price)
print(image)


# In[ ]:




