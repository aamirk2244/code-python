import PyPDF2 
import nltk
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize 
from sklearn.feature_extraction.text import TfidfVectorizer
import numpy

# nltk.download('stopwords')

# open the slide named Lecture Set 2, for visual view of term document frequency and posting lists

def pdfRead(filename):
    pdfFileObj = open(filename,'rb') 
 
    pdfReader = PyPDF2.PdfFileReader(pdfFileObj) 

    num_of_pages = pdfReader.numPages 
    count = 0 
    text = "" 
    pageObj = None

    while count < num_of_pages: 
        pageObj = pdfReader.getPage(count) 
        count +=1 
        text += pageObj.extractText()                         # converting into text of characters
    return text
def findWordInDocx(givenWord, vec):
    rankThisWord =  givenWord
    toList = list(vec.get_feature_names())
    getIndexOfWord = -1
    try: 
        getIndexOfWord = toList.index(rankThisWord) 
    except:    
        print(' "{} " is not present in any of the documents'.format(rankThisWord))
        getIndexOfWord = -1
    return getIndexOfWord

def RankTheDocxWithSort():
     # print('found at this index -> ', getIndexOfWord)
    # print(vec.get_feature_names())
    rankedList= []
    rankDocx = {}
    for i in range(len(files)):
        rankedList.append(tfMatrix[i][getIndexOfWord])
    # print(rankedList)
    mx = -1
    saveIndex = 0
    for i in range(len(rankedList)):
        if rankedList[i] > 0: rankDocx[rankedList[i]] = files[i]           # saving all ranked doc in dictionary


    docSort = list(rankDocx)
    docSort.sort()
    # print('this is the max value ', mx)
    getMap = list(map(lambda onKey: rankDocx[onKey], docSort))
    # print(rankDocx)
    print('these are the list of documents in order of their ranking via Descending order(higest to lowest) on the basis of the given Query \n ', getMap)
    # print(rankedList)

    
def showMaxRankTermsInDocx(tfMatrix, vec, files):
    totalDox = len(tfMatrix)
    # print('total document are ------------- ', totalDox)
    maxInRows = list(numpy.amax(tfMatrix, axis=1))                    #  gertting all max in rows
    # print('Max value of every Row: ', maxInRows)
    
    for docNumber in range(totalDox):
        maxScore_in_doc =  list(tfMatrix[docNumber]).index(maxInRows[docNumber])                     # getting the index of max score value
        # print('word {} has maximum score in {}'.format(vec.get_feature_names()[maxScore_in_doc],files[docNumber] ))


files = ['myDocx.pdf', 'myDocx2.pdf', 'myDocxPdf3.pdf', 'myDocxPdf4.pdf', 'myDocxPdf5.pdf', 'myDocxPdf6.pdf', 'myDocxPdf7.pdf', 'myDocxPdf8.pdf', 'myDocxPdf9.pdf', 'myDocxPdf10.pdf']
# fileNameWithIndex = list(map(lambda file: files.index(file), files))
# print(fileNameWithIndex)
fileNameWithIndex = {}

fileIndexMap = [files.index(i) for i in files]
for file in range(len(files)):
    fileNameWithIndex[file+1] = files[file]
# print(fileNameWithIndex)

fileNameIndexMap = map(lambda fileName : files.index(fileName), files) 
readingPdfOneByOne = list(map(lambda file : pdfRead(file), files))           # calling to pdfRead function fol all files, this is shortcut
# print(readingPdfOneByOne)
vec = TfidfVectorizer(stop_words='english')
matrix  = vec.fit_transform(readingPdfOneByOne)

tfMatrix =  matrix.toarray()
# print('Sparse Matrix n', matrix.shape, "n",tfMatrix)

# maxScore_in_doc1 =  list(tfMatrix[0]).index(max(tfMatrix[0]))                     # getting the index of max score value
# print('index of max score value in doc1 is ', maxScore_in_doc1)
# print('word present at that index is ', vec.get_feature_names()[maxScore_in_doc1])

# maxScore_in_doc1 = max(tfMatrix[0])
showMaxRankTermsInDocx(tfMatrix, vec,files)
# print("************************")
givenWord  = 'facility'
getIndexOfWord = findWordInDocx(givenWord, vec)

if getIndexOfWord != -1:  RankTheDocxWithSort()
   
    # print(tfMatrix[1][266])

    # print(tfMatrix.shape)
