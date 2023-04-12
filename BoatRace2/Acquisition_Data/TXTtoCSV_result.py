# -*- coding: utf-8 -*-

import re
import os

#csvへの変換を行う
def getmeta(f, f2) :
	
	a = ""
	b = ""
	c = ""
	
	for l in f :
		
		
		if re.search(r"競走成績",l):
			
			f.readline()
			a = f.readline()
			f.readline()
			b = f.readline()
			# レース名,第 〇日,Y/M/D,〇〇競艇場
			d = a[:-1].strip() + "," + b[3:7] + "," + b[17:27] + "," + b[56:65] + ","
		
		if re.search(r"R",l) and re.search(r"H",l) :
				# ラウンド名,種別,コース距離,天候,風向き,風速,波の高さ
                # 種別の部分で列数が変わってしまうため、種別以降のカラムがうまくいかない
				a = l[3:4] + "," + l[12:15] + "," # + l.split("H")[36:40] + "," + l[43:45] + "," + l[50:52] + "," + l[53:55] + "," + l[61:63] + ","
				f.readline()
				f.readline()
				c = f.readline()
				
				# 入着順位,艇,登番,選手名,モーターナンバー,ボートナンバー,展示タイム,進入,スタートタイミング,レースタイム
				while c != "\n":
					e = c[2:4] + "," + c[6] + "," + c[8:12] + "," + c[13:21] + "," + c[22:24] + "," + c[27:29] + "," + c[31:35] + "," + c[38] + "," + c[43:47] + "," + c[52:58]       
					c = f.readline()
					f2.write(d + a + e + "\n")

file_list = os.listdir('result_txt')
m = ""
filename = ""
# "レース名,日にち,日付,開催地,ラウンド名,種別,距離(m),天候,風向き,風速(m),波の高さ(cm),着,艇,登番,選手名,モーター,ボート,展示,進入,ST,レースタイム\n"
head = "レース名,日にち,日付,開催地,ラウンド名,種別,着,艇,登番,選手名,モーター,ボート,展示,進入,ST,レースタイム\n"

#1年分ごとにまとめて変換を行う
for m in file_list: 
	f = open("result_txt/" + m,"r")
	# 2022
	if (m == "K220101.TXT"):
		filename = "result_2022.csv"
		f2 = open("result_csv/" + filename, "w")
		f2.write(head)
		getmeta(f, f2)
	elif (m == "K221231.TXT"):
		getmeta(f, f2)
		f2.close()
		f.close()
		print(filename + " : 2022年の成績データを生成")
	else:
		getmeta(f, f2)
		f.close()