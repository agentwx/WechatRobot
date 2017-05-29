#-*- coding: utf-8 -*-
import re

file = open('list.txt')
output_file = open('kd_list.pt', 'w')
string = file.read()
pattern = ur'<a data-code="(.+?)">(.+?)</a>'
t = re.findall(pattern, string)
s = {}
ns = {}
for i in t:
	key, value = (i[0].decode('utf-8'), i[1].decode('utf-8'))
	s[key] = value
	ns[value] = key
print 's =', s
print 'ns =', ns