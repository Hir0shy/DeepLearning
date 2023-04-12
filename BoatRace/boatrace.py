import pandas as pd
from pandas import DataFrame, Series

import warnings
import pdb
warnings.filterwarnings('ignore')
pd.set_option('display.max_columns', 150)

# path
path_racer = "C:/Users/HiroshiHarada/DeepLearning/BoatRace/Acquisition_Data/boat-racer_csv/" # boat-racer
path_ttable = "C:/Users/HiroshiHarada/DeepLearning/BoatRace/Acquisition_Data/timetable_csv/" # timetable
path_result = "C:/Users/HiroshiHarada/DeepLearning/BoatRace/Acquisition_Data/result_csv/"    # result

# get csv_file 2020~2022
df_racer = pd.read_csv(path_racer + 'FAN0110.csv', encoding="ANSI")

#df_ttable_2020 = pd.read_csv(path_ttable + 'B200101.csv', encoding="ANSI")
#df_ttable_2021 = pd.read_csv(path_ttable + 'B210101.csv', encoding="ANSI")
#df_ttable_2022 = pd.read_csv(path_ttable + 'B220101.csv', encoding="ANSI")

df_result_2020 = pd.read_csv(path_result + 'K200101.csv', encoding="ANSI")
df_result_2021 = pd.read_csv(path_result + 'K210101.csv', encoding="ANSI")
df_result_2022 = pd.read_csv(path_result + 'K220101.csv', encoding="ANSI")

# 結合してまとめる
#df_ttable = pd.concat([df_ttable_2020,df_ttable_2021,df_ttable_2022],axis=0,ignore_index=True)
df_result = pd.concat([df_result_2020,df_result_2021,df_result_2022],axis=0,ignore_index=True)
pdb.set_trace()
# カラムの並び替え 目的変数(着)が最後尾に
df_result = df_result[['レース名', '日にち', '日付', '開催地', 'ラウンド名',
                    '種別', '艇', '登番', '選手名', 'モーター', 'ボート', '展示',
                    '進入', 'スタートタイム', 'レースタイム', '着']]

"レース名,日にち,日付,開催地,ラウンド名,種別,着,艇,登番,選手名,モーター,ボート,展示,進入,ST,レースタイムn"
# 3着以内に入るかどうかの2値分類をして、3着以内の中から1,2,3着の分類をする

##--------------- 前処理 ---------------##
# 使用しないカラムを除去
df_result.drop('レース名', axis=1, inplace=True)
df_result.drop('日にち', axis=1, inplace=True)
df_result.drop('日付', axis=1, inplace=True)
df_result.drop('開催地', axis=1, inplace=True)
df_result.drop('ラウンド名', axis=1, inplace=True)
df_result.drop('種別', axis=1, inplace=True)
df_result.drop('ﾓｰﾀｰ', axis=1, inplace=True)
df_result.drop('ﾎﾞｰﾄ', axis=1, inplace=True)
df_result.drop('展示', axis=1, inplace=True)
df_result.drop('進入', axis=1, inplace=True)
df_result.drop('ﾚｰｽﾀｲﾑ', axis=1, inplace=True)

# train,valid data分割

pdb.set_trace() 








