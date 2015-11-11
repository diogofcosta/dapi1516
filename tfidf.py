import math
import sys
import os
from textblob import TextBlob

def tf(word, blob):
    return blob.words.count(word) / len(blob.words)

def n_containing(word, bloblist):
    return sum(1 for blob in bloblist if word in blob)

def idf(word, bloblist):
    return math.log(len(bloblist) / (1 + n_containing(word, bloblist)))

def tfidf(word, blob, bloblist):
    return tf(word, blob) * idf(word, bloblist)

docentes = 'C:/Users/Diogo/Documents/myProjects/DAPIDb/dapi1516/Docentes'
docentesStats = open('Docentes/aaDocentesStats.txt', 'w')

for subdir, dirs, files in os.walk(docentes):
    for file in files:
        path = 'Docentes/'+file
        content = open(path).read()
        blob = TextBlob(content)
        for word in blob.words:
            score = tf(word,blob)
            docentesStats.write('Word: ')
            docentesStats.write(word)
            docentesStats.write(' -- TF: ')
            docentesStats.write(str(score))
            docentesStats.write('\n')

docentesStats.close()

"""
docentesStats = open('Docentes//aaDocentesStats.txt', 'w')
publicoStats = open('NoticiasPublico\\aaPublicoStats.txt', 'w')
ucsStats = open('NoticiasTsf\\aaUcsStats.txt', 'w')
tsfStats = open('Ucs\\aaTsfStats.txt', 'w')

for file in os.walk(docentes):
    if file.endswith(".txt") : 
        document = tb(file.read())
        for word in document.words:
            score = tf(word,document.words)
            docentesStats.write('Word: ')
            docentesStats.write(word)
            docentesStats.write(' -- TF: ')
            docentesStats.write(score)
            docentesStats.write('\n')
        continue
    else:
        continue

docentesStats.close()
publicoStats.close()
ucsStats.close()
tsfStats.close()
"""