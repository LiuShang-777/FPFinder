# -*- coding: utf-8 -*-
"""
Created on Mon Dec 18 13:12:59 2023

@author: liushang
"""
import numpy as np
def tf_idf_calculate(term_num,term_total,idf_num,idf_total):
    tf=term_num/term_total
    idf=np.log10(idf_total/idf_num)
    fp_score=tf*idf
    return fp_score
    
    
    
    


