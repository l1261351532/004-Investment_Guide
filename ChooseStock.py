#coding=utf-8
"""
本函数实现了股票筛选功能。
使用get_today_all得到当日实时股票数据，运行成本高
过滤出市盈率在0-30倍之间，且今日换手率>1%，涨幅超2%的股票。
之后统计今日涨停和接近涨停的股票。


"""
import pandas as pd
import tushare as ts
import numpy as np

e=ts.get_today_all()
code=e[u'code']
name = e[u'name']
per = e[u'per'] # 市盈率
tt = e[u'turnoverratio']	# 换手率
cc = e[u'changepercent']	# 涨跌幅
mm = e[u'mktcap']	# 总市值
idx = len(name)
total = 0
while idx > 0:
	idx -= 1
    #选择市盈率在0-30倍之间，且今日换手率>1%，涨幅超2%的
	if per[idx] < 30 and per[idx] > 0 and tt[idx] > 1 and cc[idx] > 2:
		print (code[idx],' ',name[idx],":",per[idx],":",tt[idx],":",cc[idx],":",mm[idx]/10000)
		total += 1
print("total:",total,"/",len(name))

idx = len(name)
total = 0
print("涨停股票：")
while idx > 0:
	idx -= 1
	# 涨停股票
	if cc[idx] > 9.5:
		total += 1
		print (code[idx],":",name[idx],":",cc[idx])