#!/usr/bin/env python
# coding: utf-8

# In[5]:


import sqlite3


# In[6]:


db=sqlite3.connect("ERD_database1.db")


# In[7]:


cursor=db.cursor()


# In[9]:


cursor.execute("CREATE TABLE customers(customerNumber INT, customerName TEXT, contactLastName TEXT, contactFirstName TEXT,phone INT  PRIMARY KEY, addressLine1 TEXT, addressLine2 TEXT, city TEXT, state TEXT, postalCode INT, country TEXT, salesRepEmployeeNumber INT, creditLimit INT, foreign key (customerNumber) references customer(customerNumber))")


# In[ ]:


cursor.execute("INSERT INTO customers VALUES (111, "Shyam","Rathod","Shyam",9966554400,"RD Road, Malda",'East Kolkata','Kolkata','West Bengal',400003,"India",0056,80000)")


# In[10]:


cursor.execute("CREATE TABLE orders(orderNumber INT, orderDate INT, requiredDate INT, shippedDate INT, status TEXT, comments TEXT, customerNumber INT, foreign key(orderNumber) references ordersdetails(orderNumber))")


# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:




