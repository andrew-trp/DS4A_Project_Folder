ls#!/usr/bin/env python
# coding: utf-8

# In[1]:


#pip install -r requirements.txt #This needs to be commented out in a jupyter notebook


# In[2]:


import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from scipy.stats import chi2_contingency
import pingouin
import sklearn
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.feature_extraction.text import TfidfVectorizer
import re


# In[3]:


def cleanhtml(raw_html):
  cleanr = re.compile('<.*?>|&([a-z0-9]+|#[0-9]{1,6}|#x[0-9a-f]{1,6});')
  cleantext = re.sub(cleanr, ' ',raw_html)
  return cleantext


# In[70]:


masculine_words = ["active","Adventurous","Aggress*","Ambitio*","Ambition","Analy*","Assert*","assertive","Athlet*","Autonom*","autonomous","Boast*","Challeng*","Compet*","competition","competitive","compliance","Confident","control","Courag*","Decide","Decision*","Decisive","Determin*","Direct","Domina*","Dominant","driven","ensure","Force*","Greedy","Headstrong","Hierarch*","hierarchical","Hostil*","Implusive","Independen*","Individual*","Intellect*","Lead*","leading","Logic","manage","Masculine","must","Objective","Opinion","Outspoken","perform individually","Persist","ping pong/pool table","Principle*","progress","Reckless","rigid","satisfy","Self-confiden*","Self-relian*","Self-sufficien*","Silicon Valley","stand","stock options","Strong","Stubborn","Superior","takes risk","workforce","seasoned"]


# In[79]:


df = pd.read_excel('results.xls', index_col=0)
df = df.dropna(how='any')
df = df.reset_index(drop=True)
df.head()


# In[80]:


#Removes part of the messy html
df = df.replace(r'\n',' ', regex=True)
df = df.replace(r'\t','', regex=True)
df = df.replace(r'\s\s\s','', regex=True)


# In[81]:


clean_description = []
for i in df['description']:
    clean = cleanhtml(i)
    clean_description.append(clean)


# In[82]:


df['clean_description'] = clean_description
df.head()


# In[83]:


description_list = df['clean_description']
words_in_description = []

for n in description_list:
    #n = "'''"+str(n)+"'''"
    n=[n]
    vectorizer = TfidfVectorizer()
    X = vectorizer.fit_transform(n)
    Y = vectorizer.get_feature_names()
    words_in_description.append(Y)


# In[84]:


df['words_description'] = words_in_description
df.head()


# In[85]:


word_count = []
for desc in df['words_description']:
    count = 0
    for w in desc:    
        if w in masculine_words:
            count += 1
    word_count.append(count)


# In[86]:


df['masculine_score'] = word_count


# In[75]:


df.head()


# In[87]:

histo = df['masculine_score'].hist()

plot = histo.get_figure()

plot.savefig("plots/Histogram.png")

# In[ ]:

print("done")


