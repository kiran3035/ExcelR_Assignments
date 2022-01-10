#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import numpy as np
from scipy import stats


# Problem Statement :
# TeleCall uses 4 centers around the globe to process customer order forms. They audit a certain % of the customer order forms. Any error in order form renders it defective and has to be reworked before processing. The manager wants to check whether the defective % varies by centre. Please analyze the data at 5% significance level and help the manager draw appropriate inferences
# 
# 1 - Business Problem
# Does the defective % varies significantly by centre ?
# 
# 2 - Data description
# α == 0.05 (95% Confidence)
# 
# Y == Discrete
# X == Discrete
# 
# Since there are more than 2 variable we will perform Chi-Square test
# 
# 3 - Chi-Square Test

# In[3]:


df = pd.read_csv("C:\\Users\\kiran\\Desktop\\New folder\\Costomer+OrderForm.csv")


# H0 == The defective % does not varies by centre
# H1 == The defective % does varies by centre

# In[4]:


stats.chi2_contingency([df['Phillippines'].value_counts(), df['Indonesia'].value_counts(), df['Malta'].value_counts(), df['India'].value_counts()])


# P value of Chi-Square test == 0.277 > α
# 
# Thus HO is accepted.
# The defective % does not varies significantly by centres
