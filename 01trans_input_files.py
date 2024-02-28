# -*- coding: utf-8 -*-
"""
Created on Sat Dec 23 10:50:43 2023

@author: liushang
"""

import numpy as np
import pandas as pd
import argparse
import sys
parser=argparse.ArgumentParser()
parser.add_argument("-target_vcf",help="vcf file of target population")
parser.add_argument("-background_vcf",help="vcf file of the background population")
parser.add_argument("-target_stat",help="the transformed result file of target vcf")
parser.add_argument("-background_stat",help="the transformed result file of background vcf")
parser.add_argument("-target_name",help="the transformed result file of background vcf")
args=parser.parse_args()

sf_path=sys.path[0]
sys.path.append(sf_path)
#sys.path.append('F:/tmp/tfidf/')
from utils import trans_vcf_to_stat,tfidf

#writing background files
background_vcf=args.background_vcf
background_stat=args.background_stat
background_header,background_marker,background_result=trans_vcf_to_stat.read_vcf(background_vcf)
trans_vcf_to_stat.write_matrix(background_header,background_marker,background_result,background_stat)

#writing target file
target_vcf=args.target_vcf
target_stat=args.target_stat
if args.target_vcf:
    target_header,target_marker,target_result=trans_vcf_to_stat.read_vcf(target_vcf)
    trans_vcf_to_stat.write_matrix(target_header,target_marker,target_result,target_stat)

if args.target_name:
    target_name=args.target_name
    with open(target_name,'r') as file:
        targets=[]
        for line in file:
            line=line.strip()
            targets.append(line)
    background=pd.read_csv(background_stat,sep='\t',index_col=0)
    target_dat=background[targets]
    target_dat.to_csv(target_stat,sep='\t')