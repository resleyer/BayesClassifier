import string, sys, random, array,  numpy

def loadDataSet():
    postingList=[['my', 'dog', 'has', 'flea', \
                          'problems', 'help', 'please'],
                         ['maybe', 'not', 'take', 'him', \
                          'to', 'dog', 'park', 'stupid'],
                         ['my', 'dalmatian', 'is', 'so', 'cute', \
                           'I', 'love', 'him'],
                         ['stop', 'posting', 'stupid', 'worthless', 'garbage'],
                         ['mr', 'licks', 'ate', 'my', 'steak', 'how',\
                           'to', 'stop', 'him'],
                         ['quit', 'buying', 'worthless', 'dog', 'food', 'stupid']]
    classVec = [0,1,0,1,0,1]
    return postingList,classVec

def createVocabList(dataSet):
    vocabSet = set([])
    for document in dataSet:
        vocabSet = vocabSet | set(document)
    return list(vocabSet)

def setOfWords2Vec(vocabList, inputSet):
    returnVec = [0] * len(vocabList)
    for word in inputSet:
        if word in vocabList:
            returnVec[vocabList.index(word)] = 1
        else:
            print "the word %s is not in the Vocabulary!" % word
    return returnVec

def trainNB0 (trainMatrix, trainCategory):
    numTrainDocs = len(trainMatrix)
    numWords = len(trainMatrix[0])
    pAbusive = sum(trainCategory)/float(numTrainDocs)
    p0Num = numpy.ones(numWords); p1Num = numpy.ones(numWords)
    p0Denom = 0.0; p1Denom = 0.0
    for i in range(numTrainDocs):
        if trainCategory[i] == 1:
            p1Num += trainMatrix[i]
            p1Denom += sum(trainMatrix[i])
        else:
            p0Num += trainMatrix[i]
            p0Denom += sum(trainMatrix[i])
        print trainMatrix[i]

    print "CCCC"    
    print p1Num
    print p1Denom
    print pAbusive
    p1Vect = numpy.log10(p1Num/p1Denom)
    p0Vect = numpy.log10(p0Num/p0Denom)
    print p1Vect
    
    return p0Vect,p1Vect,pAbusive


def classifyNB(vec2Classify, p0Vec, p1Vec, pClass1):
    p1 = sum(vec2Classify * p1Vec) + numpy.log10(pClass1)  #this is addition because we are dealing with logs
    p0 = sum(vec2Classify * p0Vec) + numpy.log10(1.0 - pClass1)
    print p1
    print p0
    if p1 > p0 :
        return 1
    else:
        return 0
    
    
def main():
    p,c = loadDataSet()
    v = createVocabList(p)
    tm = []
    for d in p:
        tm.append(setOfWords2Vec(v,d))
    
    p0V, p1V , pAb = trainNB0(tm,c)  
    
    testEntry = ['love', 'my', 'stupid' , 'dalmatian']
    
    thisDoc = setOfWords2Vec(v, testEntry)
    
    print testEntry, ' classified as: ' , classifyNB(thisDoc, p0V, p1V, pAb)
    
    testEntry = ['stupid', 'garbage']
    thisDoc = setOfWords2Vec(v, testEntry)
    
    print testEntry, ' classified as: ' , classifyNB(thisDoc, p0V, p1V, pAb)
    
    


    
