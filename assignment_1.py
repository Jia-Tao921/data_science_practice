#!/usr/bin/env python
# coding: utf-8

# # Assignment \#1 - the Python beginner
# 
# 0) Create a function which computes the area of a rectangle given its height and width. Example: given 10 and 20, should return 200.
# 
# 1) Create a function which given 2 booleans computes the exclusive OR (should return True if one boolean is True and the other boolean is False; and False if both booleans are True or both booleans are False). Example: given True and False, should return True.
# 
# 2) Create a function which given hours, minutes and seconds computes the total number of seconds. Example: given 1 hour, 1 minute and 1 second, should return 3661.
# 
# 3) Create a function which given an integer, compute the sum of all integers between this integer and its double included. Example: given 3, should return 18 (3 + 4 + 5 + 6).
# 
# 4) Create a function which given a string produces a 2 characters string with the first character of the initial string and the last one. If the initial string is empty, it should return an empty string. Example: given 'Python', should return 'Pn'.
# 
# 5) Create a function which given a string returns the sentence: 'The reverse of X is Y!' where X is the initial string and Y is the reverse of the initial string. Example: given 'Paris', should return 'The reverse of Paris is siraP!'.
# 
# 6) Create a function which given a string returns True if the letters of the string are unique and False otherwise. Example: given 'Python', should return True; and given 'alphabet', should return False.
# 
# 7) Create a function which given a string returns True if the string is a palindrome (e.g., a word which has the property of reading the same forwards as it does backwards) and False otherwise. Example, given 'tattarrattat', should return True; and given 'alphabet', should return False.
# 
# 8) Create a function which given 3 numbers returns the one which is in the middle. Example: given 9, 5 and 6, should return 6.
# 
# 9) Create a function which given a list of strings produces a string with the first character of each non empty string of the list. Example: given ['Hi', 'elephants', '', 'like', 'lazy', 'olives'], should return 'Hello'.
# 
# 10) Create a function which given a list of strings returns the longest one. Example: given ['Hi', 'elephants', '', 'like', 'lazy', 'olives'], should return 'elephants'.

# In[1]:


# THIS IS AN EXAMPLE. THERE IS NOTHING TO DO. IT WILL NOT BE GRADED.
# 0) Create a function which computes the area of a rectangle given its height and width.
def exercise_00(height, width):
    result = height * width
    return result


# In[2]:


# run and check
exercise_00(10, 20)


# In[35]:


# 1) Create a function which given 2 booleans computes the exclusive OR.
# (should return True if one boolean is True and the other boolean is false, False if both booleans are True or both booleans are False).
def exercise_01(bool1, bool2):
    # change the line 'result = None' to perform the appropriate calculation
    result= False if bool1==bool2 else True
    return result


# In[36]:


# run and check
exercise_01(True, False)


# In[30]:


# 2) Create a function which given hours, minutes and seconds computes the total of seconds.
def exercise_02(hours, minutes, seconds):
    # change the line 'result = None' to perform the appropriate calculation
    result = hours*60*60+minutes*60+seconds
    return result


# In[31]:


# run and check
exercise_02(1, 1, 1)


# In[352]:


# 3) Create a function which given an integer, compute the sum of all integers between this integer and its double included.
def exercise_03(integer):
    # change the line 'result = None' to perform the appropriate calculation
    result =0
    for integer in range(integer,(2*integer+1)):
        result+=integer
    return result


# In[353]:


# run and check
exercise_03(3)


# In[93]:


# 4) Create a function which given a string produces a 2 characters string with the first character of the initial string and the last one.
# If the initial string is empty, it should return an empty string.
def exercise_04(string):
    # change the line 'result = None' to perform the appropriate calculation
    result = string[0]+string[-1]
    return result


# In[94]:


# run and check
exercise_04('Python')


# In[98]:


# 5) Create a function which given a string returns the sentence: 'The reverse of X is Y!'
def exercise_05(string):
    # change the line 'result = None' to perform the appropriate calculation
    if type(string)== str:
        result = print('The reverse of X is Y')
    return result


# In[99]:


# run and check
exercise_05('Paris')


# In[118]:


# 6) Create a function which given a string returns True if the letters of the string are unique and False otherwise.
def exercise_06(string):
    # change the line 'result = None' to perform the appropriate calculation
    for letter in string:
        if string.count(letter)>1:
            result = False
        else:
            result= True
    return result


# In[119]:


# run and check
exercise_06('Python')


# In[310]:


# 7) Create a function which given a string returns True if the string is a palindrome
# (e.g., a word which has the property of reading the same forwards as it does backwards) and False otherwise.
def exercise_07(string):
    # change the line 'result = None' to perform the appropriate calculation
    string_forward=list(string)
    print(string_forward)
    print(list(reversed(string_forward)))
    if list(reversed(string_forward))==string_forward:
        result = True
    else:
        result=False
    return result


# In[311]:


# run and check
exercise_07('tattarrattat')


# In[155]:


# 8) Create a function which given 3 numbers returns the one which is in the middle.
def exercise_08(number1, number2, number3):
    # change the line 'result = None' to perform the appropriate calculation
    numbers =[number1,number2,number3]
    result = numbers[1]
    return result


# In[156]:


# run and check
exercise_08(9, 5, 6)


# In[409]:


# 9) Create a function which given a list of strings produces a string with the first character of each non empty string of the list.
def exercise_09(list_of_strings):
    # change the line 'result = None' to perform the appropriate calculation
    result=''
    for string in list_of_strings:
        new_list=string[0:1]
        if string=='':
            continue
        result+=new_list
    return result
    


# In[410]:


# run and check
exercise_09(['Hi', 'elephants', '', 'like', 'lazy', 'olives'])


# In[420]:


# 10) Create a function which given a list of strings returns the longest one.
def exercise_10(list_of_strings):
    # change the line 'result = None' to perform the appropriate calculation
    j=list_of_strings[0]
    for i in list_of_strings:
        if len(i)>len(j):
            j=i
        
    return j


# In[421]:


# run and check
exercise_10(['Hi', 'elephants', '', 'like', 'lazy', 'olives'])


# In[ ]:





# In[ ]:




