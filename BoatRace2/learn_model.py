import os
import numpy as np
import pandas as pd
from pandas import DataFrame, Series

from sklearn.model_selection import train_test_split, GridSearchCV

import warnings
import pdb
warnings.filterwarnings('ignore')
pd.set_option('display.max_columns', 150)

path_result = os.path.join(os.getcwd(), 'Acquisition_Data/result_csv/')
path_racer = os.path.join(os.getcwd(), 'Acquisition_Data/racer_csv/')

df = pd.read_csv(path_result + 'result_2022.csv', encoding="ANSI")
df_racer = pd.read_csv(path_racer + 'boat-racer.csv', encoding="ANSI")

pdb.set_trace()

##------ 前処理 ------##
# 不要なカラムを除去
df.drop('レース名', axis=1, inplace=True)
df.drop('日にち', axis=1, inplace=True)
df.drop('日付', axis=1, inplace=True)
df.drop('ラウンド名', axis=1, inplace=True)
df.drop('種別', axis=1, inplace=True)
#df.drop('登番', axis=1, inplace=True)
df.drop('展示', axis=1, inplace=True)
df.drop('進入', axis=1, inplace=True)
df.drop('ST', axis=1, inplace=True)
df.drop('レースタイム', axis=1, inplace=True)

# 登番が同じracerのカラムを取得(無かったら、全体の最頻値くらい)


# 開催地：one-hot
place = df['開催地']
place_oh = pd.get_dummies(place)
df = pd.concat([df, place_oh], axis=1)
df.drop('開催地', axis=1, inplace=True)

# 選手名：one-hot
racer = df['選手名']
racer_oh = pd.get_dummies(racer)
df = pd.concat([df, racer_oh], axis=1)
df.drop('選手名', axis=1, inplace=True)

# 着(目的変数)：1~6着以外を6着に変換し、01~06を1~6に変換
df.replace({'着': {'01':1, '02':2, '03':3, '04':4, '05':5, '06':6}}, inplace=True)
df.replace({'着': {'0':6, 'F':6, 'K0':6, 'K1':6, 'L0':6, 'L1':6, 'S0':6, 'S1':6, 'S2':6}}, inplace=True)

# ：one-hot
position = df['着']
position_oh = pd.get_dummies(position)
df = pd.concat([df, position_oh], axis=1)
df.drop('着', axis=1, inplace=True)

#pdb.set_trace()
##--------------------##
# dfをdf.train, df.validに分割
x = df.iloc[:, :1658].values
y = df.iloc[:, 1658:].values

split_rate = 0.2
x_train, x_valid, y_train, y_valid = train_test_split(x, y, test_size=split_rate, shuffle=False, random_state=0)

pdb.set_trace()

# モデル作成    
model = Sequential() 
model.add(Dense(132, input_shape=(x_train_std.shape[1],), activation='relu'))
model.add(Dropout(0.36))
model.add(Dense(200, activation='relu'))
model.add(Dropout(0.49))
model.add(Dense(200, activation='relu'))
model.add(Dropout(0.49))
model.add(Dense(y_train.shape[1], activation='softmax'))
model.compile(loss='categorical_crossentropy', optimizer='adam', metrics=['accuracy'])

# モデル学習
early_stopping = EarlyStopping(patience=10, verbose=1)
model.fit(x_train_std, y_train, batch_size=50, verbose=0, epochs=100, validation_split=0.1, callbacks=[early_stopping])

# モデルの保存
model_json = model.to_json()
with open('/content/drive/My Drive/model_winner.json', 'w') as f_model:
    f_model.write(model_json)
best_model.save_weights('/content/drive/My Drive/model_winner.h5')


