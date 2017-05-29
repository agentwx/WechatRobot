#-*- coding: utf-8 -*-
import requests, json, StationList

def query(From, To, Date):
	
	if StationList.s.get(From) == None or StationList.s.get(To) == None:
			return -1

	try:
		url = 'https://kyfw.12306.cn/otn/leftTicket/query?'
		url += 'leftTicketDTO.train_date=%s' % Date
		url += '&' + 'leftTicketDTO.from_station=%s' % StationList.s[From]
		url += '&' + 'leftTicketDTO.to_station=%s' % StationList.s[To]
		url += '&purpose_codes=ADULT'
	
		req = requests.get(url, verify=False).text
		reply = json.loads(req)
		mp = reply['data']['map']
		ticket_list = []
		
	except Exception as e:
		raise e
		return -1

	for i in reply['data']['result']:
		t = i.split('|')
		t = [t[3]] + t[6:10]
		t[1] = mp[t[1]]
		t[2] = mp[t[2]]
		ticket_list.append(t)
	
	return ticket_list

if __name__ == '__main__':
	
	#print station.s
	a = u'哈尔滨'
	b = u'北京'
	c = u'2017-05-25'
	replys = query(a, b, c)
	print replys
	#print query('北京', '上海', '2017-05-20')