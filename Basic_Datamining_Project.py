#!/usr/bin/env python
# coding: utf-8

# # Importing our Modules:

# In[126]:


import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sb
import csv


# # Loading Our Data:
# 

# In[102]:


data = pd.read_csv("D:\Semester 2\MS5114 - Advanced Programming for Business Analytics\Final Project\Walmart.csv")


# # The Data at a Glance:
# 

# In[103]:


data.head()


# In[148]:


data["Weekly_Sales"].plot(kind = "line", figsize = (20,10))
#but no date ??


# In[147]:


data.plot.line(y ="Weekly_Sales", x = "Date", figsize = (20,5))


# In[116]:


data["Weekly_Sales"].plot(kind = "box", vert = False, figsize = (20,10))
#same issue. Weekly sales do not show true value.


# In[117]:


data["Weekly_Sales"].plot(kind = "density", figsize = (20,10))
#same issue. Weekly sales do not show true value.


# In[101]:


corr = data.corr()


# In[143]:


fig = plt.figure(figsize = (20,10))
plt.matshow(corr, cmap= "RdBu", fignum = fig.number)
plt.xticks(range(len(corr.columns)), corr.columns, rotation = "vertical")
plt.yticks(range(len(corr.columns)), corr.columns);


# In[ ]:





# In[140]:


total_sales = (data.resample(, on = "Date").sum().resetindex())
total_sales.plot(x = "Date", y = "Weekly Sales")


# In[142]:


sales_by_store = sb.relplot(data = data, x = "Date", y = "Weekly_Sales", hue = "Store", kind = "bar")


# In[ ]:





# In[ ]:




