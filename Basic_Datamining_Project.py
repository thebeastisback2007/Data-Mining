#!/usr/bin/env python
# coding: utf-8

# # Importing our Modules:

# In[ ]:


import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import sklearn as sk
import csv


# # Loading Our Data:
# 

# In[102]:


data = pd.read_csv("D:\Semester 2\MS5114 - Advanced Programming for Business Analytics\Final Project\Walmart.csv")


# # The Data at a Glance:
# 

# In[103]:


data.head()


# In[ ]:





# In[ ]:





# 

# In[ ]:





# In[110]:


data.plot.line(y ="Weekly_Sales", x = "Date", figsize = (20,10))


# In[98]:


data["Weekly_Sales"].plot(kind = "box", vert = False, figsize = (20,10))


# In[99]:


data["Weekly_Sales"].plot(kind = "density", figsize = (20,10))


# In[100]:


data["Weekly_Sales"].plot(kind = "line", figsize = (20,10))
#but no date ??


# In[101]:


corr = data.corr()


# In[ ]:


fig = plt.figure(figsize = (20,10))
plt.matshow(corr, cmap= "RdBu", fignum = fig.number)
plt.xticks(range(len(corr.columns)), corr.columns, rotation = "vertical")
plt.yticks(range(len(corr.columns)), corr.columns);


# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:




