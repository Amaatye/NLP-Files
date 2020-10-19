#!/usr/bin/env python
# coding: utf-8

# In[7]:


import nltk
from nltk import word_tokenize


# In[2]:


sentence = [("the", "DT"), ("little", "JJ"), ("yellow", "JJ"),("dog", "NN"), ("barked", "VBD"), ("at", "IN"),  ("the", "DT"), ("cat", "NN")]
grammar="NP: {<DT>?<JJ>*<NN>}"
c=nltk.RegexpParser(grammar)
result=c.parse(sentence)
print(result)
result.draw()


# In[12]:


sen2="Four score and seven years ago our fathers brought forth on this continent, a new nation, conceived in Liberty, and dedicated to the proposition that all men are created equal."
n_token=nltk.word_tokenize(sen2)
c_token=nltk.pos_tag(n_token)
grammar="NP:{<DT>?<JJ>*<NN>}"
i=nltk.RegexpParser(grammar)
res=i.parse(c_token)
print(res)


# In[ ]:




