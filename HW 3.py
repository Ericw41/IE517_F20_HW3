#!/usr/bin/env python
# coding: utf-8

# In[217]:


#EDA on the "High Yield Corporate Bond" dataset
import numpy as np
import pandas as pd
from pandas import DataFrame
import scipy.stats
import matplotlib.pyplot as plt
import seaborn as sns
import pylab
import requests
import sys


# In[218]:


#Insert csv data
df = pd.read_csv(r"C:\Users\weizi\Desktop\IE 517\hw 3\HY.csv")
df.head#display the first/last 5 rows
df


# In[219]:


#find out number of rows, columns, elements
number_of_rows = len(df)
print(number_of_rows)

print(len(df.columns))

print(df.size)


# In[220]:


#selecting the weekly_mean_ntrades column as a series
weekly_mean_ntrades = df['weekly_mean_ntrades']

#plot the QQ plot for weekly_mean_ntrades
scipy.stats.probplot(df['weekly_mean_ntrades'], dist = 'norm', plot = pylab)

pylab.show()


# In[221]:


#selecting the weekly_median_ntrades column as a series
weekly_median_ntrades = df['weekly_median_ntrades']

#plot the QQ plot for weekly_mean_ntrades, one can see that there is a high outlier
scipy.stats.probplot(df['weekly_median_ntrades'], dist = 'norm', plot = pylab)

plt.show()


# In[222]:


#Selecting the 'weekly_median_ntrades' and 'weekly_median_volume' as attributes to create a scatterplot
_=plt.plot(df['weekly_median_ntrades'],df['weekly_median_volume'], marker='.', linestyle='none')
plt.title('weekly_median_ntrades vs weekly_median_volume');
plt.xlabel('weekly_median_ntrades');
plt.ylabel('weekly_median_volume');
plt.show()


# In[223]:


#Selecting the 'weekly_median_ntrades' and 'bond_type' as attributes to create a scatterplot
_=plt.plot(df['weekly_median_ntrades'],df['bond_type'], marker='.', linestyle='none')
plt.title('weekly_median_ntrades vs bond_type');
plt.xlabel('weekly_median_ntrades');
plt.ylabel('bond_type');
plt.show()


# In[224]:


#Selecting the weekly_mean_volume,weekly_median_volume,weekly_max_volume,
#weekly_min_volume, weekly_mean_ntrades as attributes to create a heatmap

data = pd.DataFrame(df.iloc[0:70, [32,33,34,35,36]].corr())


sns.heatmap(data)
plt.show()



# In[ ]:





# In[225]:


#Selecting the 'bond_type' as attribute to create a histogram

_= plt.hist(df['bond_type'], color = 'red')
_=plt.title('Histogram of the types of bonds')
_=plt.xlabel('Types of bonds')
_=plt.ylabel('Number of bonds')
plt.show()


# In[226]:


#Selecting the 'weekly_median_ntrades' as attribute to create a histogram

_= plt.hist(df['weekly_median_ntrades'], color = 'purple')
_=plt.title('Histogram of the weekly median number of trades')
_=plt.xlabel('weekly median number of trades')
_=plt.ylabel('Number of dates')
plt.show()


# In[227]:


#Selecting the 'weekly_median_ntrades', 'weekly_mean_ntrades' as attributes to create two boxplots
plt.boxplot(df[['weekly_median_ntrades','weekly_mean_ntrades']].values)
_ = plt.xlabel('Weekly mediann # of trades (plot 1), and Weekly mean # of trades (plot 2) ')


plt.show()


# In[228]:


print("My name is {Zicheng Wei}")
print("My NetID is: {wei41}")
print("I hereby certify that I have read the University policy on Academic Integrity and that I am not in violation.")


# In[ ]:





# In[ ]:





# In[ ]:




