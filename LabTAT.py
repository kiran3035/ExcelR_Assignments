#!/usr/bin/env python
# coding: utf-8

# # Laboratory Problem

# In[9]:


import pandas as pd
import numpy as np
from scipy import stats


# Problem Statement :
# A hospital wants to determine whether there is any difference in the average Turn Around Time (TAT) of reports of the laboratories on their preferred list. They collected a random sample and recorded TAT for reports of 4 laboratories. TAT is defined as sample collected to report dispatch
# 
# Analyze the data and determine whether there is any difference in average TAT among the different laboratories at 5% significance level
# 
# 1 - Business Problem
# Is there a significant difference in the average Turn Around Time between laboratories ?
# 
# 2 - Data description
# α == 0.05 (95% Confidence)
# 
# Y == Continious
# X == Discrete
# 
# Is Y1, Y2, Y3 and Y4 normal ?
# 
# H0 = Y1, Y2, Y3 and Y4 are normal
# H1 = Y1, Y2, Y3 and Y4 are not normal
# 
# 3 - Normality Test

# In[10]:


df = pd.read_csv("C:\\Users\\kiran\\Desktop\\New folder\\LabTAT.csv")
stats.shapiro(df["Laboratory 1"])


# (0.9901824593544006, 0.5506953597068787)
# P value for Laboratory 1 == 0.55 > α

# In[11]:


stats.shapiro(df["Laboratory 2"])


# (0.9936322569847107, 0.8637524843215942)
# P value for Laboratory 2 == 0.86 > α

# In[12]:


stats.shapiro(df["Laboratory 3"])


# (0.9886345267295837, 0.4205053448677063)
# P value for Laboratory 3 == 0.42 > α

# In[13]:


stats.shapiro(df["Laboratory 4"])


# (0.9913753271102905, 0.6618951559066772)
# P value for Y1 (Unit B) == 0.66 > α
# 
# HO is accepted. Thats is Y1, Y2, Y3, and Y4 are normal
# 4 - Variance
# H0 == Variance of all 4 laboratories are the same
# H1 == Variance of all 4 laboratories are the not same

# In[14]:


stats.levene(df["Laboratory 1"], df["Laboratory 2"], df["Laboratory 3"], df["Laboratory 4"])


# LeveneResult(statistic=2.599642500418024, pvalue=0.05161343808309816)
# P Value of Variance test is == 0.051 > α
# 
# H0 is accepted
# Thus we will perform one way Anova Test
# 5 - Model
# H0 == Mean TAT for 4 laboratories equal (There is no significance difference between TAT of the laboratories)
# H1 == Mean TAT for 4 laboratories not equal (There is a significance difference between TAT of the laboratories)

# In[15]:


stats.stats.f_oneway(df["Laboratory 1"], df["Laboratory 2"], df["Laboratory 3"], df["Laboratory 4"])


# F_onewayResult(statistic=118.70421654401437, pvalue=2.1156708949992414e-57)
# P value of the One way Anova test is == 2e-16 < α
# 
# Thus H1 is accepted.
# Mean TAT for 4 laboratories not equal (There is a significance difference between TAT of the laboratories)
