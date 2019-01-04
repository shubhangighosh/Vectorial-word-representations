# Vectorial-word-representations  
Corpus collection and training word vectors  
  
############################################################  
THE THREE MODELS  
############################################################  
GloVe :     
1) cd to GloVe - "cd GloVe"  
2) ./glove.sh <vector_size>  
eg : "./glove.sh 50  
Other parameters can also be changed inside glove.sh  
vocab_GloVe.txt and vectors_GloVe.txt will be produced inside GloVe folder  

Skipgram :   
1) cd to Skipgram - "cd skipgram"  
2) ./skipgram.sh <vector_size>  
eg : "./skipgram.sh 50  
vectors_skipgram.txt will be produced inside skipgram folder  

CBOW :   
1) cd to GloVe - "cd cbow"  
2) ./cbow.sh <vector_size>  
eg : "./cbow.sh 50  
vectors_cbow.txt will be produced inside cbow folder  




############################################################  
EVALUATION  
############################################################  
1) 'word-sim-pairs-raw' file contains a test set of 30 pairs of words with average human similarity ratings. Correlation between human ratings and model ratings is measured by running :  
'python evaluate.py', which prints the Pearson and Spearman's coefficient of correlation for all three models  
2) Synonyms of a given word can be obtained by changing the input word inside evaluate.py and then running:  
'python evaluate.py > evaluation'  
3) Analogy equations can be solved by setting the equation words inside evaluate.py and then running:  
'python evaluate.py > evaluation'  
Top ten results are provided for the   



############################################################  
PREPROCESSING  
############################################################  
Process corpus data :   
Process text - Tokenize, remove numbers, unwanted characters and words  
argument 1 - raw data file  
produces <input file>.processed as output  
"python process.py <data_file>"  

Process wikipedia articles :   
Process all the wikipedia articles inside tawiki and combines them into a single file  
"python process_all_articles.py"  

Combine multiple data files into one:  
Appends 5 dummy words in between  
Set files to be combined and name of output file inside combine.py  
"python combine.py"  


All of this can be done by running './process_data.sh'.  




