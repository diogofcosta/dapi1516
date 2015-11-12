import math
import sys
import os
import operator
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
ucs = 'C:/Users/Diogo/Documents/myProjects/DAPIDb/dapi1516/Ucs'
tsf = 'C:/Users/Diogo/Documents/myProjects/DAPIDb/dapi1516/NoticiasTsf'
publico = 'C:/Users/Diogo/Documents/myProjects/DAPIDb/dapi1516/NoticiasPublico'
docentesStats = open('Docentes/fullDocentesStats.txt', 'w')
ucsStats = open('Ucs/fullUcsStats.txt', 'w')
tsfStats = open('NoticiasTsf/fullTSFStats.txt', 'w')
publicoStats = open('NoticiasPublico/fullPublicoStats.txt', 'w')
fileStopWords = open("stopwords.txt") 
listStopWords = fileStopWords.read().splitlines()

num_files = 0

bloblist = []

for subdir, dirs, files in os.walk(docentes):
    for file in files:
        path = 'Docentes/'+file
        content = open(path).read()
        blob = TextBlob(content)
        bloblist.append(blob)
        num_files += 1

for subdir, dirs, files in os.walk(ucs):
    for file in files:
        path2 = 'Ucs/'+file
        content = open(path2).read()
        blob = TextBlob(content)
        bloblist.append(blob)
        num_files += 1

for subdir, dirs, files in os.walk(publico):
    for file in files:
        path3 = 'NoticiasPublico/'+file
        content = open(path3).read()
        blob = TextBlob(content)
        bloblist.append(blob)
        num_files += 1

for subdir, dirs, files in os.walk(tsf):
    for file in files:
        path4 = 'NoticiasTsf/'+file
        content = open(path4).read()
        blob = TextBlob(content)
        bloblist.append(blob)
        num_files += 1
"""
for subdir, dirs, files in os.walk(docentes):
    for file in files:
        path = 'Docentes/'+file
        content = open(path).read()
        blob = TextBlob(content)
        docentesStats.write('\n%r :\n' % (file))
        listRepeatWords = []
        d = {}
        scoresToSort = {word: tfidf(word,blob,bloblist) for word in blob.words}
        sorted_words = sorted(scoresToSort.items(), key=lambda x: x[1], reverse=True)
        for word, score in sorted_words:
            if word in listStopWords:
                continue
            if word not in listRepeatWords:
                listRepeatWords.append(word)
                scoreTF = tf(word,blob)
                scoreNContaining = n_containing(word,bloblist)
                scoreIDF = idf(word,bloblist)
                scoreTFIDF = scoreTF * scoreIDF
                docentesStats.write('Word: %r -- TF: %r -- n_times: %r -- idf: %r -- TF-idf: %r \n' % (word,scoreTF,scoreNContaining,scoreIDF,scoreTFIDF))
            else:
                continue
"""
docentesStats.close()

for subdir, dirs, files in os.walk(ucs):
    for file in files:
        path = 'Ucs/'+file
        content = open(path).read()
        blob = TextBlob(content)
        ucsStats.write('\n%r :\n' % (file))
        listRepeatWords = []
        for word in blob.words:
            if word in listStopWords:
                continue
            if word not in listRepeatWords:
                listRepeatWords.append(word)
                scoreTF = tf(word,blob)
                scoreNContaining = n_containing(word,bloblist)
                scoreIDF = idf(word,bloblist)
                scoreTFIDF = scoreTF * scoreIDF
                ucsStats.write('Word: %r -- TF: %r -- n_times: %r -- idf: %r -- TF-idf: %r \n' % (word,scoreTF,scoreNContaining,scoreIDF,scoreTFIDF))
            else:
                continue

ucsStats.close()

for subdir, dirs, files in os.walk(tsf):
    for file in files:
        path = 'NoticiasTsf/'+file
        content = open(path).read()
        blob = TextBlob(content)
        tsfStats.write('\n%r :\n' % (file))
        listRepeatWords = []
        for word in blob.words:
            if word in listStopWords:
                continue
            if word not in listRepeatWords:
                listRepeatWords.append(word)
                scoreTF = tf(word,blob)
                scoreNContaining = n_containing(word,bloblist)
                scoreIDF = idf(word,bloblist)
                scoreTFIDF = scoreTF * scoreIDF
                tsfStats.write('Word: %r -- TF: %r -- n_times: %r -- idf: %r -- TF-idf: %r \n' % (word,scoreTF,scoreNContaining,scoreIDF,scoreTFIDF))
            else:
                continue

tsfStats.close()

for subdir, dirs, files in os.walk(publico):
    for file in files:
        path = 'NoticiasPublico/'+file
        content = open(path).read()
        blob = TextBlob(content)
        publicoStats.write('\n%r :\n' % (file))
        listRepeatWords = []
        for word in blob.words:
            if word in listStopWords:
                continue
            if word not in listRepeatWords:
                listRepeatWords.append(word)
                scoreTF = tf(word,blob)
                scoreNContaining = n_containing(word,bloblist)
                scoreIDF = idf(word,bloblist)
                scoreTFIDF = scoreTF * scoreIDF
                publicoStats.write('Word: %r -- TF: %r -- n_times: %r -- idf: %r -- TF-idf: %r \n' % (word,scoreTF,scoreNContaining,scoreIDF,scoreTFIDF))
            else:
                continue

publicoStats.close()