#!/usr/bin/env python
# coding: utf-8

# **Name:** Sina <br> 
# **Last name:** Heidari <br> 
# **Student number:** 400464201 <br> 
# **Course:** Natural Language Processing <br> 

# # Importing Libraries

# In[1]:


from os import walk
import os
from parsivar import Normalizer
from parsivar import Tokenizer
from parsivar import FindStems
from hazm import Lemmatizer
import re


# **If you don't have hazm and parsivar installed, run the following command inside the working directory:**<br> 
# pip install -r requirements.txt

# # Reading the poem files into a dictionary

# In[2]:


# derives current working folder path from getcwd function
poems_path = os.getcwd() + '/Poems'

# create a dic for storing the poems
poems = {}

# walk through all of the files inside Poems directory
for root, dirs, files in walk(poems_path):
    # iterate through all poem files
    for name in files:
        # join cwd path and file name and open the file
        to_read_file = open(os.path.join(root, name))
        # split file name with '.' and choose first field
        file_key = name.split('.')[0]
        # store in dic
        poems[file_key] = {'txt' : to_read_file.read(), 'tokenized': []}
        to_read_file.close()

# Ex: open file with key: 4844
print(poems['4844']['txt'])


# # Normalize each poem document

# In[3]:


normalizer = Normalizer()
for key in poems:
    poems[key] = normalizer.normalize(poems[key]['txt'])
    # replace half spaces and new line characters with single space
    poems[key] = {'txt': re.sub('‌|[\\n]' , ' ', poems[key]), 'tokenized': []}


# In[4]:


print(poems['4844'])


# # Tokenize each poem document
# Tokenized poems are stored in 'tokenized' field of every dictionary element (which is a dictionary itself).

# In[5]:


tokenizer = Tokenizer()
for key in poems:
    poems[key]['tokenized'] = tokenizer.tokenize_words(poems[key]['txt'])


# In[6]:


print(poems['4844']['tokenized'])


# # Removing stop-words

# In[7]:


# read stop-words file
stop_file = open(os.getcwd() + '/Stopwords/Stopwords.txt', mode='r')
stop_file = stop_file.read()
# split them into a list of words
stop_file_split = stop_file.split('\n')
to_read_file.close()
tokenizer = Tokenizer()
# for every key inside poem dictionary
for key in poems:
    # a list comprehension to only choose words that are not included in our stop-words file (ignore stop-words)
    poems[key]['tokenized'] = [token for token in poems[key]['tokenized'] if token not in stop_file_split]


# In[8]:


print(poems['4844']['tokenized'])


# # Lemmatizing tokenized words

# In[9]:


lemmatizer = Lemmatizer()
# A list comprehension to lemmetize each word inside the tokenized list of words corresponding to each element of dictionary
example_lemmetized = [lemmatizer.lemmatize(token) for token in poems['4844']['tokenized']]


# In[10]:


print(example_lemmetized)


# # Stemming tokenized words

# In[11]:


my_stemmer = FindStems()
# A list comprehension to find stems of each word inside the tokenized list of words corresponding to each element of dictionary
example_stems = [my_stemmer.convert_to_stem(token) for token in poems['4844']['tokenized']]


# In[12]:


print(example_stems)

