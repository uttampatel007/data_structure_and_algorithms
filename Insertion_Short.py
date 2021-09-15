#!/usr/bin/env python
# coding: utf-8

# In[22]:


# Insertion Sort

# If element before is bigger then it will move right

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



# Insertion sort practice 2

A = [1,5,56,44,2323,54545,3,32,2,2,4,5,6,3,2,23,4,4,6,6,8,9,]

for j in range(1,len(A)):
    key = A[j]
    i = j-1
    
    while(i>0 and A[i]>key):
        A[i+1] = A[i]
        i -= 1
    A[i+1] = key
    
print(A)
