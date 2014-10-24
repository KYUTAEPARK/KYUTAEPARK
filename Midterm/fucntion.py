# -*- coding: utf-8 -*- # us Korean (unicode charset)

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
s = '대학교'
for sheet_name, values in parse_xls(SourceFilePath+SourceFileName, 'utf-8'):
	for row_idx, col_idx in sorted(values.keys()):
		v = values[(row_idx, col_idx)]
		# print '(%d, %d) =' % (row_idx, col_idx), v
		if (type(v) is unicode):
tmp = str(v)
if tmp.find(s) >= 0:
count = count + 1 # count
# ws.write(row_idx,col_idx,v)
print s, '' , count, '.'
# w.save('copiedfile.xls')