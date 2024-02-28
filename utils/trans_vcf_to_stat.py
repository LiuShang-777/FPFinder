# -*- coding: utf-8 -*-
"""
Created on Mon Dec 18 16:15:57 2023

@author: liushang
"""


def genotype(str_):
    symbol_1,symbol_2=str_[0],str_[2]
    if symbol_1=='.':
        symbol_1=0
    if symbol_2=='.':
        symbol_2=0
    symbol_1,symbol_2=int(symbol_1),int(symbol_2)
    if (symbol_1+symbol_2)>=1:
        return '1'
    else:
        return '0'
        
def read_vcf(test):    
    with open(test,'r') as file:
        result,marker,num_record=[],[],0
        for line in file:
            line=line.strip()
            if line.startswith('##'):
                continue
            elif line.startswith('#CHROM'):
                head=line.split('\t')[9:]
            else:
                num_record+=1
                if (num_record%10000)==0:
                    print('taking %d variants'%num_record)
                line=line.split('\t')
                marker.append('_'.join([line[0],str(line[1]),line[3],line[4]]))
                result.append([genotype(i) for i in line[9:]])
    return (head,marker,result)

def write_matrix(header,marker,result,output_file):
    num_record=0
    header='marker'+'\t'+'\t'.join(header)
    with open(output_file,'w') as file:
        file.write(header+'\n')
        for i,j in zip(marker,result):
            num_record+=1
            file.write(i+'\t'+'\t'.join(j)+'\n')
            if (num_record%10000)==0:
                print('recording %d variants'%num_record)







