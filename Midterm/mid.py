# -*- coding: utf-8 -*- # us Korean (unicode charset)
2번 문제 
# can us Korean (unicode charset) for arguments
import sys
reload (sys)
sys.setdefaultencoding ('utf-8')

from pyExcelerator import *

SourceFilePath = './'
SourceFileName = 'data2.xls'

# w = Workbook()
# ws = w.add_sheet ('Copied Cell')

count = 0

s = '서울'

for sheet_name, values in parse_xls(SourceFilePath+SourceFileName,'utf-8'):
   for row_idx, col_idx in sorted(values.keys()):
      v=values[(row_idx,col_idx)]
      print '(%d,%d)  ='%(row_idx,col_idx),v
      if (type(v) is unicode):
         if v.find(s)>=0:
            count=count + 1 #count
         #ws.write(row_idx,col_idx,v)

print s, '안에 소재한 대학교는', count, '입니다.'



count = 0

t = ['부산' , '광주' , '울산' , '인천' , '대구' , '대전']
for sheet_name, values in parse_xls(SourceFilePath+SourceFileName,'utf-8'):
   for row_idx, col_idx in sorted(values.keys()):
      v=values[(row_idx,col_idx)]
      print '(%d,%d)  ='%(row_idx,col_idx),v
      if (type(v) is unicode):
         if v.find(t[0])>=0:
            count=count + 1 #count
         #ws.write(row_idx,col_idx,v)

print t, '안에 소재한 대학교는', count, '입니다.'

count = 0

a = ['충남' , '충북' , '경기' , '강원' , '전남' , '전북' , '경남' , '경북' , '제주']
for sheet_name, values in parse_xls(SourceFilePath+SourceFileName,'utf-8'):
   for row_idx, col_idx in sorted(values.keys()):
      v=values[(row_idx,col_idx)]
      print '(%d,%d)  ='%(row_idx,col_idx),v
      if (type(v) is unicode):
         if v.find(a[0])>=0:
            count=count + 1 #count
         #ws.write(row_idx,col_idx,v)

print a, '안에 소재한 대학교는', count, '입니다.'
# w.save('copiedfile.xls')

# k = open('as.txt','w')

# t = 'asdasd'
# k.write(t+'\n'+'\n')

# k.close


# p = open('as.txt','a')

# e = 'coco'
# k.write(e)

# l=[1,2,3,4,66,2]
# for i in l:

# 	k.write(str(i)+'\n')

# p.close