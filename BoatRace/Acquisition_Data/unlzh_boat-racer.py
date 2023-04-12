import lhafile
import os
import re
#https://trac.neotitans.net/wiki/lhafile/

file_list = os.listdir('boat-racer_lzh/')
m = ""
f = ""
out = ""
name = ""
for m in file_list :
  if re.search(".lzh",m):
   # 解凍
   f = lhafile.Lhafile("boat-racer_lzh/" + m)
   info = f.infolist()
   name = info[0].filename
   out = open("boat-racer_txt/" + name,"wb").write(f.read(name))

