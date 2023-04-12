import lhafile
import os
import re
#https://trac.neotitans.net/wiki/lhafile/

file_list = os.listdir('racer_lzh/')
m = ""
f = ""
out = ""
name = ""
for m in file_list :
  if re.search(".lzh",m):
   # 解凍
   f = lhafile.Lhafile("racer_lzh/" + m)
   info = f.infolist()
   name = info[0].filename
   out = open("racer_txt/" + name,"wb").write(f.read(name))

