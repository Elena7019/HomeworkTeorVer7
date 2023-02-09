#!/usr/bin/env python
# coding: utf-8

# In[1]:


import numpy as np
import scipy.stats as stats
x1 = np.array([380, 420, 290])
x2 = np.array([140, 360, 200, 900])
stats.mannwhitneyu(x1, x2)


# In[2]:


import numpy as np
before = np.array([150, 160, 165, 145, 155])
test1 = np.array([140, 155, 150, 130, 135])
test2 = np.array([130, 130, 120, 130, 125])
stats.friedmanchisquare(before, test1, test2)


# In[3]:


import numpy as np
import scipy.stats as stats
before = np.array([150, 160, 165, 145, 155])
test1 = np.array([140, 155, 150, 130, 135])
stats.wilcoxon(before, test1)


# In[4]:


import numpy as np
import scipy.stats as stats
x1 = np.array([56, 60, 62, 55, 71, 67, 59, 58, 64, 67])
x2 = np.array([57, 58, 69, 48, 72, 70, 68, 71, 50, 53])
x3 = np.array([57, 67, 49, 48, 47, 55, 66, 51, 54])
stats.kruskal(x1, x2, x3)


# In[ ]:




