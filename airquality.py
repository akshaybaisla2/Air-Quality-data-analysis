#!/usr/bin/env python
# coding: utf-8

# In[1]:


#importing libraries
import seaborn as sns
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd


# In[4]:


dataset = pd.read_csv('data.csv',encoding='latin1')
df = dataset.copy()


# In[6]:


df.head()  


# In[7]:


df.tail()


# In[8]:


df.info()


# In[9]:


df.isnull().sum()


# In[10]:


df['agency'].value_counts()


# In[11]:


df['type'].value_counts()


# In[12]:


#deleting all values which have null in type attribute
df = df.dropna(axis = 0, subset = ['type'])
# deleting all values which are null in location attribute
df = df.dropna(axis = 0, subset = ['location'])
#deleting all null values in so2 attribute
df = df.dropna(axis = 0, subset = ['so2'])


# In[13]:


df.isnull().sum()


# In[14]:


#not interested in agency
del df['agency']
del df['location_monitoring_station']
del df['stn_code']
del df['sampling_date']


# In[15]:


#dataset after deleting the above columns
df.head()


# In[16]:


#changing type to only 3 categories
a = list(df['type'])
for i in range(0, len(df)):
    if str(a[i][0]) == 'R' and a[i][1] == 'e':
        a[i] = 'Residential'
    elif str(a[i][0]) == 'I':
        a[i] = 'Industrial'
    else:
        a[i] = 'Other'
    
df['type'] = a
df['type'].value_counts()


# In[17]:


#how many observations belong to each location
sns.catplot(x = "type", kind = "count", palette = "ch: 0.25", data = df)


# In[18]:


#bar plot of so2 vs state - desc order
df[['so2', 'state']].groupby(['state']).median().sort_values("so2", ascending = False).plot.bar()


# In[19]:


# bar plot of no2 vs state - desc order
df[['no2', 'state']].groupby(['state']).median().sort_values("no2", ascending = False).plot.bar(color = 'r')


# In[20]:


# rspm = PM10
df[['rspm', 'state']].groupby(['state']).median().sort_values("rspm", ascending = False).plot.bar(color = 'r')


# In[21]:


# spm
df[['spm', 'state']].groupby(['state']).median().sort_values("spm", ascending = False).plot.bar(color = 'r')


# In[22]:


# spm
df[['pm2_5', 'state']].groupby(['state']).median().sort_values("pm2_5", ascending = False).plot.bar(color = 'r')


# In[23]:


#Scatter plots of all columns
sns.set()
cols = ['so2', 'no2', 'rspm', 'spm', 'pm2_5']
sns.pairplot(df[cols], size = 2.5)
plt.show()


# In[24]:


#Correlation matrix
corrmat = df.corr()
f, ax = plt.subplots(figsize = (15, 10))
sns.heatmap(corrmat, vmax = 1, square = True, annot = True)


# In[52]:


# Creating an year column
df['date'] = pd.to_datetime(df['date'], format = '%Y/%m/%d')
df['year'] = df['date'].dt.year # year
df['year'] = df['year'].fillna(0.0).astype(int)
df = df[(df['year']>0)]


# In[53]:


df.head()


# In[54]:


# Heatmap Pivot with State as Row, Year as Col, No2 as Value
f, ax = plt.subplots(figsize = (10,10))
ax.set_title('{} by state and year'.format('so2'))
sns.heatmap(df.pivot_table('so2', index = 'state',
                columns = ['year'], aggfunc = 'median', margins=True),
                annot = True, cmap = 'YlGnBu', linewidths = 1, ax = ax, cbar_kws = {'label': 'Average taken Annually'})


# In[55]:


# Heatmap Pivot with State as Row, Year as Col, So2 as Value
f, ax = plt.subplots(figsize=(10,10))
ax.set_title('{} by state and year'.format('no2'))
sns.heatmap(df.pivot_table('no2', index='state',
                columns=['year'],aggfunc='median',margins=True),
                annot = True, cmap = "YlGnBu", linewidths = 1, ax = ax,cbar_kws = {'label': 'Annual Average'})


# In[57]:


# bar plot of no2 vs location - desc order - first 10
df[['no2', 'location']].groupby(['location']).median().sort_values("no2", ascending = False).head(10).plot.bar(color = 'g')


# In[58]:


# bar plot of no2 vs location - desc order - last 10
df[['no2', 'location']].groupby(['location']).median().sort_values("no2", ascending = False).tail(10).plot.bar(color = 'g')


# In[59]:


# bar plot of so2 vs location - desc order
df[['so2', 'location']].groupby(['location']).median().sort_values("so2", ascending = False).head(10).plot.bar(color = 'y')


# In[61]:


# bar plot of no2 vs location - desc order
df[['so2', 'location']].groupby(['location']).median().sort_values("so2", ascending = False).tail(10).plot.bar(color = 'y')


# In[73]:


# rspm = PM10 - location wise - first 10
df[['rspm', 'location']].groupby(['location']).median().sort_values("rspm", ascending = False).head(10).plot.bar(color = 'r')


# In[72]:


# rspm = PM10 - location wise - last 20
df[['rspm', 'location']].groupby(['location']).median().sort_values("rspm", ascending = False).tail(20).plot.bar(color = 'r')


# In[69]:


# spm = PM10 - location wise - first 10
df[['spm', 'location']].groupby(['location']).median().sort_values("spm", ascending = False).head(10).plot.bar(color = 'r')


# In[66]:


# heatmap of rspm
f, ax = plt.subplots(figsize = (10,10))
ax.set_title('{} by state and year'.format('rspm'))
sns.heatmap(df.pivot_table('rspm', index='state',
                columns = ['year'], aggfunc = 'median', margins = True),
                annot = True, cmap = "YlGnBu", linewidths = 1, ax = ax, cbar_kws = {'label': 'Annual Average'})


# In[67]:


# heatmap of spm
f, ax = plt.subplots(figsize = (10, 10))
ax.set_title('{} by state and year'.format('spm'))
sns.heatmap(df.pivot_table('spm', index ='state',
                columns = ['year'], aggfunc = 'median', margins = True)
                , cmap = "YlGnBu", linewidths = 0.5, ax = ax, cbar_kws = {'label': 'Annual Average'})


# In[ ]:




