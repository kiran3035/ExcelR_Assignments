#!/usr/bin/env python
# coding: utf-8

# # cutlet problem

# In[4]:


import pandas as pd
import numpy as np
from scipy import stats


# Problem Statement :
# A F&B manager wants to determine whether there is any significant difference in the diameter of the cutlet between two units. A randomly selected sample of cutlets was collected from both units and measured? Analyze the data and draw inferences at 5% significance level. Please state the assumptions and tests that you carried out to check validity of the assumptions
# 
# 1 - Business Problem
# Is there significant difference in the diameter of the cutlet ?
# 
# 2 - Data description
# α == 0.05 (95% Confidence)
# 
# Y == Continious
# X == Discrete
# 
# Is Y1 and Y2 normal ?
# 
# H0 = Y1 and Y2 are normal
# H1 = Y1 and Y2 are not normal
# 
# 3 - Normality Test

# In[6]:


df = pd.read_csv("C:\\Users\\kiran\\Desktop\\New folder\\Cutlets.csv")
stats.shapiro(df["Unit A"])


# P value for Unit A == 0.32 > α

# In[7]:


stats.shapiro(df["Unit B"])


# (0.9727300405502319, 0.5224985480308533)
# P value for Unit B == 0.52 > α
# 
# HO is accepted. Thats is both Y1 and Y2 are normal
# 4 - External Condition
# External condition are same.
# Thus we can perform Paired T Test
# 5 - Model
# H0 == Mean for Y1 and Y2 are equal (There is no significance difference between diameter of the Culets)
# H1 == Mean for Y1 and Y2 are not equal (There is a significance difference between diameter of the Culets)

# In[8]:


stats.ttest_rel(df["Unit A"], df["Unit B"])


# Ttest_relResult(statistic=0.7536787225614323, pvalue=0.45623007680384076)
# P value of the Paired T Test is == 0.45 > α
# 
# Thus H0 is accepted.
# Mean of both Y1 and Y2 are equal
