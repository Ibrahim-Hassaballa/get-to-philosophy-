#!/usr/bin/env python
# coding: utf-8

# # import web scrapping library 

# In[2]:


from bs4 import BeautifulSoup
import requests
import time


# In[3]:


add_link="https://en.wikipedia.org"


# In[4]:


target="https://en.wikipedia.org/wiki/Philosophy"


# In[ ]:


def search(link):
    l=[]
    soup=BeautifulSoup(link.text,'html.parser')    
    for div in soup.find_all("p"): 
        a = div.find('a', href=True) # find <a> anywhere in <div>
        if a:
            l.append(a['href'])
            url=l[0]
            
            new=add_link+url
            if new == target:
                return target
            else:
                l=[]
                return new
                


# In[ ]:


links=[]
link=requests.get("https://en.wikipedia.org/wiki/Special:Random")
while True:
    url = search(link)
    if url == target:
        print("you are in philosophy that link :",(url))

        break
    elif url in links:
        print("we are in stuck in a loop",url)
        break
    else:
        links.append(url)
        time.sleep(1)
        link = requests.get(url)
        
            
for i in links:
    print("links are reached :",i)


# In[ ]:




