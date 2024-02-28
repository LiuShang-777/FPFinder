# -*- coding: utf-8 -*-
"""
Created on Tue Dec 26 16:56:41 2023

@author: liushang
"""

import numpy as np
import pandas as pd
import argparse
import sys
parser=argparse.ArgumentParser()
parser.add_argument("-target_stat",help="the transformed result file of target vcf")
parser.add_argument("-background_stat",help="the transformed result file of background vcf")
parser.add_argument("-fp_score_file",help="the transformed result file of background vcf")
args=parser.parse_args()

sf_path=sys.path[0]
sys.path.append(sf_path)
#sys.path.append('F:/tmp/tfidf/')
from utils import trans_vcf_to_stat,tfidf

#get the standard dataframe
background_dat=pd.read_csv(args.background_stat,sep='\t',index_col=0)
target_dat=pd.read_csv(args.target_stat,sep='\t',index_col=0)
common=list(set(target_dat.index.tolist())&set(background_dat.index.tolist()))
target_dat=target_dat.loc[target_dat.index.isin(common)]
background_dat=background_dat.loc[background_dat.index.isin(common)]

target_dat=target_dat.sort_index()
background_dat=background_dat.sort_index()

target_dat=target_dat.sub(1)
target_dat=target_dat.mul(-1)
background_dat=background_dat.sub(1)
background_dat=background_dat.mul(-1)

#tf-idf calculate
term_frequency_dat=target_dat.sum(axis=1)/target_dat.shape[1]
inverse_document_frequency=np.log10(background_dat.shape[1]/background_dat.sum(axis=1))
tf_idf_result=term_frequency_dat*inverse_document_frequency
tf_idf_score=pd.DataFrame()
tf_idf_score['FingerprintScore']=tf_idf_result
tf_idf_score.index=background_dat.index
tf_idf_score.to_csv(args.fp_score_file,sep='\t')