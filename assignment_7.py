#!/usr/bin/env python
# coding: utf-8

# # Assignment \#7 the Sentiment140 dataset
# 
# The sentiment140 dataset contains 1,600,000 tweets extracted using the twitter api from April to June 2009. The tweets have been annotated (0 = negative, 4 = positive) and they can be used to detect sentiment.
# 
# Source: kaggle.com

# As the file is quite large (230MB), we use a subset of this dataset, where we selected only tweets containing the strings (not only isolated words) `"good"` or `"bad"`. The subset for this assignment contains 103,259 tweets:
# 
# - date: datetime of the tweet in the format: year-month-day hours:minutes:seconds
# - score: polarity of the tweet: 0=negative and 4=positive
# - user: user who produced the tweet
# - text: text of the tweet

# **Caution**: Questions asking to return a floating point number (ratio, mean, percentage) should round it to 1 decimal place:
# - Such questions are marked with `(°)`
# - For instance, if the variable `result` is a floating point number, e.g. `3.14159265359`
# - The functions should return `round(result, 1)` instead of `result`, e.g. `3.1`
# - Sommetimes, rounding a floating point number to 1 decimal place leads to a strange number such as `3.100000001`. This is a common outcome with floating point numbers representation and will not affect the grade.
# - Percentages should be returned as floating point numbers (not with the % mark).

# #### Questions
# 
# **A. In this part, we explore the time series aspect of the dataset**
# 
# 1) Pick up the datetime of the first row in the dataset and produce a string in the exact format `day/month/year`, example `"25/12/2021"`, using the `strftime()` method.
# 
# 2) Pick up the datetime of the last row in dataset and produce a string in the exact format `month day, year`, example `"Dec 25, 2021"`, using the `strftime()` method.
# 
# 3) How many days with at least one tweet do we have?
# 
# 4) What is the maximum number of tweets in a day?
# 
# 5) What is the minimum number of tweets in a day with at least one tweet?
# 
# 6) What is the average number of tweets in a day with at least one tweet (°)?
# 
# 7) If we consider only the hours of the day (0 to 23) where the tweets have been produced, at what hour do we have the minimum number of tweets?
# 
# 8) If we consider only the hours of the day (0 to 23) where the tweets have been produced, at what hour do we have the maximum number of tweets?
# 
# 9) Who is the most active user in the dataset?
# 
# 10) What is the average number of tweets in a day produced by the most active user (°)?
# 
# 
# (°) Result of functions should be rounded to 1 decimal place.

# **B. In this part, we explore the textual aspect of the dataset**
# 
# 11) What is the mean score of all tweets (°)?
# 
# 12) What is the mean score of tweets containing the string `"good"` (°)?
# 
# 13) What is the mean score of tweets containing the string `"bad"` (°)?
# 
# 14) What is the mean score of tweets issued by the most active user found in question 9 (°)?
# 
# 15) Which text is the most frequent one in all tweets?
# 
# 16) How many different users issued the most frequent tweet?
# 
# 17) What is the mean score of all tweets issued by those users (°)?
# 
# 18) In tweets, users are quoted with a string starting with an `@` and then containing possibly uppercase and lowercase letters, digits and underscore `_`. Which user is the most quoted one (the result should be a string starting with an `@`)?
# 
# 19) How many different users issued at least a tweet quoting the most quoted user?
# 
# 20) What is the mean score of tweets quoting the most quoted user (°)?
# 
# (°) Result of functions should be rounded to 1 decimal place.

# **Important import**
# 
# The cell below imports only the `pandas` module.
# 
# To achieve this assignment, you will need to import other modules. In order to avoid runtime errors when grading please import below the supplementary modules that you need.
# 
# Do not import the `locale` module. All written ouputs are supposed to be in English.

# In[199]:


# import
import pandas as pd

# Import here the supplementary modules that you need
# import
import datetime
import pytz
from pytz import timezone
import re
from collections import Counter


# In[200]:


# loading the data
# the dates are parsed!
df = pd.read_csv('sample1600000.csv', parse_dates=['date'])
df.head()


# In[201]:


# Pick up the datetime of the first row in dataset and produce a string in the exact format "25/12/2021"
def exercise_01():
    result = df['date'][0].strftime('%d/%m/%Y')
    return result


# In[202]:


# run and check
exercise_01()


# In[203]:


# Pick up the datetime of the last row in the dataset and produce a string in the exact format "Dec 25, 2021"
def exercise_02():
    result = df['date'].iloc[-1].strftime('%B %d,%Y')
    return result


# In[204]:


# run and check
exercise_02()


# In[205]:


# How many days with at least one tweet do we have?
def exercise_03():
    df['just_date']=df['date'].dt.date
    result = df['just_date'].nunique()
    return result


# In[206]:


# run and check
exercise_03()


# In[207]:


# What is the maximum number of tweets in a day?
def exercise_04():
    result = df.groupby('just_date').size().max()
    return result


# In[208]:


# run and check
exercise_04()


# In[209]:


# What is the minimum number of tweets in a day with at least one tweet?
def exercise_05():
    result = df.groupby('just_date').size().min()
    return result


# In[210]:


# run and check
exercise_05()


# In[211]:


# What is the average number of tweets in a day with at least one tweet (°)?
def exercise_06():
    result = df.groupby('just_date').size().mean()
    return round(result,1)


# In[212]:


# run and check
exercise_06()


# In[213]:


# At what hour do we have the minimum number of tweets?
def exercise_07():
    df['just_hour']=df['date'].dt.hour
    result = df.groupby('just_hour').size().idxmin()
    return result


# In[214]:


# run and check
exercise_07()


# In[215]:


# At what hour do we have the maximum number of tweets?
def exercise_08():
    result = df.groupby('just_hour').size().idxmax()
    return result


# In[216]:


# run and check
exercise_08()


# In[217]:


# Who is the most active user in the dataset?
def exercise_09():
    result = df.groupby('user').size().idxmax()
    return result


# In[218]:


# run and check
exercise_09()


# In[219]:


# What is the average number of tweets in a day produced by the most active user (°)?
def exercise_10():
    result = df.loc[df['user']=='VioletsCRUK'].groupby('just_date').size().mean()
    return round(result,1)


# In[220]:


# run and check
exercise_10()


# In[221]:


# What is the mean score of all tweets (°)?
def exercise_11():
    result = df['score'].mean()
    return round(result,1)


# In[222]:


# run and check
exercise_11()


# In[223]:


# What is the mean score of tweets containing the string "good" (°)?
def exercise_12():
    result = df.loc[df['text'].str.contains('good'),'score'].mean()
    return round(result,1)


# In[224]:


# run and check
exercise_12()


# In[225]:


# What is the mean score of tweets containing the string "bad" (°)?
def exercise_13():
    result = df.loc[df['text'].str.contains('bad'),'score'].mean()
    return round(result,1)


# In[226]:


# run and check
exercise_13()


# In[227]:


# What is the mean score of tweets issued by the most active user found in question 9 (°)?
def exercise_14():
    result =df.loc[df['user']=='VioletsCRUK','score'].mean()
    return round(result,1)


# In[228]:


# run and check
exercise_14()


# In[245]:


# Which text is the most frequent one in all tweets?
def exercise_15():
    result = df['text'].value_counts().index[0]
    return result


# In[246]:


# run and check
exercise_15()


# In[247]:


# How many different users issued the most frequent tweet?
def exercise_16():
    result = df.loc[df['text']=="good morning ",'user'].nunique()
    return result


# In[248]:


# run and check
exercise_16()


# In[265]:


# What is the mean score of all tweets issued by those users (°)?
def exercise_17():
    users = (df.loc[df['text']=="good morning ",'user'].unique()).tolist()
    result = df.loc[df['user'].isin(users),'score'].mean()
    return round(result,1)


# In[266]:


# run and check
exercise_17()


# In[348]:


# Which user is the most quoted one (the result should be a string starting with an `@`)?
def exercise_18():
    quoted_user=df['text'].str.findall(r'^[@]+[A-Za-zÀ-ÿ0-9]+')
    
    result = quoted_user.value_counts().index[1]
    return result


# In[349]:


# run and check
exercise_18()


# In[335]:


# How many different users issued at least a tweet quoting the most quoted user?
def exercise_19():
    result = df.loc[df['text'].str.contains('@mileycyrus'),'user'].nunique()
    return result


# In[336]:


# run and check
exercise_19()


# In[339]:


# What is the mean score of tweets quoting the most quoted user (°)?
def exercise_20():
    result = df.loc[df['text'].str.contains('@mileycyrus'),'score'].mean()
    return round(result,1)


# In[340]:


# run and check
exercise_20()

