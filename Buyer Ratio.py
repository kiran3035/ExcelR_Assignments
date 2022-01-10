#!/usr/bin/env python
# coding: utf-8

# In[2]:


import pandas as pd
import numpy as np
from scipy import stats


# Problem Statement :
# Sales of products in four different regions is tabulated for males and females. Find if male-female buyer rations are similar across regions
# 
# 1 - Business Problem
# Is the male-female buyer rations are similar across regions
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


df = pd.read_csv("C:\\Users\\kiran\\Desktop\\New folder\\BuyerRatio.csv")


# H0 == The male-female buyer rations are similar across regions
# H1 == The male-female buyer rations are not similar across regions

# In[4]:


stats.chi2_contingency([df["East"], df["West"], df["North"], df["South"]])


# P value of Chi-Square test == 0.66 > α
# 
# Thus HO is accepted.
# The male-female buyer rations are similar across regions
