# -*- coding: utf-8 -*-
import numpy
from scipy.stats import spearmanr, pearsonr
import operator

#############################################################################################################
#############################################################################################################
#Load all vector representations

#LOAD GLOVE VECTORS
glove = {}
model = 'GloVe'
lines = open(model+'/vectors_'+model+'.txt').readlines()
for line in lines:
	tokens = line.strip().split()
	glove[tokens[0].decode('utf-8')] = [float(e) for e in tokens[1:]]

#LOAD SKIPGRAM VECTORS
skipgram = {}
model = 'skipgram'
lines = open(model+'/vectors_'+model+'.txt').readlines()[1:]
for line in lines:
	tokens = line.strip().split()
	skipgram[tokens[0].decode('utf-8')] = [float(e) for e in tokens[1:]]

#LOAD CBOW VECTORS
cbow = {}
model = 'cbow'
lines = open(model+'/vectors_'+model+'.txt').readlines()[1:]
for line in lines:
	tokens = line.strip().split()
	cbow[tokens[0].decode('utf-8')] = [float(e) for e in tokens[1:]]



#############################################################################################################
#############################################################################################################
#Utility functions


#Get similarity between two words for a certain model
def similarity(word1, word2, modelvec):
	v1 = numpy.array(modelvec[word1])
	v2 = numpy.array(modelvec[word2])
	return numpy.dot(v1, v2)/(numpy.linalg.norm(v1)*numpy.linalg.norm(v2))
	


#WORD SIMILARITY - MODEL COMPARISON
def correlation(list1, list2):
	return (pearsonr(list1, list2)[0], spearmanr(list1, list2)[0])

def model_correlation():
	word_sim_pairs = open('word-sim-pairs-human', 'r').readlines()
	real_sim = []
	model1_sim = []
	# model2_sim = []
	# model3_sim = []

	# outfile = open('word-sim-pairs-models', 'w')
	# outfile.write('Word1 Word2 GloVe Skipgram Cbow\n')

	for word_sim_pair in word_sim_pairs[1:]:
		(word1, word2, sim) = word_sim_pair.strip().split()
		real_sim.append(float(sim))
		sim1 = similarity(word1.decode('utf-8'), word2.decode('utf-8'), glove)*10
		# sim2 = similarity(word1.decode('utf-8'), word2.decode('utf-8'), skipgram)*10
		# sim3 = similarity(word1.decode('utf-8'), word2.decode('utf-8'), cbow)*10
		model1_sim.append(sim1)
		# model2_sim.append(sim2)
		# model3_sim.append(sim3)	
	# 	outfile.write(word1 + " " + word2 + " " + sim + " " + str(sim1) + " " + str(sim2) + " " +  str(sim3) + "\n")
	# outfile.close()

	c1 = correlation(real_sim, model1_sim)
	print "Correlation with GloVe : Pearson -", c1[0],  ", Spearman's -", c1[1]
	# c2 = correlation(real_sim, model2_sim)
	# print "Correlation with skipgram : Pearson -", c2[0],  ", Spearman's -", c2[1]
	# c3 = correlation(real_sim, model3_sim)
	# print "Correlation with cbow : Pearson -", c3[0],  ", Spearman's -", c3[1]



#SYNONYMS
def n_most_similar(root_word, n, modelvec):
	sim_words = {}
	for word, vec in modelvec.items():
		if word != root_word.decode('utf-8'):
			sim_words[word] = similarity(root_word.decode('utf-8'), word, modelvec)
	#Sort word similarities and print top n words
	sorted_sims = sorted(sim_words.items(), key=operator.itemgetter(1), reverse=True)
	return sorted_sims[:n]


#SEMANTIC ANALOGY
def closest_to(a, b, c, modelvec):	
	d_vec = numpy.array(modelvec[b]) + numpy.array(modelvec[c]) - numpy.array(modelvec[a])
	sim_words = {}
	for word, vec in modelvec.items():
		if(word != a and word != b and word != c):
			w_vec = numpy.array(modelvec[word])
			sim_words[word] = numpy.dot(w_vec, d_vec)/(numpy.linalg.norm(w_vec)* numpy.linalg.norm(d_vec))
	
	sorted_sims = sorted(sim_words.items(), key=operator.itemgetter(1), reverse=True)
	return sorted_sims[:10]



#############################################################################################################
#############################################################################################################
#Evaluation measures, described in README


# #1 CORRELATION
# #Calculate correlations of word pair similarities for each model
model_correlation()



#2 SYNONYMS - comment out while evaluating
#Return n most similar words to x
# x = 'பயம்' 	#Words to find synonyms for
# n = 10 			#Number of synonyms to find
# print("\nSynonyms of " + x + ":\n")
# for synonym in n_most_similar(x, 10, glove):
# 	print(synonym[0].encode('utf-8'))




# #3 SEMANTIC ANALOGY - comment out while evaluating
# #Find word closest to b + c - a
# a = 'ஆண்'
# b = 'பெண்'   
# c = 'மகன்'		  
# print("\nSemantic Analogy :- " + b + " + " + c + " - " + a + " :\n")
# for analogy in closest_to(a.decode('utf-8'),b.decode('utf-8'),c.decode('utf-8'),glove):
# 	print(analogy[0].encode('utf-8'))



