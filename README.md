# FPFinder
 The script to identify fingerprint sites based on vcf files

## Install:

This python script only need numpy and pandas installed, which could be implemented as below:

conda install numpy

conda install pandas

Download the file and enter the FPFinder directory.

## Run:

This script requires two steps, i)transform the vcf file into matrix file in which 0 represents for site absence and 1 represents for site presence. ii) calculate fingerprint score for each site based on the matrix file.

### 1. File transformation

For the first step, the command is below:

if we have vcf file for both target population(small population with fingerprint sites) and background population (large cohort used as background):

***python 01trans_input_files.py -target_vcf target.vcf -background_vcf background.vcf -background_stat background.stat -target_stat target.stat***

or if the target population is just a small part of the background population, we could run this step like this:

***python 01trans_input_files.py -target_name target_name.txt -background_vcf background.vcf -background_stat background.stat -target_stat target.stat***

In file target_name.txt, the name of sample was recorded.

### 2. Fingerprint score calculation:

After the file transformation, we could calculate the fingerprint score based on the matrix files. The command could be implemented like this:

python 02calculate_fp_score.py -background_stat background.stat -target_stat target.stat -fp_score_file fpscore.csv

## Result:

The result file is a csv file recording each variant's fingerprint score. Higher score represents for more specific site in target population.

