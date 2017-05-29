#-*- coding: utf-8 -*-
import json, requests, KdList

def query(type, postid):

	try:
		url = 'https://www.kuaidi100.com/query?type=%s&postid=%s' % (KdList.ns[type], postid)
		print url
		req = requests.get(url).text
		reply = json.loads(req)
		string = ''

	except Exception as e:
		raise e
		return -1

	if reply['message'] == u'ok':
		for i in reply['data']:
			string += ' '.join([i['ftime'], i['context']]) + '\n'
	else:
		string = reply['meaasge']
	
	return string

if __name__ == '__main__':
	
	print query(u'圆通',885149255189479946)
