#!/usr/bin/env python
# coding: utf-8

# QUESTION == 1

# In[ ]:


import selenium
import pandas as pd
from selenium import webdriver

import warnings
warnings.filterwarnings('ignore')
from selenium.common.exceptions import StaleElementReferenceException, NoSuchElementException
from selenium.webdriver.common.by import By
import time


# In[ ]:


#First connect to the driver
driver=webdriver.Chrome(r'‪C:\Users\govind\Desktop\chromedriver.exe')


# In[ ]:


#Opening the automated chrome page
driver.get("https://www.naukri.com/")


# In[ ]:


#Entering designation and location
designation = driver.find_element(By.CLASS_NAME,"suggestor-input")
designation.send_keys("Data Analyst")


# In[ ]:


location = driver.find_element(By.XPATH,"/html/body/div[1]/div[6]/div/div/div[5]/div/div/div/input")
location.send_keys("Banglore")


# In[ ]:


search = driver.find_element(By.CLASS_NAME,"qsbSubmit")
search.click()


# In[ ]:





# In[ ]:


job_title = []
job_location = []
company_name = []
experience_required = []


# In[ ]:


#Scraping job title from the given page
title_tags=driver.find_elements(By.XPATH,'//a[@class="title ellipsis"]')
for i in title_tags[0:10]:
    title=i.text
    job_title.append(title)

#Scraping job_location from the given page
location_tags=driver.find_elements(By.XPATH,'//span[@class="ellipsis fleft locWdth"]')
for i in location_tags[0:10]:
    loc=i.text
    job_location.append(loc)

#Scraping Company name from the given page
company_tags=driver.find_elements(By.XPATH,'//a[@class="subTitle ellipsis fleft"]')
for i in company_tags[0:10]:
    company=i.text
    company_name.append(company)
    
#Scraping Experience required from the given page
experience_tags=driver.find_elements(By.XPATH,'//span[@class="ellipsis fleft expwdth"]')
for i in experience_tags[0:10]:
    exp=i.text
    experience_required.append(exp)


# In[ ]:


print(len(job_title),len(job_location),len(company_name),len(experience_required))


# In[ ]:


#Preparing database for ten job_title,location, company_name and experience_required
df=pd.DataFrame({'Title':job_title,'Location':job_location,'Company':company_name,'Experience':experience_required})


# In[ ]:


df


# In[ ]:





# In[ ]:


'*'*125


# QUESTION == 2

# In[ ]:


import selenium
import pandas as pd
from selenium import webdriver

import warnings
warnings.filterwarnings('ignore')
from selenium.common.exceptions import StaleElementReferenceException, NoSuchElementException
from selenium.webdriver.common.by import By


# In[ ]:


#import webdriver
driver=webdriver.Chrome(r"C:\Users\govind\Desktop\chromedriver.exe")


# In[ ]:


#Opening the automated chrome page form naukri.com
driver.get(r'https://www.naukri.com/')


# In[ ]:


#Scrap for Designation and job_location

designation=driver.find_element(By.XPATH,'/html/body/div[1]/div[6]/div/div/div[1]/div/div/div/input')
designation.send_keys(" Data Scientist")


location=driver.find_element(By.XPATH,'/html/body/div[1]/div[6]/div/div/div[5]/div/div/div/input')
location.send_keys("Banglore")


# In[ ]:


#Scraping Search from site
search=driver.find_element(By.XPATH,'/html/body/div[1]/div[6]/div/div/div[6]')
search.click()


# In[ ]:


job_title=[]
job_location=[]
company_name=[]
experience_required=[]


# In[ ]:


#Scraping job_title from the web page
title_tags=driver.find_elements(By.XPATH,'//a[@class="title ellipsis"]')
for i in title_tags[0:10]:
    title=i.text
    job_title.append(title)
    
#Scraping job_location from the web_page
location_tags=driver.find_elements(By.XPATH,'//span[@class="ellipsis fleft locWdth"]')
for i in location_tags[0:10]:
    location=i.text
    job_location.append(location)
    
#Scraping company_name form the web_page
company_tags=driver.find_elements(By.XPATH,'//a[@class="subTitle ellipsis fleft"]')
for i in company_tags[0:10]:
    company=i.text
    company_name.append(company)
    
#Scraping  Experience_required from web_page
experience_tags=driver.find_elements(By.XPATH,'//span[@class="ellipsis fleft expwdth"]')
for i in experience_tags[0:10]:
    exp=i.text
    experience_required.append(exp)


# In[ ]:


print(len(job_title),len(job_location),len(company_name),len(experience_required))


# In[ ]:


data=pd.DataFrame({'Title':job_title,'Location':job_location,'Company':company_name,'Experience':experience_required})
data


# In[ ]:





# In[ ]:


'#'*125


# QUESTION == 3

# In[ ]:


import selenium
import pandas as pd
from selenium import webdriver
from selenium.common.exceptions import StaleElementReferenceException, NoSuchElementException
from selenium.webdriver.common.by import By

import warnings
warnings.filterwarnings('ignore')
import time


# In[ ]:


#import web driver
driver=webdriver.Chrome(r'C:\Users\govind\Desktop\chromedriver.exe')


# In[ ]:


#opening automated scap page of naukri.com
driver.get("https://www.naukri.com/")


# In[ ]:


#Scraping the designation and location
designation=driver.find_element(By.XPATH,'/html/body/div[1]/div[6]/div/div/div[1]/div/div/div/input')
designation.send_keys(" Data Scientist")

location=driver.find_element(By.XPATH,'/html/body/div[1]/div[6]/div/div/div[5]/div/div/div/input')
location.send_keys("Delhi/NCR")

#salary=driver.find_element(By.CLASS_NAME,'class="ellipsis fleft "')
#salary.send_keys("3-6 Lakhs")

search=driver.find_element(By.XPATH,'/html/body/div[1]/div[6]/div/div/div[6]')
search.click()


# In[ ]:


job_title=[]
job_location=[]
company_name=[]
experience_required=[]


# In[ ]:


#scraping the job_title from the webpage
title_tags=driver.find_elements(By.XPATH,'//a[@class="title ellipsis"]')
for i in title_tags[0:10]:
    title=i.text
    job_title.append(title)
    
#scraping the job_location from the webpage
location_tags=driver.find_elements(By.XPATH,'//span[@class="ellipsis fleft locWdth"]')
for i in location_tags[0:10]:
    loc=i.text
    job_location.append(loc)
    
#scraping the salary fron the webpage
#salary_tags=driver.find_elements(By.XPATH,'//span[@class="ellipsis fleft filterLabel"]')
#for i in salary_tags[0:10]:
   # sal=i.text
   # salary.append(sal)
    
#scraping the company_name from the webpage
company_tags=driver.find_elements(By.XPATH,'//a[@class="subTitle ellipsis fleft"]')
for i in company_tags[0:10]:
    com=i.text
    company_name.append(com)

#Scraping the Experience_required from the webpage
experience_tags=driver.find_elements(By.XPATH,'//span[@class="ellipsis fleft expwdth"]')
for i in experience_tags[0:10]:
    exp=i.text
    experience_required.append(exp)


# In[ ]:


print(len(job_title),len(job_location),len(company_name),len(experience_required))


# In[ ]:


df=pd.DataFrame({'Title':job_title,'Location':job_location,'Company':company_name,'Experience':experience_required})


# QUESTION == 4

# In[ ]:


#Import Libraries

import pandas as pd
import selenium
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException, StaleElementReferenceException
from selenium.webdriver.common.by import By


# In[ ]:


#Connect to the webdriver
driver=webdriver.Chrome(r'C:\Users\govind\Desktop\chromedriver.exe')


# In[ ]:


#opening automated scap page of flipkart.com
driver.get("https://www.flipkart.com/")


# In[ ]:


# finding element for job search bar
search_g= driver.find_element(By.XPATH,"//input[@type='text']")
search_g.send_keys("sunglasses")

search_btn=driver.find_element(By.XPATH,"//button[@class='L0Z3Pu']")
search_btn.click()


# In[ ]:


#Make a list
brand_name=[]
product_description=[]
price=[]


# In[ ]:


#Scraping the Brand, Product_description and Price
start=0
end=4
for page in range(start,end):
    brand_tags=driver.find_elements(By.XPATH,"//div[@class='_2WkVRV']")
    for i in brand_tags:
        brand_n=i.text[:100]
        brand_name.append(brand_n)
    
    product_tags=driver.find_elements(By.XPATH,"//a[@class='IRpwTa']")
    for i in product_tags:
        pro_desc=i.text[:100]
        product_description.append(pro_desc)
    
    price_tags=driver.find_elements(By.XPATH,"//div[@class='_25b18c']")
    for i in price_tags:
        price_t=i.text[:100]
        price.append(price_t)
next_button=driver.find_elements(By.XPATH,"/html/body/div[1]/div/div[3]/div[1]/div[2]/div[12]/div/div/nav/a[11]")
next_button.click()
time.sleep(3)


# In[ ]:


print(len(brand_name),len(product_description),len(price))


# In[ ]:





# In[ ]:


df=pd.DataFrame({'Brand':brand_name,'Product Details':product_description,'Price':price})
df


# In[ ]:





# QUESTION == 5 

# In[52]:


#import libraries
import pandas as pd
import selenium
from selenium import webdriver
from selenium.common.exceptions import StaleElementReferenceException, NoSuchElementException

import warnings
warnings.filterwarnings('ignore')
import time


# In[53]:


#first connect to the webdriver
driver=webdriver.Chrome(r'C:\Users\govind\Desktop\chromedriver.exe')


# In[55]:


# Lets opening the automated page of Flipkart
driver.get('https://www.flipkart.com/apple-iphone-11-black-64-gb-includes-earpods-power-adapter/product-reviews/itm0f37c2240b217?pid=MOBFKCTSVZAXUHGR&lid=LSTMOBFKCTSVZAXUHGREPBFGI&marketplace=FLIPKART')


# In[56]:


#Make a list
rating=[]
review_summary=[]
full_review=[]


# In[58]:


#Scraping the Rating
start=0
end=10
for page in range(start,end):
    rating_tags=driver.find_elements(By.XPATH,'//div[@class="_3LWZlK _1BLPMq"]')
    
    for i in rating_tags:
        rating_n=i.text[:100]
        rating.append(rating_n)
        
    next_button=driver.find_element(By.XPATH,'//a[@class="_1LKTO3"]')
    next_button.click()
    time.sleep(3)


# In[60]:


#Scraping the review Summary
start=0
end=10
for page in range(start,end):
    review_tags=driver.find_elements(By.XPATH,'//p[@class="_2-N8zT"]')
    
    for i in review_tags:
        review_n=i.text[:100]
        review_summary.append(review_n)
        
    next_button=driver.find_element(By.XPATH,'//a[@class="_1LKTO3"]')
    next_button.click()
    time.sleep(3)


# In[77]:


#Scraping the Full review
start=0
end=10
for page in range(start,end):
    f_review_tags=driver.find_elements(By.XPATH,'//div[@class="t-ZTKy"]')
    
    for i in f_review_tags[0:100]:
        review_n=i.text
        full_review.append(review_n)
        
    next_button=driver.find_element(By.XPATH,'//a[@class="_1LKTO3"]')
    next_button.click()
    time.sleep(3)


# In[ ]:


rating[:100]


# In[80]:


print(len(rating[:100]),len(review_summary[:100]),len(full_review[:100]))


# In[ ]:


df=pd.DataFrame({'Rating':rating,'Review Summary':review_summary,'Full Review':full_review})


# In[ ]:





# QUESTION == 6

# In[85]:


#Import Libraries

import pandas as pd
import selenium
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException, StaleElementReferenceException
from selenium.webdriver.common.by import By


# In[86]:


#first connect to the webdriver
driver=webdriver.Chrome(r'C:\Users\govind\Desktop\chromedriver.exe')


# In[87]:


#opening automated scap page of flipkart.com
driver.get("https://www.flipkart.com/")


# In[88]:


# finding element for job search bar
search_g= driver.find_element(By.XPATH,"//input[@type='text']")
search_g.send_keys("sneakers")

search_btn=driver.find_element(By.XPATH,"//button[@class='L0Z3Pu']")
search_btn.click()


# In[ ]:


#Make a list
brand_name=[]
product_description=[]
price=[]


# In[ ]:





# In[ ]:


#Scraping the Brand
start=0
end=4
for page in range(start,end):
    brand_tags=driver.find_elements(By.XPATH,"//div[@class='_2WkVRV']")
    for i in brand_tags:
        brand_n=i.text[:100]
        brand_name.append(brand_n)
    
next_button=driver.find_elements(By.XPATH,"/html/body/div[1]/div/div[3]/div[1]/div[2]/div[12]/div/div/nav/a[11]")
next_button.click()
time.sleep(3)


# In[ ]:


#Scraping the Product_description
start=0
end=4
for page in range(start,end):
    product_tags=driver.find_elements(By.XPATH,"//div[@class='_2WkVRV']")
    for i in product_tags:
        pro_n=i.text[:100]
        product_description.append(pro_n)
    
next_button=driver.find_elements(By.XPATH,"/html/body/div[1]/div/div[3]/div[1]/div[2]/div[12]/div/div/nav/a[11]")
next_button.click()
time.sleep(3)


# In[ ]:


#Scraping the Price
start=0
end=4
for page in range(start,end):
    price_tags=driver.find_elements(By.XPATH,"//div[@class='_2WkVRV']")
    for i in price_tags:
        price_n=i.text[:100]
        price.append(price_n)
    
next_button=driver.find_elements(By.XPATH,"/html/body/div[1]/div/div[3]/div[1]/div[2]/div[12]/div/div/nav/a[11]")
next_button.click()
time.sleep(3)


# In[ ]:




