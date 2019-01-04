# -*- coding: utf-8 -*-
from langdetect import detect
import sys, os


infile = sys.argv[1]
outfile = infile + ".processed"
tempfile = 'temp.ta'
tokenfile = 'tokens.ta'

os.system('python indic_lib/src/indicnlp/normalize/indic_normalize.py ' + infile + ' ' + tempfile + ' ta')
os.system('python indic_lib/src/indicnlp/tokenize/indic_tokenize.py ' + tempfile + ' ' + tokenfile + ' ta')

tokenlines = open(tokenfile, 'r').readlines()
outlines = open(outfile, 'w')
for line in tokenlines[:]:
	processed_line = ""
	for token in line.strip().split():
		if token == '.':
			processed_line += "\n"
		elif len(token) > 3 and not any(c.isdigit() for c in token):
			try:
				if(detect(token.decode('utf-8')) == 'ta'):
					processed_line += token + " "
			except:
				print("Unknown token", token)

	outlines.write(processed_line)

outlines.close()
os.system('rm tokens.ta')
os.system('rm temp.ta')







