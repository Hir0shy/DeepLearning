# -*- coding: utf-8 -*-

import re
import os

#csvへの変換を行う
def getmeta(f, f2) :
	
	a = ""
	b = ""
	c = ""
	
	for l in f :
		
		
		if re.search(r"番組表",l):
			
			f.readline()
			#レース名
			a = f.readline()
			f.readline()
			#日にち、日付、開催地
			b = f.readline()
			
			d = a[:-1].strip() + "," + b[3:7] + "," + b[17:28] + "," + b[51:58].strip() + ","
			
		if re.search(r"Ｒ",l) and re.search(r"Ｈ",l)  :
				#ラウンド、種別
				a = l[1:3] + "," + l[5:8] + "," 
				f.readline()
				f.readline()
				f.readline()
				f.readline()
				c = f.readline()
				
				#番組表取得
				while c != "\n":
					
					if re.search(r"BEND",c):
						
						break
					
					e = c[0] + "," + c[2:6] + "," + c[6:10] + "," + c[10:12] + "," + c[12:14] + "," + c[14:16] + "," + c[16:18] + "," + c[19:23] + "," + c[24:29] + "," + c[30:34] + "," + c[36:40] + "," + c[41:43] + "," + c[44:49] + "," + c[50:52] + "," + c[53:58] + "," + c[59:61] + "," + c[61:63] + "," + c[63:65] + "," + c[65:67] + "," + c[67:69] + "," + c[69:71] + "," + c[71:73]
					c = f.readline()
					f2.write(d + a + e + "\n")
				
				
					
file_list = os.listdir('timetable_txt')
m = ""
filename = ""
head = "レース名,日にち,日付,開催地,ラウンド名,種別,艇番,選手登番,選手名,年例,出身,体重,級別,全国勝率,2率,当地勝率,2率,モーターNo,2率,ボートNo,2率,今節成績1,2,3,4,5,6,早見\n"

#1年分ごとにまとめて変換を行う
for m in file_list: 
	f = open("timetable_txt/" + m,"r")
	# 2002
	if (m == "B020101.TXT"):
		filename = m.split(".")[0] + ".csv"	
		f2 = open("timetable_csv/" + filename,"w")
		f2.write(head)
		getmeta(f,f2)
	elif (m == "B021231.TXT"):
		getmeta(f,f2)
		f2.close()
		f.close()
		print(filename + " : 2002年のタイムテーブルデータを生成")
	# 2003
	elif (m == "B030101.TXT"):
		filename = m.split(".")[0] + ".csv"	
		f2 = open("timetable_csv/" + filename,"w")
		f2.write(head)
		getmeta(f,f2)
	elif (m == "B031231.TXT"):
		getmeta(f,f2)
		f2.close()
		f.close()
		print(filename + " : 2003年のタイムテーブルデータを生成")
	# 2004
	elif (m == "B040101.TXT"):
		filename = m.split(".")[0] + ".csv"	
		f2 = open("timetable_csv/" + filename,"w")
		f2.write(head)
		getmeta(f,f2)
	elif (m == "B041231.TXT"):
		getmeta(f,f2)
		f2.close()
		f.close()
		print(filename + " : 2004年のタイムテーブルデータを生成")
	# 2005
	elif (m == "B050101.TXT"):
		filename = m.split(".")[0] + ".csv"	
		f2 = open("timetable_csv/" + filename,"w")
		f2.write(head)
		getmeta(f,f2)
	elif (m == "B051231.TXT"):
		getmeta(f,f2)
		f2.close()
		f.close()
		print(filename + " : 2005年のタイムテーブルデータを生成")
	# 2006
	elif (m == "B060101.TXT"):
		filename = m.split(".")[0] + ".csv"	
		f2 = open("timetable_csv/" + filename,"w")
		f2.write(head)
		getmeta(f,f2)
	elif (m == "B061231.TXT"):
		getmeta(f,f2)
		f2.close()
		f.close()
		print(filename + " : 2006年のタイムテーブルデータを生成")
	# 2007
	elif (m == "B070101.TXT"):
		filename = m.split(".")[0] + ".csv"	
		f2 = open("timetable_csv/" + filename,"w")
		f2.write(head)
		getmeta(f,f2)
	elif (m == "B071231.TXT"):
		getmeta(f,f2)
		f2.close()
		f.close()
		print(filename + " : 2007年のタイムテーブルデータを生成")
	# 2008
	elif (m == "B080101.TXT"):
		filename = m.split(".")[0] + ".csv"	
		f2 = open("timetable_csv/" + filename,"w")
		f2.write(head)
		getmeta(f,f2)
	elif (m == "B081231.TXT"):
		getmeta(f,f2)
		f2.close()
		f.close()
		print(filename + " : 2008年のタイムテーブルデータを生成")
	# 2009
	elif (m == "B090101.TXT"):
		filename = m.split(".")[0] + ".csv"	
		f2 = open("timetable_csv/" + filename,"w")
		f2.write(head)
		getmeta(f,f2)
	elif (m == "B091231.TXT"):
		getmeta(f,f2)
		f2.close()
		f.close()
		print(filename + " : 2009年のタイムテーブルデータを生成")
	# 2010
	elif (m == "B100101.TXT"):
		filename = m.split(".")[0] + ".csv"	
		f2 = open("timetable_csv/" + filename,"w")
		f2.write(head)
		getmeta(f,f2)
	elif (m == "B101231.TXT"):
		getmeta(f,f2)
		f2.close()
		f.close()
		print(filename + " : 2010年のタイムテーブルデータを生成")
	# 2011
	elif (m == "B110101.TXT"):
		filename = m.split(".")[0] + ".csv"	
		f2 = open("timetable_csv/" + filename,"w")
		f2.write(head)
		getmeta(f,f2)
	elif (m == "B111231.TXT"):
		getmeta(f,f2)
		f2.close()
		f.close()
		print(filename + " : 2011年のタイムテーブルデータを生成")
	# 2012
	elif (m == "B120101.TXT"):
		filename = m.split(".")[0] + ".csv"	
		f2 = open("timetable_csv/" + filename,"w")
		f2.write(head)
		getmeta(f,f2)
	elif (m == "B121231.TXT"):
		getmeta(f,f2)
		f2.close()
		f.close()
		print(filename + " : 2012年のタイムテーブルデータを生成")
	# 2013
	elif (m == "B130101.TXT"):
		filename = m.split(".")[0] + ".csv"	
		f2 = open("timetable_csv/" + filename,"w")
		f2.write(head)
		getmeta(f,f2)
	elif (m == "B131231.TXT"):
		getmeta(f,f2)
		f2.close()
		f.close()
		print(filename + " : 2013年のタイムテーブルデータを生成")
	# 2014
	elif (m == "B140101.TXT"):
		filename = m.split(".")[0] + ".csv"	
		f2 = open("timetable_csv/" + filename,"w")
		f2.write(head)
		getmeta(f,f2)
	elif (m == "B141231.TXT"):
		getmeta(f,f2)
		f2.close()
		f.close()
		print(filename + " : 2014年のタイムテーブルデータを生成")
	# 2015
	elif (m == "B150101.TXT"):
		filename = m.split(".")[0] + ".csv"	
		f2 = open("timetable_csv/" + filename,"w")
		f2.write(head)
		getmeta(f,f2)
	elif (m == "B151231.TXT"):
		getmeta(f,f2)
		f2.close()
		f.close()
		print(filename + " : 2015年のタイムテーブルデータを生成")
	# 2016
	elif (m == "B160101.TXT"):
		filename = m.split(".")[0] + ".csv"	
		f2 = open("timetable_csv/" + filename,"w")
		f2.write(head)
		getmeta(f,f2)
	elif (m == "B161231.TXT"):
		getmeta(f,f2)
		f2.close()
		f.close()
		print(filename + " : 2016年のタイムテーブルデータを生成")
	# 2017
	elif (m == "B170101.TXT"):
		filename = m.split(".")[0] + ".csv"	
		f2 = open("timetable_csv/" + filename,"w")
		f2.write(head)
		getmeta(f,f2)
	elif (m == "B171231.TXT"):
		getmeta(f,f2)
		f2.close()
		f.close()
		print(filename + " : 2017年のタイムテーブルデータを生成")
	# 2018
	elif (m == "B180101.TXT"):
		filename = m.split(".")[0] + ".csv"	
		f2 = open("timetable_csv/" + filename,"w")
		f2.write(head)
		getmeta(f,f2)
	elif (m == "B181231.TXT"):
		getmeta(f,f2)
		f2.close()
		f.close()
		print(filename + " : 2018年のタイムテーブルデータを生成")
	# 2019
	elif (m == "B190101.TXT"):
		filename = m.split(".")[0] + ".csv"	
		f2 = open("timetable_csv/" + filename,"w")
		f2.write(head)
		getmeta(f,f2)
	elif (m == "B191231.TXT"):
		getmeta(f,f2)
		f2.close()
		f.close()
		print(filename + " : 2019年のタイムテーブルデータを生成")
	# 2020
	elif (m == "B200101.TXT"):
		filename = m.split(".")[0] + ".csv"	
		f2 = open("timetable_csv/" + filename,"w")
		f2.write(head)
		getmeta(f,f2)
	elif (m == "B201231.TXT"):
		getmeta(f,f2)
		f2.close()
		f.close()
		print(filename + " : 2020年のタイムテーブルデータを生成")
	# 2021
	elif (m == "B210101.TXT"):
		filename = m.split(".")[0] + ".csv"	
		f2 = open("timetable_csv/" + filename,"w")
		f2.write(head)
		getmeta(f,f2)
	elif (m == "B211231.TXT"):
		getmeta(f,f2)
		f2.close()
		f.close()
		print(filename + " : 2021年のタイムテーブルデータを生成")
	# 2022
	elif (m == "B220101.TXT"):
		filename = m.split(".")[0] + ".csv"	
		f2 = open("timetable_csv/" + filename,"w")
		f2.write(head)
		getmeta(f,f2)
	elif (m == "B221231.TXT"):
		getmeta(f,f2)
		f2.close()
		f.close()
		print(filename + " : 2022年のタイムテーブルデータを生成")
	else:
		getmeta(f,f2)
		f.close()