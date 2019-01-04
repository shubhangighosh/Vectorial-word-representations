# -*- coding: utf-8 -*-
import os

files = []
for x in ['AA', 'AB', 'AC', "AD", 'AE']:
	if x == 'AE':
		n = 17
	else:
		n = 100
	for i in range(n):
		if i < 10:
			file = x + "/wiki_0" + str(i)
		else:
			file = x + "/wiki_" + str(i)
		files.append(file)
		os.system("python process.py Data/wikipedia/tawiki/"+file)


#Output file name : 
outputfile = 'Data/wikipedia/alldata'


output = open(outputfile, 'w')
for file in files:
	text = open("Data/wikipedia/tawiki/"+file+'.processed','r').readlines()[0]
	output.write(text)
	output.write(" டம்மி டம்மி டம்மி டம்மி டம்மி ")
output.close()

