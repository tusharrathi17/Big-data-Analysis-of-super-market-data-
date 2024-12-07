#!/usr/bin/env python
# coding: utf-8

# In[1]:


#BIG DATA MINI PROJECT 


# In[2]:


import numpy as np 
import pandas as pd 


# In[3]:


import matplotlib.pyplot as plt # visualizing data
get_ipython().run_line_magic('matplotlib', 'inline')


# In[4]:


import seaborn as sns


# In[5]:


#here we have read or csv file  
df = pd.read_csv('C:\\Users\\HP\\OneDrive\\Desktop\\sales.csv')


# In[6]:


df.shape


# In[7]:


df.head()


# In[8]:


#gives information in the file 
df.info()


# In[9]:


#check for null values
pd.isnull(df).sum()


# In[10]:


# drop null values
df.dropna(inplace=True)


# In[11]:


# change data type
df['Unit price'] = df['Unit price'].astype('int')


# In[12]:


df['Unit price'].dtypes


# In[13]:


df.columns


# In[14]:


# describe() method returns description of the data in the DataFrame
df.describe()


# In[15]:


#GENDER
# plotting a bar chart for Gender and it's count

ax = sns.countplot(x = 'Gender',data = df)

for bars in ax.containers:
    ax.bar_label(bars)


# In[16]:


# plotting a bar chart for gender vs Unit price

sales_gen = df.groupby(['Gender'], as_index=False)['Unit price'].sum().sort_values(by='Unit price', ascending=False)

sns.barplot(x = 'Gender',y= 'Unit price' ,data = sales_gen)


# In[17]:


#graph for payment methods
ax = sns.countplot(data = df, x = 'Payment', hue = 'Gender')

for bars in ax.containers:
    ax.bar_label(bars)


# In[19]:


# total number of ratings from top 3 Cities

sales_state = df.groupby(['City'], as_index=False)['Rating'].sum().sort_values(by='Rating', ascending=False).head(10)

sns.set(rc={'figure.figsize':(15,2)})
sns.barplot(data = sales_state, x = 'City',y= 'Rating')


# In[21]:


city_name = 'Yangon'  
filtered_df = df[df['City'] == city_name]
filtered_df


# In[40]:


#graph for the product line
ax = sns.countplot(data = df, x = 'Product line')

sns.set(rc={'figure.figsize':(7,5)})
for bars in ax.containers:
    ax.bar_label(bars)


# In[43]:


#graph for product line nad its unit price 
sales_state = df.groupby(['Product line', 'Gender'], as_index=False)['Unit price'].sum().sort_values(by='Unit price', ascending=False)

sns.set(rc={'figure.figsize':(6,4)})
sns.barplot(data = sales_state, x = 'Product line',y= 'Unit price', hue='Gender')


# In[46]:


#graph for invoice id and gross income 
sales_state = df.groupby(['Invoice ID'], as_index=False)['gross income'].sum().sort_values(by='gross income', ascending=False).head(10)

sns.set(rc={'figure.figsize':(20,5)})
sns.barplot(data = sales_state, x = 'Invoice ID',y= 'gross income')


# In[ ]:




