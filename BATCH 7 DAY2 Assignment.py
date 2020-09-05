#!/usr/bin/env python
# coding: utf-8

# In[2]:


lst=[1,100,"A","Nikita",98.6]
lst


# In[3]:


lst.append(12)
lst


# In[4]:


lst.insert(3,23)
lst


# In[5]:


lst[2]


# In[6]:


lst[-3]


# In[9]:


lst.index(98.6)


# In[10]:


dict={"Name":"Nikita","class":"MSc Comp sci"}
dict


# In[12]:


dict.get('Name')


# In[13]:


dict.items()


# In[14]:


dict.keys()


# In[17]:


dict.pop("Name")


# In[18]:


dict


# In[20]:


dict["Name"]="Nikita"


# In[21]:


dict


# In[22]:


set1={1,2,3,4,5,6}
set2={2,4,6,8,0}
set1
set2


# In[23]:


set1


# In[24]:


set2.issubset(set1)


# In[25]:


set1.isdisjoint(set2)


# In[26]:


set1.intersection(set2)


# In[27]:


set2.difference(set1)


# In[28]:


set1.discard(set2)


# In[29]:


set2


# In[30]:


set1


# In[31]:


tup=("A","B","c")
tup


# In[33]:


tup.count("B")


# In[34]:


tup.index("c")


# In[35]:


str1="NIKITA"
str2="YERNAlE"
str1


# In[36]:


str2


# In[37]:


str3=str1+str2


# In[38]:


str3


# In[39]:


str1.capitalize()


# In[40]:


str4="nikita"
str4.capitalize()
str4


# In[41]:


str3.count("a")


# In[42]:


str1.isdigit()


# In[43]:


str2.islower()


# In[ ]:




