#!/usr/bin/env python
# coding: utf-8

# # Assignment \#5 the Gapminder dataset 1/2

# <div style="color:red">
#     <p><strong>Please read carefully all this introduction prior to get into the assignment.</strong></p>
# </div>

# There are 4 files for this assignment:
# - `population_total.csv`: total population, per country and per year (1800 to 2018)
# - `life_expectancy_years.csv`: life expectancy, per country and per year (1800 to 2018)
# - `income_per_person.csv`: income per person, per country and per year (1800 to 2018)
# - `countries_total.csv`: countries and regions (Asia, Europe, Africa, Oceania, Americas)
# 
# As usual the files must be along with your notebook and not in a dedicated folder.

# **Important note about the `geo` columns accross the `DataFrame` objects**: 
# - The 3 first files contain a field named `geo` with the names of the different countries. The last file contains also a column with the different countries. It is renamed to `geo` on load to ease the merges that would have to be performed (option `on='geo'` of `merge()` function or `join()` method).
# - The name of the countries have to be processed as is, without trying to homogenize them accross the different files.
# - In order to avoid discrepancies between results, all joins should be performed by using the `how='inner'`option.

# **Hint about the `python_data_science_1` and `python_data_science_2` notebooks**
# 
# - The 13 following questions rely on materials that will be studied in the notebook `python_data_science_1`: 1 to 13
# - The 2 following questions rely on materials that will be studied in the notebook `python_data_science_2`: 14 to 15

# **Caution**: Questions asking to return a floating point number (ratio, mean, percentage) should round it to 1 decimal place:
# - Such questions are marked with `(°)`
# - For instance, if the variable `result` is a floting point number, e.g. `3.14159265359`
# - The functions should return `round(result, 1)` instead of `result`, e.g. `3.1`
# - Percentages should be returned as floating point numbers (not with the % mark).

# <div style="color:red">
#     <p><strong>Last warning:</strong> Do not use the <code>inplace = True</code> option when doing any manipulations of a <code>DataFrame</code>:</p>
#     <ol>
#         <li>This option is no longer recommended.</li>
#         <li>This option might have side effects which may alter your results from one function to another.</li>
#     </ol>
# 
# <p>Therefore, instead of <code>df.any_method(inplace=True)</code>, use <code>df = df.any_method()</code></p>
# </div>

# #### Questions
# 
# **A. In this part, we will only deal with the data for year 2018**
# 
# - Total population by country in 2018:
# 
# 1) What is the sum of the total population in 2018?
# 
# 2) Which country has the largest total population in 2018?
# 
# 3) Which country has the smallest total population in 2018?
# 
# - Life expectation by country in 2018:
# 
# 4) What is the average life expectancy in 2018 (°)?
# 
# 5) What is the difference between the largest and the smallest life expectancy in 2018?
# 
# 6) Which country has the largest life expectancy in 2018?
# 
# 7) Which country has the smallest life expectancy in 2018?
# 
# 8) In 2018, below which life expectancy threshold a country is in the first decile (°)?
# 
# - Income per person by country in 2018:
# 
# 9) What is the average income per person in 2018 (°)?
# 
# 10) What is the ratio between the largest and the smallest income per person in 2018 (°)?
# 
# 11) Which country has the largest income per person in 2018?
# 
# 12) Which country has the smallest income per person in 2018?
# 
# 13) In 2018, above which income per person threshold a country is in the last decile (°)?
# 
# - Perform an inner join between the population and the country `DataFrame` objects:
# 
# 14) Which region has the largest total population in 2018?
# 
# 15) Which region has the smallest total population in 2018?
# 
# (°) Result of functions should be rounded to 1 decimal place.

# **Homework, out of the scope of the assignment, and not to submit**
# 
# - Homogenize the country names accross the different files and compare the results of the 15 exercises.
# 
# - Implement a graphics showing, for a given year, all countries positionned with their income per person on the `x` axis and their life expectancy on the `y` axis, and represented by their name, as well as, a circle which radius is linked to their total population and which color is linked to their region.

# In[1]:


# import
import numpy as np
import pandas as pd


# In[2]:


# loading the data
# DO NOT CHANGE THIS CELL

df_population = pd.read_csv('population_total.csv')
df_life = pd.read_csv('life_expectancy_years.csv')
df_income = pd.read_csv('income_per_person.csv')
df_country = pd.read_csv('countries_total.csv',
                           engine='python',
                           usecols=[0, 5],
                           header=0,
                           names=['geo', 'region'])


# In[3]:


# What is the sum of the total population in 2018?
def exercise_01():
    result = df_population["2018"].sum()
    return result


# In[4]:


# run and check
exercise_01()


# In[5]:


# Which country has the largest total population in 2018?
def exercise_02():
    result = df_population.loc[df_population["2018"].idxmax(),"geo"]
    return result


# In[6]:


# run and check
exercise_02()


# In[7]:


# Which country has the smallest total population in 2018?
def exercise_03():
    result = df_population.loc[df_population["2018"].idxmin(),"geo"]
    return result


# In[8]:


# run and check
exercise_03()


# In[9]:


# What is the average life expectancy in 2018 (°)?
def exercise_04():
    result = df_life["2018"].mean()
    return round(result,1)


# In[10]:


# run and check
exercise_04()


# In[11]:


# What is the difference between the largest and the smallest life expectancy in 2018?
def exercise_05():
    result = df_life["2018"].max()-df_life["2018"].min()
    return result


# In[12]:


# run and check
exercise_05()


# In[13]:


# Which country has the largest life expectancy in 2018?
def exercise_06():
    result = df_life.loc[df_life["2018"].idxmax(),"geo"]
    return result


# In[14]:


# run and check
exercise_06()


# In[15]:


# Which country has the smallest life expectancy in 2018?
def exercise_07():
    result = df_life.loc[df_life["2018"].idxmin(),"geo"]
    return result


# In[16]:


# run and check
exercise_07()


# In[165]:


# In 2018, below which life expectancy threshold a country is in the first decile (°)?
def exercise_08():
    df_life['decile']=pd.qcut(df_life['2018'],10,labels=False)
    result = df_life.loc[df_life['decile']==0,'2018'].max()
    
    return result


# In[166]:


# run and check
exercise_08()


# In[19]:


# What is the average income per person in 2018 (°)?
def exercise_09():
    result = df_income["2018"].mean()
    return round(result,1)


# In[20]:


# run and check
exercise_09()


# In[153]:


# What is the ratio between the largest and the smallest income per person in 2018
def exercise_10():
    result = df_income["2018"].max()/df_income["2018"].min()
    return round(result,1)


# In[154]:


# run and check
exercise_10()


# In[23]:


# Which country has the largest income per person in 2018?
def exercise_11():
    result = df_income.loc[df_income['2018'].idxmax(),'geo']
    return result


# In[24]:


# run and check
exercise_11()


# In[25]:


# Which country has the smallest income per person in 2018?
def exercise_12():
    result = df_income.loc[df_income['2018'].idxmin(),'geo']
    return result


# In[26]:


# run and check
exercise_12()


# In[151]:


# In 2018, above which income per person threshold a country is in the last decile (°)?
def exercise_13():
    var1,var2=pd.qcut(df_income['2018'],10,retbins=True)
    result = var2[9]
    return result


# In[152]:


# run and check
exercise_13()


# In[38]:


# Which region has the largest total population in 2018?
def exercise_14():
    df=pd.merge(df_population,df_country,
                on='geo',
                how='inner')
    result = df.loc[df['2018'].idxmax,'region']
    return result


# In[39]:


# run and check
exercise_14()


# In[137]:


# Which region has the smallest total population in 2018?
def exercise_15():
    df=pd.merge(df_population,df_country,
                on='geo',
                how='inner')
    var=df.pivot_table(index='region',values='2018',aggfunc='sum')
    result = var['2018'].idxmin()
    return result


# In[138]:


# run and check
exercise_15()

