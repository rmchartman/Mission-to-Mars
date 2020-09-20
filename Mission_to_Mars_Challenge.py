#!/usr/bin/env python
# coding: utf-8

# In[1]:


# Import Splinter and BeautifulSoup
from splinter import Browser
from bs4 import BeautifulSoup as soup
import pandas as pd


# In[2]:


# Set the executable path and initialize the chrome browser in splinter
executable_path = {'executable_path': 'chromedriver'}
browser = Browser('chrome', **executable_path)


# In[3]:


# Visit the mars nasa news site
url = 'https://mars.nasa.gov/news/'
browser.visit(url)
# Optional delay for loading the page
browser.is_element_present_by_css("ul.item_list li.slide", wait_time=1)


# In[4]:


# Set up HTML parser
html = browser.html
news_soup = soup(html, 'html.parser')
slide_elem = news_soup.select_one('ul.item_list li.slide')


# In[5]:


# Use the parent element to find the first `a` tag and save it as `news_title`
news_title = slide_elem.find("div", class_='content_title').get_text()
news_title


# In[6]:


# Use the parent element to find the paragraph text
news_p = slide_elem.find('div', class_="article_teaser_body").get_text()
news_p


# ### Featured Images

# In[7]:


# Visit URL
url = 'https://www.jpl.nasa.gov/spaceimages/?search=&category=Mars'
browser.visit(url)


# In[8]:


# Find and click the full image button
full_image_elem = browser.find_by_id('full_image')
full_image_elem.click()


# In[9]:


# Find the more info button and click that
browser.is_element_present_by_text('more info', wait_time=1)
more_info_elem = browser.links.find_by_partial_text('more info')
more_info_elem.click()


# In[ ]:


# Parse the resulting html with soup
html = browser.html
img_soup = soup(html, 'html.parser')


# In[ ]:


# Find the relative image url
img_url_rel = img_soup.select_one('figure.lede a img').get("src")
img_url_rel


# In[ ]:


# Use the base URL to create an absolute URL
img_url = f'https://www.jpl.nasa.gov{img_url_rel}'
img_url


# ### MARS FACTS

# In[ ]:


df = pd.read_html('http://space-facts.com/mars/')[0]
df.columns=['Description', 'Mars Value']
df.set_index('Description', inplace=True)
df


# In[ ]:


df.to_html()


# ### Mars Weather

# In[ ]:


# Visit the weather website
url = 'https://mars.nasa.gov/insight/weather/'
browser.visit(url)


# In[ ]:


# Parse the data
html = browser.html
weather_soup = soup(html, 'html.parser')


# In[ ]:


# Scrape the Daily Weather Report table
weather_table = weather_soup.find('table', class_='mb_table')
print(weather_table.prettify())


# In[10]:


# 1. Use browser to visit the URL 
url = 'https://astrogeology.usgs.gov/search/results?q=hemisphere+enhanced&k1=target&v1=Mars'
browser.visit(url)


# In[11]:


# 2. Create a list to hold the images and titles.
hemisphere_image_urls = []

# 3. Write code to retrieve the image urls and titles for each hemisphere.

# Find and click the full image button
html = browser.html
html_soup = soup(html, 'html.parser')
titles = html_soup.find_all('h3')

for t in titles:
    #image_name = image_name.find_all('h3')
    title = t.get_text()
    
    

    browser.visit(url)
    html = browser.html
    html_soup = soup(html, 'html.parser')
    image_url = html_soup.find('div', class_='description')
    image_url = image_url.find('a').get('href')
    image_url = 'https://astrogeology.usgs.gov'+ image_url
    browser.visit(image_url)
    html = browser.html
    html_soup = soup(html, 'html.parser')
    image_url = html_soup.find(class_='downloads')
    image_url = image_url.find('li')
    image_url = image_url.find('a').get('href')
    #print(image_url)
    
    
    hemispheres = {"img_url": image_url,
                  "title": title}
    hemispheres
    hemisphere_image_urls.append(hemispheres)
    
    browser.visit(url)
    


# In[12]:


# 4. Print the list that holds the dictionary of each image url and title.
hemisphere_image_urls


# In[13]:


browser.quit()


# In[ ]:




