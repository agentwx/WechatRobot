#-*- coding: utf-8 -*-

f = open('station.txt')
s = { }
for i in f:
	t = i.split(' ')
	s[t[0].decode('utf-8')] = t[1].replace('\n', '')

print 's = ', s