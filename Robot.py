#-*- coding: utf-8 -*-
import requests, json, itchat, random
import TrainTicketQuery.Main, KdQuery.Main, Duanzi.Main
from itchat.content import *


@itchat.msg_register(TEXT)
def robot_talk(msg):

	info = msg['Text']
	replys = None
	temp = info.split(' ')
	print info

	if temp[0] == u'帮助' or temp[0] == u'help':
		replys = u'目前支持的命令:\n'
		replys += u'[0] “其他” 机器人陪聊 QWQ\n'
		replys += u'[1] “hcp 出发地 目的地” 时间(例如:"hcp 北京 上海 2017-05-20")\n查询火车票信息\n'
		replys += u'[2] “kd 快递公司 快递号”(例如:"kd 京东 53971178602")\n查询快递信息\n'
		replys += u'[3] “dz”\n获取一条段子\n”'

	elif temp[0] == u'hcp':
		try:
			replys = TrainTicketQuery.Main.query(temp[1], temp[2], temp[3])
		except Exception as e:
			print e
			replys = -1

		if replys != -1:
			form = []
			for i in replys:
				form.append(' '.join(i))
			replys = '\n'.join(form)

	elif temp[0] == u'kd':
		print temp[1], temp[2]
		try:
			replys = KdQuery.Main.query(temp[1], temp[2])
		except Exception as e:
			print e
			replys = -1

	elif temp[0] == u'dz':
		replys = Duanzi.Main.GetDuanzi()[random.randint(0,20)]

	else:
		url = 'http://www.tuling123.com/openapi/api'
		key = 'dfa39cc9aa114b72820dfc06ff57e101'
		data = {'key': key, 'info': info}
		req = requests.post(url, data).text
		replys = json.loads(req)['text']
		print info, replys, msg['FromUserName']
	
	if replys == -1:
		replys = 'Error!'

	print replys
	return replys

itchat.auto_login()
itchat.run()
