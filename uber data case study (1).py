#!/usr/bin/env python
# coding: utf-8

# # Uber Data Case Study

# In[1]:


import pandas as pd 
import numpy as np 


# In[2]:


df = pd.read_csv('My Uber Drives - 2016 (1).csv')
df.head()


# Write a code to get the top 7 rows of the dataset.
# 

# In[3]:


df.head(7)


# Write a code to get the last 5 rows of the dataset.
# 

# In[4]:


df.tail(5)


# Get the total number of rows and columns in the dataset.
# 

# In[5]:


print(df.shape[0])# for rows
print(df.shape[1])#for cloumns


# Get the total number of elements in the dataset (Use size function)

# In[6]:


df.size


# Write a code to get the total number of NULL values across every column in the
# dataset.

# In[7]:


df.isnull().sum()


# Write a code to get the total number of Non-NULL values across every column in the
# dataset.

# In[8]:


df.notnull().sum()


#  Write a code to get the entries having NULL values in the 'Purpose' column.

# In[9]:


df[df['PURPOSE*'].isnull()]


# Write a code to get the entries having Non-NULL values in the 'Purpose' column
# using the Tilde (~) operator.
# 

# In[10]:


df[~df['PURPOSE*'].isnull()]


# Write a code to get Non-NULL entries in the PURPOSE column.
# 

# In[11]:


df[df['PURPOSE*'].notnull()]


# Write a code to remove the * in every column name using the rename function.

# In[12]:


df.rename(columns = {'START_DATE*':'START_DATE', 'END_DATE*':'END_DATE', 
                     'CATEGORY*':'CATEGORY', 'START*':'START', 'STOP*':'STOP', 'MILES*':'MILES', 'PURPOSE*':'PURPOSE'}, inplace=True)


# In[13]:


df.columns


# Write a code to remove the * in every column name using the str.replace() function.

# In[14]:


df.columns.str.replace("*","")


# Write a code to remove the * in every column name using the lambda function.
# 

# In[15]:


df.rename(columns = lambda x :x.replace("*","")).columns


#  Get the entries in the data where the START location is 'Fort Pierce'.
# 

# In[16]:


df[df['START']=='Fort Pierce'].head(2)


# Get the entries in the data where the STOP location is 'Fort Pierce'.
# 

# In[17]:


df[df['STOP']=='Fort Pierce'].head(2)


# In[18]:


Write a code to sort the entries in the data in descending order of the 'MILES'
column.


# In[ ]:


df.sort_values('MILES', ascending = False).head(2)


# Write a code to drop all the rows where there are NULL values in the STOP column.

# In[ ]:


df.dropna(subset=['STOP'],inplace=True)
df.head()


# Use describe() function to get the Statistical Properties about the numerical columns
# in the data.
# 

# In[ ]:


df.describe()


# Create a report in an html file using pandas profiling

# In[ ]:


get_ipython().system(' pip install pandas_profiling --quite')


# In[ ]:


import pandas_profiling as pp


# In[ ]:


report = pp.ProfileReport(df)


# In[ ]:


report.to_file('ubercasestudy.html')


# In[ ]:





# In[ ]:





# Get the unique and total number of unique values in the START and STOP column of
# the data.
# 

# In[ ]:


df[['START','STOP']].nunique()


# In[ ]:


start_unique = df['START'].unique()
stop_unique = df['STOP'].unique()


# In[ ]:


count_start = len(start_unique)
count_stop = len(stop_unique)


# In[ ]:


print("no of unique value in start column:",count_start)
print("no of unique value in start column:",count_stop)


# Get the rides where we have the same START and STOP locations using a
# comparison operator (==).
# 

# In[ ]:


a = df[df['START'] == df['STOP']]


# Get the rides where we have the same START and STOP locations using a
# membership operator.
# 

# In[ ]:


df.loc[df['START'] == df['STOP']].head()


# Use value_counts() function to demonstrate the proportion of different categorical
# values in the data.
# 

# In[ ]:


df['START'].value_counts()


# Get the number of rides where START and STOP locations are the same

# In[ ]:


df[df['START'] == df['STOP']].shape[0]


# Find the favorite starting point according the the total number of MILES covered.
# (Use groupby function).
# 
# 

# In[ ]:


tot_mile = df.groupby('START')['MILES'].sum()
highst_mile = tot_mile.sort_values(ascending=False)
favorite_starting_point = highst_mile.index[0]
print(f"favorite starting point is {favorite_starting_point}.")


# Check the data types of all the columns in the dataset.

# In[ ]:


df.dtypes


# Drop the 'unknown location' value from START and STOP column.

# In[20]:


newUber = df[df['STOP'] != 'Unknown Location'].copy()


# In[21]:


newUber = newUber[newUber['START'] != 'Unknown Location'].copy()


# In[22]:


sum(newUber['STOP'] =='Unknown location')


# In[23]:


sum(newUber['START'] =='Unknown location')


# In[36]:


df.head(2)


# In[ ]:


Find the most popular START-STOP pair according to the total number of rides
covered.


# In[35]:


newUber.groupby(['START','STOP']).size().sort_values(ascending=False).reset_index(name='count')


# Convert the datatypes of START_DATE and END_DATE columns to datetime.

# In[52]:


df = df[df['START_DATE']!='Totals'].copy()


# In[53]:


df['START_DATE']=pd.to_datetime(df['START_DATE'])


# In[55]:


df['END_DATE']=pd.to_datetime(df['END_DATE'])


# Extract the month from START_DATE and try to get the proportion of rides of
# different months.

# In[63]:


df['month']=df['START_DATE'].dt.month


# In[65]:


proportion = df['month'].value_counts(normalize=True)
proportion


# In[68]:


df.head(2)


# Find the average distance covered each month.

# In[70]:


pd.pivot_table(df, values = 'MILES', index = 'month').reset_index()


# Extract the day from the START_DATE column.

# In[110]:


df['day']= df['START_DATE'].dt.day # for day no 


# In[113]:


df['day']= df['START_DATE'].dt.day_name()# for day name


# In[114]:


df.head(2)


# Find the total miles covered per category per purpose.

# In[117]:


pd.pivot_table(df, values = 'MILES', index = ['CATEGORY','PURPOSE']).sort_values(by = 'MILES', ascending = False).reset_index()


# Find the percentage of Business Miles covered and Personal mIles covered.

# In[84]:


df['CATEGORY'].unique()


# In[120]:


total_miles = df.groupby('CATEGORY')['MILES'].sum()
total_miles


# In[98]:


buss_tot = (total_miles['Business']/total_miles.sum())*100

print('percentage of business miles is',buss_tot)


# In[99]:


pers_tot = (total_miles['Personal']/total_miles.sum())*100

print('percentage of personal miles is',pers_tot)


# In[ ]:




