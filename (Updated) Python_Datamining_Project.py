#!/usr/bin/env python
# coding: utf-8

# # Importing Our Modules:

# In[1]:


import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sb
import csv


# 
# # Loading Our Data:

# In[2]:


data = pd.read_csv("D:\Semester 2\MS5114 - Advanced Programming for Business Analytics\Final Project\Walmart(1).csv", parse_dates = ["Date"])


# # The Data at a Glance:

# In[3]:


data.head()


# In[4]:


data["Weekly_Sales"].plot(kind = "line", figsize = (20,10))


# In[5]:


data["Weekly_Sales"].plot(kind = "box", vert = False, figsize = (20,10))


# In[6]:


data["Weekly_Sales"].plot(kind = "density", figsize = (20,10))


# In[7]:


corr = data.corr()
fig = plt.figure(figsize = (20,10))
plt.matshow(corr, cmap= "RdBu", fignum = fig.number)
plt.xticks(range(len(corr.columns)), corr.columns, rotation = "vertical")
plt.yticks(range(len(corr.columns)), corr.columns);


# # Sales by week:

# In[8]:


sales_total = (data.resample('D', on='Date').sum().reset_index())

sales_total['Weekly_Sales'] = sales_total['Weekly_Sales'] // 1_000_000

sales_total.plot(x='Date', y='Weekly_Sales', figsize=(20, 10), ylabel='Weekly Sales in million USD')


# # Sales by store:

# In[10]:


sales_by_store = data.groupby(["Store"])[["Weekly_Sales"]].sum()
sales_by_store = sales_by_store // 1_000_000

sales_by_store.plot(kind="bar", figsize=(20, 10), ylabel= "Total Sales in million USD")


# In[11]:


print(sales_by_store)
sales_by_store.describe()


# # Which store has the most sales in 2011?

# In[12]:


print(sales_by_store.idxmax())


# # What were the total sales for that store?

# In[14]:


print(sales_by_store.max())


# # Backup Code

# In[ ]:


sales_total = (data.resample('D', on='Date').sum().reset_index())

sales_total.plot(x='Date', y='Weekly_Sales',figsize=(20, 10))


# In[ ]:


sales_by_store = data.groupby("Store")["Weekly_Sales"].sum()
sales_by_store.plot(kind = "bar", figsize = (20,10))

