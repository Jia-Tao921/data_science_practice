#!/usr/bin/env python
# coding: utf-8

# # Assignment \#6 the Gapminder dataset 2/2

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
# - The 7 following questions in parts A and B rely on materials that will be studied in the notebook `python_data_science_1`: 1, 4 and 7 to 11
# - The 8 following questions in parts A and B rely on materials that will be studied in the notebook `python_data_science_2`: 2 to 3, 5 to 6 and 13 to 15

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
# **A. In this part, we will only deal with the data for year 2018 (cont.)**
# 
# - Perform an inner join between the life expectancy and the total population `DataFrame` objects, then an inner join with the result and the country `DataFrame` object. Remember that overlapping columns names are renamed automatically with the `_x` and `_y` suffixes in the left and right side:
# 
# 1) What is the weighted average life expectancy in 2018 (°) (+)?
# 
# 2) What is the largest weighted average life expectancy by region in 2018 (°) (+)?
# 
# 3) What is the smallest weighted average life expectancy by region in 2018 (°) (+)?
# 
# - Perform an inner join between the income per person and the total population `DataFrame` objects, then an inner join with the result and the country `DataFrame` objects. Remember that overlapping columns are renamed automatically with the `_x` and `_y` suffixes in the left and right side:
# 
# 4) What is the weighted average income per person in 2018 (°) (++)?
# 
# 5) Which region has the largest weighted average income per person in 2018 (++)?
# 
# 6) Which region has the smallest weighted average income per person in 2018 (++)?
# 
# (+) The *weighted average life expectancy* is computed with the sum of the products of life expectancy by total population of each country divided by the sum of total population of each country. It can be computed for all countries in the world or for all countries in each region.
# 
# Hint: weighted average life expectancy $= \frac{\displaystyle\sum_{i} life_{i} \times pop_{i}}{\displaystyle\sum_{i} pop_{i}}$
# 
# (++) The *weighted average income per person* is computed with the sum of the products of income per person by total population of each country divided by the sum of total population of each country. It can be computed for all countries in the world or for all countries in each region.
# 
# Hint: weighted average income per person $= \frac{\displaystyle\sum_{i} income_{i} \times pop_{i}}{\displaystyle\sum_{i} pop_{i}}$
# 
# (°) Result of functions should be rounded to 1 decimal place.

# **B. In this part, we deal with data for all years**
# 
# 7) Which country has the smallest mean life expectancy accross years?
# 
# 8) Which country has the smallest mean income per person accross years?
# 
# 9) Compute the correlation of total population between all countries accross years. Which country has the highest mean correlation with the other ones? 
# 
# 10) Compute the correlation of life expectancy between all countries accross years. Which country has the highest mean correlation of life expectancy with the other ones? 
# 
# 11) Compute the correlation of income per person between all countries accross years. Which country has the highest mean correlation of income per person with the other ones?
# 
# 12) Perform a wide to long format transformation of the total population `DataFrame` object by using the `melt()` function. What is the length of the new `DataFrame` object for total population?
# 
# 13) Perform a wide to long format transformation of the life expectancy `DataFrame` object by using the `melt()` function. What is the length of the new `DataFrame` object for life expectancy?
# 
# 14) Perform a wide to long format transformation of the income per person `DataFrame` object by using the `melt()` function. What is the length of the new `DataFrame` object for income per person?
# 
# 15) Perform 3 wide to long format transformations of the total population, life expectancy and income per person `DataFrame` objects by using the `melt()` function. Then perform an inner join of the 2 first `DataFrame` objects on both `geo` and `Year` by using the `merge()` function. Then perform another inner join of this `DataFrame` object and the third one. You should obtain a final `DataFrame` object with 5 columns: `geo`, `Year`, `Total Population`, `Life Expectancy` and `Income Per Person`. Remove lines with `NA` . What is the length of the final `DataFrame` object obtained?

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


# What is the weighted average life expectancy in 2018 (°)?

df1= pd.merge(df_life,df_population,on='geo',how='inner')
df=pd.merge(df_country,df1)
def exercise_01(group):
   
    result = np.sum(group['2018_x']*group['2018_y'])/np.sum(group['2018_y'])
    return round(result,1)


# In[4]:


# run and check
exercise_01(df)


# In[5]:


# What is the largest weighted average life expectancy by region in 2018 (°)?
def exercise_02():
    result = df.groupby('region').apply(exercise_01).max()
    return result


# In[6]:


# run and check
exercise_02()


# In[7]:


# What is the smallest weighted average life expectancy by region in 2018 (°)?
def exercise_03():
    result = df.groupby('region').apply(exercise_01).min()
    return result


# In[8]:


# run and check
exercise_03()


# In[9]:


# What is the weighted average income per person in 2018 (°)?
df2=pd.merge(df_income,df_population,on='geo',how='inner')
df_waipp=pd.merge(df_country,df2)
def exercise_04(group):
    result = np.sum(group['2018_x']*group['2018_y'])/np.sum(group['2018_y'])
    return round(result,1)


# In[10]:


# run and check
exercise_04(df_waipp)


# In[11]:


# Which region has the largest weighted average income per person in 2018?
def exercise_05():
    result = df_waipp.groupby('region').apply(exercise_04).idxmax()
    return result


# In[12]:


# run and check
exercise_05()


# In[13]:


# Which region has the smallest weighted average income per person in 2018?
def exercise_06():
    result = df_waipp.groupby('region').apply(exercise_04).idxmin()
    return result


# In[14]:


# run and check
exercise_06()


# In[15]:


# Which country has the smallest average life expectancy accross years?
def exercise_07():
    df3=df_life
    df3['avg']=df3.min(axis=1)
    result = df3.loc[df3['avg'].idxmin(),'geo']
    return result


# In[16]:


# run and check
exercise_07()


# In[17]:


# Which country has the smallest average income per person accross years?
def exercise_08():
    df4=df_income
    df4['avg']=df4.min(axis=1)
    result = df4.loc[df4['avg'].idxmin(),'geo']
    return result


# In[18]:


# run and check
exercise_08()


# In[19]:


# Which country has the highest mean correlation of total population with other countries? 
def exercise_09():
    df5=df_population
    df5=df5.set_index('geo').T
    
    result = df5.corr().mean().idxmax()
    return result


# In[20]:


# run and check
exercise_09()


# In[21]:


# Which country has the highest mean correlation of life expectancy with other countries? 
def exercise_10():
    df6=df_life
    df6=df6.set_index('geo').T
    result = df6.corr().mean().idxmax()
    return result


# In[22]:


# run and check
exercise_10()


# In[23]:


# Which country has the highest mean correlation of income per person with other countries? 
def exercise_11():
    df7=df_income
    df7=df7.set_index('geo').T
    result = df7.corr().mean().idxmax()
    return result


# In[24]:


# run and check
exercise_11()


# In[25]:


# What is the length of the new DataFrame object for total population?
def exercise_12():
    df_population_long=df_population.melt(id_vars='geo')
    result = df_population_long.shape[0]
    return result


# In[26]:


# run and check
exercise_12()


# In[27]:


# What is the length of the new DataFrame object for life expectancy?
def exercise_13():
    df_life_long=df_life.melt(id_vars='geo')
    result = df_life_long.shape[0]
    return result


# In[28]:


# run and check
exercise_13()


# In[29]:


# What is the length of the new DataFrame object for income per person?

def exercise_14():
    df_income_long=df_income.melt(id_vars='geo')
    result = df_income_long.shape[0]
    return result


# In[30]:


# run and check
exercise_14()


# In[31]:


# What is the length of the DataFrame object merging total population, life expectancy and income per person in a long format?
def exercise_15():
    df_population_long=df_population.melt(id_vars='geo')
    df_life_long=df_life.melt(id_vars='geo')
    df_income_long=df_income.melt(id_vars='geo')
    df8=pd.merge(left=df_population_long,right=df_life_long,on=['geo','variable'],how='inner')
    df_final=df8.merge(df_income_long,on=['geo','variable'],how='inner')
    df_final=df_final.dropna()
    result = df_final.shape[0]
    return result


# In[32]:


# run and check
exercise_15()


# In[ ]:




