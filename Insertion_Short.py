#!/usr/bin/env python
# coding: utf-8

# In[22]:


# Insertion Sort

A = [5,2,4,6,1,3,3,2,3,45,3,2,3,434,3,45,54,5,45,4,5,4,23,43,4,35]


# In[23]:


for x in range(1,len(A)):
    key = A[x]
    fi = x - 1
    while (fi>=0 and A[fi]>key):
        A[fi+1] = A[fi]
        fi = fi - 1
    A[fi+1] = key
    
print(A)


# In[ ]:




