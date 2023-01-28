#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import selenium
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.common.exceptions import StaleElementReferenceException, NoSuchElementException
import time

import warnings
warnings.filterwarnings('ignore')


# In[2]:


#Install webdriver
driver = webdriver.Chrome(r'‪C:\Users\govind\Desktop\chromedriver.exe')


# In[3]:


#opening webpage of automated Chrome browser
driver.get('https://www.amazon.in')


# In[4]:


search_panel = driver.find_element(By.XPATH,'/html/body/div[1]/header/div/div[1]/div[2]/div/form/div[2]/div[1]/input')
search_panel.send_keys("guitar")

search_but = driver.find_element(By.XPATH,'//input[@id="nav-search-submit-button"]')
search_but.click()
#Brand Name", "Name of the Product", "Price", "Return/Exchange", "Expected Delivery", "Availability" and “Product URL”


# In[5]:


brand_name = []
name_of_the_product= []
price = []
return_exchange= []
expected_delivery= []
availability= []
product_url= []


# In[11]:


# scraping the brand name from web page
start = 0
end = 1
for page in range(start,end):
    brand_b= driver.find_elements(By.XPATH,'//h2[@class="a-size-mini a-spacing-none a-color-base s-line-clamp-4"]')
    for i in brand_b[0:10]:
        bran=i.text
        brand_name.append(bran)
    next_button=driver.find_element(By.XPATH,'//a[@class="s-pagination-item s-pagination-next s-pagination-button s-pagination-separator"]')
    next_button.click()
    time.sleep(3)


# In[ ]:


# scraping the name of product from web page
start = 0
end = 1
for page in range(start,end):
    product_b= driver.find_elements(By.XPATH,'//h2[@class="a-size-mini a-spacing-none a-color-base s-line-clamp-4"]')
    for i in product_b[0:10]:
        pro=i.text
        name_of_the_product.append(bran)
    next_button=driver.find_element(By.XPATH,'//a[@class="s-pagination-item s-pagination-next s-pagination-button s-pagination-separator"]')
    next_button.click()
    time.sleep(3)


# In[ ]:





# In[ ]:





# In[ ]:





# Question == 3

# In[25]:


import pandas as pd
import selenium
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.common.exceptions import StaleElementReferenceException, NoSuchElementException
import time

import warnings
warnings.filterwarnings('ignore')


# In[28]:


#Install webdriver
driver = webdriver.Chrome(r'‪C:\Users\govind\Desktop\chromedriver.exe')


# In[53]:


#opening webpage of automated Chrome browser
driver.get('https://www.google.com')

image_g=driver.find_element(By.XPATH,'/html/body/div[1]/div[1]/div/div/div/div[1]/div/div[2]/a')
image_g.click()

#fruits’, ‘cars’ and ‘Machine Learning’, ‘Guitar’, ‘Cakes


# In[54]:


search_bar=driver.find_element(By.XPATH,'//input[@class="gLFyf"]')
search_bar.send_keys("fruits")

search_btn=driver.find_element(By.XPATH,'//span[@class="z1asCe MZy1Rb"]')
search_btn.click()


# In[24]:


fruits = []
car_n_machine_learning =[]
guitar = []
cakes = []


# In[55]:


#scrap fruits images from page
fruit_tag=driver.find_elements(By.XPATH,'//div[@class="c7cjWc mvjhOe"]')
for i in fruit_tag[0:10]:
    fru=i.text
    fruits.append(fru)


# In[33]:





# In[ ]:





# In[50]:


#Opening automated Chrome web page
driver.get('https://www.google.com')

image_g=driver.find_element(By.XPATH,'/html/body/div[1]/div[1]/div/div/div/div[1]/div/div[2]/a')
image_g.click()


search_bar=driver.find_element(By.XPATH,'//input[@class="gLFyf"]')
search_bar.send_keys("car and machine learning")

search_btn=driver.find_element(By.XPATH,'//span[@class="z1asCe MZy1Rb"]')
search_btn.click()

#scrap car n ML images from page
car_tag=driver.find_elements(By.XPATH,'//div[@class=" bRMDJf islir"]')
for i in car_tag[0:10]:
    car_ml=i.text
    car_n_machine_learning.append(car_ml)


# In[40]:


#Opening automated Chrome web page
driver.get('https://www.google.com')

image_g=driver.find_element(By.XPATH,'/html/body/div[1]/div[1]/div/div/div/div[1]/div/div[2]/a')
image_g.click()


search_bar=driver.find_element(By.XPATH,'//input[@class="gLFyf"]')
search_bar.send_keys("guitar")

search_btn=driver.find_element(By.XPATH,'//span[@class="z1asCe MZy1Rb"]')
search_btn.click()

#scrap guitar images from page
guitar_tag=driver.find_elements(By.XPATH,'//div[@class=" bRMDJf islir"]')
for i in guitar_tag[0:10]:
    play=i.text
    guitar.append(play)


# In[47]:


#Opening automated Chrome web page
driver.get('https://www.google.com')

image_g=driver.find_element(By.XPATH,'/html/body/div[1]/div[1]/div/div/div/div[1]/div/div[2]/a')
image_g.click()


search_bar=driver.find_element(By.XPATH,'//input[@class="gLFyf"]')
search_bar.send_keys("cakes")

search_btn=driver.find_element(By.XPATH,'//span[@class="z1asCe MZy1Rb"]')
search_btn.click()

#scrap fruits images from page 
cake_tag=driver.find_elements(By.XPATH,'//div[@class=" bRMDJf islir"]') 
for i in cake_tag[0:10]:     
    food=i.text    
    cakes.append(food)


# In[56]:


print(len(fruits),len(car_n_machine_learning),len(guitar),len(cakes))


# In[ ]:





# In[ ]:


QUESTION == 4


# In[57]:


import pandas as pd
import selenium
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.common.exceptions import StaleElementReferenceException, NoSuchElementException
import time

import warnings
warnings.filterwarnings('ignore')


# In[58]:


#Install webdriver
driver = webdriver.Chrome(r'‪C:\Users\govind\Desktop\chromedriver.exe')


# In[64]:


#Opening automated Chrome web page
driver.get('https://www.flipkart.com')

search_bar=driver.find_element(By.XPATH,'//input[@class="_3704LK"]')
search_bar.send_keys("pixel 4A")

search_btn=driver.find_element(By.XPATH,'//button[@class="L0Z3Pu"]')
search_btn.click()

Brand Name”, “Smartphone name”, “Colour”, “RAM”, “Storage(ROM)”, 
“Primary Camera”, “Secondary Camera”, “Display Size”, “Battery Capacity”, “Price”, “Product URL


# In[71]:


#scrap brand name from page 
brand_tag=driver.find_elements(By.XPATH,'NAN') 
for i in brand_tag[0:1]:     
    cell=i.text    
    brand_name.append(cell)


# In[72]:


#scrap smartphone name from page 
sm_name_tag=driver.find_elements(By.XPATH,'//div[@class="_4rR01T"]') 
for i in sm_name_tag[0:1]:     
    cell=i.text    
    smartphone_name.append(cell)


# In[73]:


#scrap colour from page 
color_tag=driver.find_elements(By.XPATH,'/html/body/div/div/div[3]/div[1]/div[2]/div[2]/div/div/div/a/div[2]/div[1]/div[1]') 
for i in color_tag[0:1]:     
    cell=i.text    
    colour.append(cell)


# In[74]:


#scrap RAM from page 
ram_tag=driver.find_elements(By.XPATH,'//li[@class="rgWa7D"]') 
for i in ram_tag[0:1]:     
    cell=i.text    
    ram.append(cell)


# In[75]:


#scrap Storage from page 
storage_tag=driver.find_elements(By.XPATH,'/html/body/div/div/div[3]/div[1]/div[2]/div[2]/div/div/div/a/div[2]/div[1]/div[1]') 
for i in storage_tag[0:1]:     
    cell=i.text    
    storage.append(cell)


# In[76]:


#scrap Primary Camerafrom page 
p_camera_tag=driver.find_elements(By.XPATH,'//li[@class="rgWa7D"]') 
for i in p_camera_tag[0:1]:     
    cell=i.text    
    primary_camera.append(cell)


# In[77]:


#scrap secondary Camera from page 
s_camera_tag=driver.find_elements(By.XPATH,'//li[@class="rgWa7D"]') 
for i in s_camera_tag[0:1]:     
    cell=i.text    
    secondary_camera.append(cell)


# In[79]:


#scrap display_size from page 
display_tag=driver.find_elements(By.XPATH,'//li[@class="rgWa7D"]') 
for i in display_tag[0:1]:     
    cell=i.text    
    display_size.append(cell)


# In[80]:


#scrap battery_capacity from page 
battery_tag=driver.find_elements(By.XPATH,'//li[@class="rgWa7D"]') 
for i in battery_tag[0:1]:     
    cell=i.text    
    battery_capacity.append(cell)


# In[82]:


#scrap price from page 
price_tag=driver.find_elements(By.XPATH,'//div[@class="_30jeq3 _1_WHN1"]') 
for i in battery_tag[0:1]:     
    cell=i.text    
    price.append(cell)


# In[83]:


#scrap product_url from page 
url_tag=driver.find_elements(By.XPATH,'/html/body/div/div/div[3]/div[1]/div[2]/div[2]/div/div/div/a') 
for i in url_tag[0:1]:     
    cell=i.text    
    product_url.append(cell)


# In[78]:


brand_name = []
smartphone_name = []
colour = []
ram = []
storage = []
primary_camera =[]
secondary_camera = []
display_size = []
battery_capacity = []
price = []
product_url = []


# In[87]:


print(len(brand_name),len(smartphone_name),len(colour),len(ram),len(storage),len(primary_camera),len(secondary_camera),len(display_size),len(battery_capacity),len(price),len(product_url))


# In[ ]:


df=pd.DataFrame({'Brand':brand_name,'Name':smartphone_name,'Colour':colou,'RAM':ram,'Storage':storage = []'Front camera':primary_camera,'Back Camera':secondary_camera,'Display':display_size,'Battery':battery_capacity,'Price':price,'URL':product_url})
df

