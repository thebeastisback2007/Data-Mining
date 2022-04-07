#!/usr/bin/env python
# coding: utf-8

# # Importing our Modules:

# In[274]:


import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sb
import csv


# # Loading Our Data:
# 

# In[275]:


data = pd.read_csv("D:\Semester 2\MS5114 - Advanced Programming for Business Analytics\Final Project\Walmart.csv", parse_dates = ["Date"])



# # The Data at a Glance:
# 

# In[276]:


data.head()


# In[277]:


data["Weekly_Sales"].plot(kind = "line", figsize = (20,10))
#but no date ??


# In[278]:


data.plot.line(y ="Weekly_Sales", x = "Date", figsize = (20,5))


# In[279]:


data["Weekly_Sales"].plot(kind = "box", vert = False, figsize = (20,10))
#same issue. Weekly sales do not show true value.


# In[280]:


data["Weekly_Sales"].plot(kind = "density", figsize = (20,10))
#same issue. Weekly sales do not show true value.


# In[281]:


corr = data.corr()


# In[282]:


fig = plt.figure(figsize = (20,10))
plt.matshow(corr, cmap= "RdBu", fignum = fig.number)
plt.xticks(range(len(corr.columns)), corr.columns, rotation = "vertical")
plt.yticks(range(len(corr.columns)), corr.columns);


# # Sales by week:

# In[283]:


sales_total = (data.resample('D', on='Date').sum().reset_index())

sales_total['Weekly_Sales'] = sales_total['Weekly_Sales'] // 1_000_000

sales_total.plot(x='Date', y='Weekly_Sales', figsize=(20, 10), ylabel='Weekly Sales in million USD')


# # Sales by store:

# In[284]:


sales_by_store = data.groupby("Store")["Weekly_Sales"].sum()
sales_by_store = sales_by_store // 1_000_000

sales_by_store.plot(kind="bar", figsize=(20, 10), ylabel= "Total Sales in million USD")


# # Backup Code

# In[ ]:


sales_total = (data.resample('D', on='Date').sum().reset_index())

sales_total.plot(x='Date', y='Weekly_Sales',figsize=(20, 10))


# In[ ]:


sales_by_store = data.groupby("Store")["Weekly_Sales"].sum()
sales_by_store.plot(kind = "bar", figsize = (20,10))

