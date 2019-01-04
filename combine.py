# -*- coding: utf-8 -*-


#Data files to be combined into one :
files = [
		'Data/corpus1/corpus.bcn.dev.ta.processed',
		'Data/corpus1/corpus.bcn.test.ta.processed',
		'Data/corpus1/corpus.bcn.train.ta.processed',
		'Data/wikipedia/alldata',
		'Data/corpus3'	
		]


#Output file name : 
outputfile = 'Data/alldata'


output = open(outputfile, 'w')
for file in files:
	text = open(file,'r').readlines()[0]
	output.write(text)
	output.write(" டம்மி டம்மி டம்மி டம்மி டம்மி\n")
output.close()



