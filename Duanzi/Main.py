import cPickle, time, os, requests, random, re

LastUpdate = None
duanzi = []
data = {}

def CheckTime():
	global data, duanzi, LastUpdate
	now = time.time()
	if now - LastUpdate >= 60:
		return 1
	else:
		return 0 

def Read():
	global data, duanzi, LastUpdate
	file = open('duanzi.txt', 'r')
	data = cPickle.load(file)
	LastUpdate = data['LastUpdate']
	duanzi = data['duanzi']
	file.close()

def Save():
	global data, duanzi, LastUpdate
	file = open('duanzi.txt', 'w')
	data['duanzi'] = duanzi
	data['LastUpdate'] = LastUpdate
	cPickle.dump(data, file)
	file.close()

def Update():
	global data, duanzi, LastUpdate
	LastUpdate = time.time()
	url = 'https://www.qiushibaike.com/text/page/' + str(random.randint(1, 30)) + '/'
	res = requests.get(url).text
	pattern = r'<span>(.*?)</span>'
	duanzi = re.findall(pattern, res)[:21]
	for i in duanzi:
		i = i.replace('</br>', '\n').replace('<br/>', '\n')

def GetDuanzi():
	global data, duanzi, LastUpdate
	if not os.path.exists('duanzi.txt'):
		Update()
		Save()
	else:
		Read()
	if CheckTime() == 1:
		Update()
		Save()
	return duanzi

if __name__ == '__main__':

	t = GetDuanzi()
	print t