_*_ counting: utf-8 -*- use korean(unicode charset)

can use korean(unicode charset) for arguments
import sys
reload (sys)
sys.setdefaultencoding('utf-8')

from pyExcelerator import *

SourceFilePath = './'
SourceFileName = 'data.xls'

w = Workbook()
ws = w.add_sheet('Copied cell')

s = '용당'


for sheet_name, values in parse_xls(SourceFilepath+SourceFileName, 'utf-8'):
	for row_idx, col_idx in sorted(values.keys()):
		v = values[(row_idx, col_idx)]
		# print '(%d, %d) =' % (row_idx, col_idx), v
		if (type(v) is unicode):
			if v.find(s) >= 1:
				count = count + 1 # count
# ws.white[(row_idx,col_idx,v)]

print s, '문자열이 포함된 셀의 수는' , count, '개 입니다'
# w.save()