# -*- coding: utf-8 -*-
"""
Created on Wed Sep  6 15:20:36 2023

@author: matthew.wortman372
"""
from scipy.stats import ttest_ind
import numpy as np
import wooldridge as woo

bwght = woo.dataWoo('BWGHT')

mother_educ = bwght['motheduc']
father_educ = bwght['fatheduc']

# find the valid rows
valid_rows = np.logical_and(~np.isnan(mother_educ), ~np.isnan(father_educ))

# only for those rows, select the mother and father education
mother_educ_valid = mother_educ[valid_rows]
father_educ_valid = father_educ[valid_rows]

# calculate the mean of the mother and father education
average_father_edu = np.mean(father_educ_valid)
print(f'average father edu {average_father_edu}')

average_mother_educ = np.mean(mother_educ_valid)
print(f'average mother edu {average_mother_educ}')

# for the same rows lets find std
std_mother_edu = mother_educ_valid[valid_rows].std()
std_father_edu = father_educ_valid[valid_rows].std()

# for the same rows lets find mean
average_father_edu = mother_educ[valid_rows].mean()
average_mother_edu = father_educ[valid_rows].mean()

# find z
z_score_fatheduc_18 = (18 - average_father_edu) / std_father_edu
z_score_motheduc_18 = (18 - average_mother_edu) / std_mother_edu
print(z_score_fatheduc_18, z_score_motheduc_18)

t_stat, p_value = ttest_ind(average_father_edu, average_mother_edu)
print(t_stat, p_value)
