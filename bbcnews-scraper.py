#!/usr/bin/env python
# coding: utf-8

# In[37]:


import requests
from bs4 import BeautifulSoup
import csv
import html


# In[42]:


# fetch page
page = requests.get("https://www.bbc.co.uk/news", headers={"User-Agent":"Mozilla/5.0"})
# check response
print(f"Status code: {page.status_code}")
if page.status_code != 200:
    print("failed to fetch page")
    exit()
# parse html
soup = BeautifulSoup(page.text, "html.parser")
headlines = soup.findAll("span", {"aria-hidden":"false"})
# open csv with utf-8 encoding
with open("scraped-news.csv", "w", encoding="utf-8", newline="") as file:
    writer = csv.writer(file)
    writer.writerow(["HEADLINES"])
    # track unique headlines
    seen = set()
        
    for headline in headlines:
        text = headline.get_text(strip=True)
        text = html.unescape(text) # decode symbols
        if text and text not in seen:
            seen.add(text)
            print(text)
            writer.writerow([text])


# In[43]:


file.close()


# In[1]:


get_ipython().system('jupyter nbconvert --to script bbcnews-scraper.ipynb')

