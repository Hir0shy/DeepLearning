import pandas as pd
import numpy as np

filename_txt = 'bs_2020_0622.txt' #オリジナルテキストデータ
output_raw = '2020_0622_raw.txt' #処理後その１_空白処理後のテキストデータ

with open(filename_txt, mode='r', encoding='utf-8') as f:
    lines = f.readlines()

for i in range(len(lines)):
    with open(output_raw, mode='a', encoding='utf-8') as f:
         f.writelines(lines[i].replace("選  手  名","選手名")
                              .replace("m波","")\
                              .replace("cm","")\
                              .replace("進入固定","")\
                              .replace("〜","")\
                              .replace("！","")\
                              .replace("（","")\
                              .replace("）","")\
                              .replace("・","")\
                              .replace("−","")\
                              .replace("　","")\
                              .replace("     "," ")\
                              .replace("    "," ")\
                              .replace("   "," ")\
                              .replace("  "," ").lstrip())


for m in file_list: 
	f = open("result_txt/" + m,"r")
	# 2022