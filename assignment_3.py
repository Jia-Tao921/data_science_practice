#!/usr/bin/env python
# coding: utf-8

# # Assignment \#3 the Olympic dataset
# 
# #### Features description
# - *City*: City
# - *Edition*: Year
# - *Sport*: Sport
# - *Discipline*: Discipline
# - *Athlete*: Athlete's last name and first name (generally separated by a comma and a space)
# - *NOC*: Country, National Olympic Committee, ISO 3166-1 alpha-3
# - *Gender*: Men, Women
# - *Event*: Event
# - *Event_gender*: Event gender (F = Women, M = Men, X = NA)
# - *Medal*: Metal of medal (Bronze, Silver, Gold)

# In[1]:


# usual import and options
import pandas as pd
pd.set_option("display.max_rows", 16)


# ### Loading the dataset
# 
# **file**: `'Summer Olympic medallists 1896 to 2008 - ALL MEDALISTS.txt'`
# 
# **separator**: tab: `\t`

# In[2]:


# LOADING THE DATASET
# DO NOT CHANGE THIS CELL FOR GRADING
# THE DATASET SHOULD BE ALONG WITH THE NOTEBOOK AND THE PYTHON FILE

df = pd.read_csv('Summer Olympic medallists 1896 to 2008 - ALL MEDALISTS.txt', sep='\t')
df.head()


#  Questions
# 
# 1) How many different cities have organized Olympic games?
# 
# 2) How many different editions of Olympic games are in the dataset?
# 
# 3) How many cities have organized more than one edition of Olympic games?
# 
# 4) Which sport distributed the most medals?
# 
# 5) Which discipline distributed the most medals?
# 
# 6) How many gold medals have been distributed?
# 
# 7) Which edition distributed the most silver medals?
# 
# 8) In how many different disciplines did men received medals (°)?
# 
# 9) In how many different disciplines did women received medals (°)?
# 
# 10) How many disciplines are dedicated to women (°)?
# 
# 11) How many countries have won a medal with an event gender equal to 'X'?
# 
# 12) How many countries have won a gold medal with an event gender equal to 'X'?
# 
# 13) How many different countries have an athlete whose surname is 'SCHMIDT'?
# 
# 14) How many different sports have the word 'ball' in their name?
# 
# 15) How many Bronze or Silver medals have been won by any athlete whose surname is 'KIM'?
# 
# 16) How many different events are in the dataset?
# 
# 17) How many different events including numbers in their description are in the dataset?
# 
# 18) Which athlete has participated in the most editions?
# 
# 19) How many sports have the same number of Gold, Silver and Bronze medals?
# 
# 20) How many athletes have strictly more Gold medals than Silver and more Silver medals than Bronze?
# 
# 21) Which country has won at least one medal in each olympic edition?
# 
# 22) Add a column named 'Score' with 1 for Bronze, 2 for Silver and 3 for Gold medals. What is the total sum of scores?
# 
# 23) Which athlete has the largest sum of scores?
# 
# 24) Which woman athlete has the largest sum of scores?
# 
# 25) For how many countries the sum of men's scores is equal to the sum of women's scores?
# 
# 26) Add a column named 'Trial' with the concatenation of columns 'Discipline', 'Sport' and 'Event' separated by a space. How many different trials are in the dataset?
# 
# 27) Which edition has the largest number of different trials?
# 
# 28) Add a column 'First Name' with the first name of athletes. How many different first names are in the dataset?
# 
# 29) Which athlete's first name has the largest sum of scores?
# 
# 30) Which woman athlete's first name has the largest sum of scores (°)?
# 
# (°) Use the 'Gender' column.

# In[3]:


# 1) How many different cities have organized Olympic games?
def exercise_01():
    result = df["City"].nunique()
    return result

# run and check
exercise_01()


# In[4]:


# 2) How many different editions of Olympic games are in the dataset?
def exercise_02():
    result = df['Edition'].nunique()
    return result

# run and check
exercise_02()


# In[5]:


# 3) How many cities have organized more than one edition of Olympic games?

def exercise_03():
    result = df['Edition'].nunique()-df["City"].nunique()
    return result

# run and check
exercise_03()


# In[6]:


# 4) Which sport distributed the most medals?

def exercise_04():
    result =df['Sport'].value_counts().idxmax()
    return result

# run and check
exercise_04()


# In[7]:


# 5) Which discipline distributed the most medals?

def exercise_05():
    result = df['Discipline'].value_counts().idxmax()
    return result

# run and check
exercise_05()


# In[8]:


# 6) How many gold medals have been distributed?

def exercise_06():
    result = df.loc[df['Medal']=='Gold'].shape[0]
    return result

# run and check
exercise_06()


# In[9]:


# 7) Which edition distributed the most silver medals?

def exercise_07():
    result = df.loc[df['Medal']=='Silver','Edition'].value_counts().index[0]
    return result

# run and check
exercise_07()


# In[10]:


# 8) In how many different disciplines did men received medals (°)?

def exercise_08():
    result = df.loc[df['Gender']=='Men','Discipline'].nunique()
    return result

# run and check
exercise_08()


# In[11]:


# 9) In how many different disciplines did women received medals (°)?

def exercise_09():
    result = df.loc[df['Gender']=='Women','Discipline'].nunique()
    return result

# run and check
exercise_09()


# In[12]:


# 10) How many disciplines are dedicated to women (°)?

def exercise_10():
    result1 = df.loc[df['Gender']=='Men','Discipline'].nunique()
    result2=df['Discipline'] .nunique()
    result=result2-result1
    return result

# run and check
exercise_10()


# In[13]:


# 11) How many countries have won a medal with an event gender equal to 'X'?

def exercise_11():
    result = df.loc[df['Event_gender']=='X','NOC'].nunique()
    return result

# run and check
exercise_11()


# In[14]:


# 12) How many countries have won a gold medal with an event gender equal to 'X'?

def exercise_12():
    result = df.loc[(df['Event_gender']=='X')& (df['Medal']=='Gold'),'NOC'].nunique()
    return result

# run and check
exercise_12()


# In[15]:


# 13) How many different countries have an athlete whose surname is 'SCHMIDT'?

def exercise_13():
    df[['Athlete_sur','firstname']]=df['Athlete'].str.split(', ',n=1,expand=True)
    result = df.loc[df['Athlete_sur']=='SCHMIDT','NOC'].nunique()
    return result

# run and check
exercise_13()


# In[16]:


# 14) How many different sports have the word 'ball' in their name?

def exercise_14():
    result = df.loc[df['Sport'].str.contains('ball'),'Sport'].nunique()
    return result

# run and check
exercise_14()


# In[17]:


# 15) How many Bronze or Silver medals have been won by any athlete whose surname is 'KIM'?

def exercise_15():
    result = df.loc[(df['Athlete_sur']=='KIM')&(df['Medal']!='Gold'),'Medal'].count()
    return result

# run and check
exercise_15()


# In[18]:


# 16) How many different events are in the dataset?

def exercise_16():
    result = df['Event'].nunique()
    return result


# run and check
exercise_16()


# In[19]:


# 17) How many different events including numbers in their description are in the dataset?

def exercise_17():
   
    result = df.loc[df['Event'].str.contains('[\d]'),'Event'].nunique()
    return result


# run and check
exercise_17()


# In[20]:


# 18) Which athlete has participated in the most editions?

def exercise_18():
    var = pd.crosstab(df['Edition'],df['Athlete'])
    result=(var!=0).sum().nlargest().index[0]
    return result


# run and check
exercise_18()


# In[21]:


# 19) How many sports distributed exactly the same number of Gold, Silver and Bronze medals?

def exercise_19():
    var=pd.crosstab(df["Sport"],df["Medal"])
    result= sum((var['Bronze']==var['Gold'])&(var['Gold']==var['Silver']))
        
    
    return result

# run and check
exercise_19()


# In[22]:


# 20) How many athletes received strictly more Gold medals than Silver and strictly more Silver medals than Bronze?

def exercise_20():
    var=pd.crosstab(df["Athlete"],df["Medal"])
    result = ((var['Gold']>var['Silver'])& (var['Silver']>var['Bronze'])).sum()
    return result

# run and check
exercise_20()


# In[23]:


# 21) Which country has won at least one medal in each olympic edition?

def exercise_21():
    var=pd.crosstab(df['Edition'],df['NOC'])
    result = (var!=0).sum().idxmax()
    return result

# run and check
exercise_21()


# In[24]:


# 22) What is the total sum of scores?

def exercise_22():
    var=pd.crosstab(df['Edition'],df['Medal'],margins=True)
    scores=var['Gold']*3+var['Silver']*2+var['Bronze']
    result = scores['All']
    return result

# run and check
exercise_22()


# In[25]:


# 23) Which athlete has the largest sum of scores?

def exercise_23():
    var = pd.crosstab(df['Athlete'],df['Medal'])
    scores=(var['Gold']*3+var['Silver']*2+var['Bronze']).idxmax()
    
    return scores

# run and check
exercise_23()


# In[45]:


# 24) Which woman athlete has the largest sum of scores (°)?

def exercise_24():
    df['score']=df['Medal']+'0'
    df['score']=df['score'].replace('Gold0',3).replace('Silver0',2).replace('Bronze0',1)
    var=df.pivot_table(values='score',index='Athlete',columns='Gender', aggfunc=len, fill_value=0)
    result = var['Women'].idxmax()
    return result

# run and check
exercise_24()


# In[49]:


# 25) For how many countries the sum of men' scores is equal to the sum of women' scores?

def exercise_25():
    var = df.pivot_table(values='score',
                            index='NOC',
                            columns='Gender',
                            aggfunc=sum,fill_value=0)
   
    result = sum(var['Men']==var['Women'])
    return result

# run and check
exercise_25()


# In[28]:


# 26) How many different trials are in the dataset?
#columns 'Discipline', 'Sport' and 'Event' separated by a space
def exercise_26():
    df['Trials']=df['Discipline']+' '+df['Sport']+' '+df['Event']
    result = df['Trials'].nunique()
    return result

# run and check
exercise_26()


# In[29]:


# 27) Which edition has the most different trials?

def exercise_27():
    var=pd.crosstab(df['Trials'],df['Edition'])
    result=(var!=0).sum().sort_values(ascending=False).idxmax()
    return result

# run and check
exercise_27()


# In[30]:


# 28) How many different first names are in the dataset?

def exercise_28():
    df[['firstname','middle']]=df['firstname'].str.split(',',n=1,expand=True).fillna(1)
    result = df['firstname'].nunique()
    return result

# run and check
exercise_28()


# In[31]:


# 29) Which athlete's first name has the largest sum of scores?

def exercise_29():
    var = pd.crosstab(df['firstname'],df['Medal'])
    scores=(var['Gold']*3+var['Silver']*2+var['Bronze']).idxmax()
    result =scores
    return result

# run and check
exercise_29()


# In[50]:


# 30) Which woman athlete's first name has the largest sum of scores (°)?

def exercise_30():
    var = df.pivot_table(values='score',
                            index='firstname',
                            columns='Gender',
                            aggfunc=sum,fill_value=0)
    
    return var['Women'].idxmax()

# run and check
exercise_30()

