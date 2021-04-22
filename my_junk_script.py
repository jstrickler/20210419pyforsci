#!/usr/bin/env python
# coding: utf-8

# # playing with stupid numbers

# In[1]:


import numpy as np


# ## Loading data

# In[12]:


sample_data = np.loadtxt(   # <1>
    "DATA/columns_of_numbers.txt",
    skiprows=1,
    dtype=int
)


# In[13]:


sample_data[:50]


# ## selecting desired data

# In[14]:


selected = sample_data[  # <2>
    (sample_data[:, 0] < 10) &  # <3>
    (sample_data[:, -1] > 35)
]
selected


# In[15]:


print(len(selected), selected.size)


# In[16]:


print(len(sample_data), sample_data.size)


# In[17]:


print(sample_data.shape, sample_data.dtype, sample_data.ndim)


# In[ ]:





# In[ ]:




