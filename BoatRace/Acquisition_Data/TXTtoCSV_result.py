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
			#レース名など
			d = a[:-1].strip() + "," + b[3:7] + "," + b[17:27] + "," + b[56:63] + ","
		
		if re.search(r"R",l) and re.search(r"H",l) :
				#ラウンドなど
				a = l[3:5] + "," + l[12:15] + "," 
				f.readline()
				f.readline()
				c = f.readline()
				
				#レース結果取得
				while c != "\n":
					
					e = c[2:4] + "," + c[6] + "," + c[8:12] + "," + c[13:21] + "," + c[22:24] + "," + c[27:29] + "," + c[31:36] + "," + c[38] + "," + c[43:47] + "," + c[52:58]
					c = f.readline()
					f2.write(d + a + e + "\n")

file_list = os.listdir('result_txt')
m = ""
filename = ""
head = "レース名,日にち,日付,開催地,ラウンド名,種別,着,艇,登番,選手名,モーター,ボート,展示,進入,ST,レースタイム\n"

#1年分ごとにまとめて変換を行う
for m in file_list: 
	f = open("result_txt/" + m,"r")
	# 2002
	if (m == "K020101.TXT"):
		filename = m.split(".")[0] + ".csv"	
		f2 = open("result_csv/" + filename,"w")
		f2.write(head)
		getmeta(f,f2)
	elif (m == "K021231.TXT"):
		getmeta(f,f2)
		f2.close()
		f.close()
		print(filename + " : 2002年の成績データを生成")
	# 2003
	elif (m == "K030101.TXT"):
		filename = m.split(".")[0] + ".csv"	
		f2 = open("result_csv/" + filename,"w")
		f2.write(head)
		getmeta(f,f2)
	elif (m == "K031231.TXT"):
		getmeta(f,f2)
		f2.close()
		f.close()
		print(filename + " : 2003年の成績データを生成")
	# 2004
	elif (m == "K040101.TXT"):
		filename = m.split(".")[0] + ".csv"	
		f2 = open("result_csv/" + filename,"w")
		f2.write(head)
		getmeta(f,f2)
	elif (m == "K041231.TXT"):
		getmeta(f,f2)
		f2.close()
		f.close()
		print(filename + " : 2004年の成績データを生成")
	# 2005
	elif (m == "K050101.TXT"):
		filename = m.split(".")[0] + ".csv"	
		f2 = open("result_csv/" + filename,"w")
		f2.write(head)
		getmeta(f,f2)
	elif (m == "K051231.TXT"):
		getmeta(f,f2)
		f2.close()
		f.close()
		print(filename + " : 2005年の成績データを生成")
	# 2006
	elif (m == "K060101.TXT"):
		filename = m.split(".")[0] + ".csv"	
		f2 = open("result_csv/" + filename,"w")
		f2.write(head)
		getmeta(f,f2)
	elif (m == "K061231.TXT"):
		getmeta(f,f2)
		f2.close()
		f.close()
		print(filename + " : 2006年の成績データを生成")
	# 2007
	elif (m == "K070101.TXT"):
		filename = m.split(".")[0] + ".csv"	
		f2 = open("result_csv/" + filename,"w")
		f2.write(head)
		getmeta(f,f2)
	elif (m == "K071231.TXT"):
		getmeta(f,f2)
		f2.close()
		f.close()
		print(filename + " : 2007年の成績データを生成")
	# 2008
	elif (m == "K080101.TXT"):
		filename = m.split(".")[0] + ".csv"	
		f2 = open("result_csv/" + filename,"w")
		f2.write(head)
		getmeta(f,f2)
	elif (m == "K081231.TXT"):
		getmeta(f,f2)
		f2.close()
		f.close()
		print(filename + " : 2008年の成績データを生成")
	# 2009
	elif (m == "K090101.TXT"):
		filename = m.split(".")[0] + ".csv"	
		f2 = open("result_csv/" + filename,"w")
		f2.write(head)
		getmeta(f,f2)
	elif (m == "K091231.TXT"):
		getmeta(f,f2)
		f2.close()
		f.close()
		print(filename + " : 2009年の成績データを生成")
	# 2010
	elif (m == "K100101.TXT"):
		filename = m.split(".")[0] + ".csv"	
		f2 = open("result_csv/" + filename,"w")
		f2.write(head)
		getmeta(f,f2)
	elif (m == "K101231.TXT"):
		getmeta(f,f2)
		f2.close()
		f.close()
		print(filename + " : 2010年の成績データを生成")
	# 2011
	elif (m == "K110101.TXT"):
		filename = m.split(".")[0] + ".csv"	
		f2 = open("result_csv/" + filename,"w")
		f2.write(head)
		getmeta(f,f2)
	elif (m == "K111231.TXT"):
		getmeta(f,f2)
		f2.close()
		f.close()
		print(filename + " : 2011年の成績データを生成")
	# 2012
	elif (m == "K120101.TXT"):
		filename = m.split(".")[0] + ".csv"	
		f2 = open("result_csv/" + filename,"w")
		f2.write(head)
		getmeta(f,f2)
	elif (m == "K121231.TXT"):
		getmeta(f,f2)
		f2.close()
		f.close()
		print(filename + " : 2012年の成績データを生成")
	# 2013
	elif (m == "K130101.TXT"):
		filename = m.split(".")[0] + ".csv"	
		f2 = open("result_csv/" + filename,"w")
		f2.write(head)
		getmeta(f,f2)
	elif (m == "K131231.TXT"):
		getmeta(f,f2)
		f2.close()
		f.close()
		print(filename + " : 2013年の成績データを生成")
	# 2014
	elif (m == "K140101.TXT"):
		filename = m.split(".")[0] + ".csv"	
		f2 = open("result_csv/" + filename,"w")
		f2.write(head)
		getmeta(f,f2)
	elif (m == "K141231.TXT"):
		getmeta(f,f2)
		f2.close()
		f.close()
		print(filename + " : 2014年の成績データを生成")
	# 2015
	elif (m == "K150101.TXT"):
		filename = m.split(".")[0] + ".csv"	
		f2 = open("result_csv/" + filename,"w")
		f2.write(head)
		getmeta(f,f2)
	elif (m == "K151231.TXT"):
		getmeta(f,f2)
		f2.close()
		f.close()
		print(filename + " : 2015年の成績データを生成")
	# 2016
	elif (m == "K160101.TXT"):
		filename = m.split(".")[0] + ".csv"	
		f2 = open("result_csv/" + filename,"w")
		f2.write(head)
		getmeta(f,f2)
	elif (m == "K161231.TXT"):
		getmeta(f,f2)
		f2.close()
		f.close()
		print(filename + " : 2016年の成績データを生成")
	# 2017
	elif (m == "K170101.TXT"):
		filename = m.split(".")[0] + ".csv"	
		f2 = open("result_csv/" + filename,"w")
		f2.write(head)
		getmeta(f,f2)
	elif (m == "K171231.TXT"):
		getmeta(f,f2)
		f2.close()
		f.close()
		print(filename + " : 2017年の成績データを生成")
	# 2018
	elif (m == "K180101.TXT"):
		filename = m.split(".")[0] + ".csv"	
		f2 = open("result_csv/" + filename,"w")
		f2.write(head)
		getmeta(f,f2)
	elif (m == "K181231.TXT"):
		getmeta(f,f2)
		f2.close()
		f.close()
		print(filename + " : 2018年の成績データを生成")
	# 2019
	elif (m == "K190101.TXT"):
		filename = m.split(".")[0] + ".csv"	
		f2 = open("result_csv/" + filename,"w")
		f2.write(head)
		getmeta(f,f2)
	elif (m == "K191231.TXT"):
		getmeta(f,f2)
		f2.close()
		f.close()
		print(filename + " : 2019年の成績データを生成")
	# 2020
	elif (m == "K200101.TXT"):
		filename = m.split(".")[0] + ".csv"	
		f2 = open("result_csv/" + filename,"w")
		f2.write(head)
		getmeta(f,f2)
	elif (m == "K201231.TXT"):
		getmeta(f,f2)
		f2.close()
		f.close()
		print(filename + " : 2020年の成績データを生成")
	# 2021
	elif (m == "K210101.TXT"):
		filename = m.split(".")[0] + ".csv"	
		f2 = open("result_csv/" + filename,"w")
		f2.write(head)
		getmeta(f,f2)
	elif (m == "K211231.TXT"):
		getmeta(f,f2)
		f2.close()
		f.close()
		print(filename + " : 2021年の成績データを生成")
	# 2022
	elif (m == "K220101.TXT"):
		filename = m.split(".")[0] + ".csv"	
		f2 = open("result_csv/" + filename,"w")
		f2.write(head)
		getmeta(f,f2)
	elif (m == "K221231.TXT"):
		getmeta(f,f2)
		f2.close()
		f.close()
		print(filename + " : 2022年の成績データを生成")
	else:
		getmeta(f,f2)
		f.close()