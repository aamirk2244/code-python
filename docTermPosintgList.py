import PyPDF2 
import nltk
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize 
# nltk.download('stopwords')

# open the slide named Lecture Set 2, for visual view of term document frequency and posting lists

def pdfRead(filename):
    pdfFileObj = open(filename,'rb') 
 
    pdfReader = PyPDF2.PdfFileReader(pdfFileObj) 

    num_of_pages = pdfReader.numPages 
    count = 0 
    text = "" 

    while count < num_of_pages: 
        pageObj = pdfReader.getPage(count) 
        count +=1 
        text += pageObj.extractText()                         # converting into text of characters
    
    tokens = word_tokenize(text) 
 
    punctuations = ['(',')',';',':','[',']',',', '.', '-']                   # removing these stop words

    # keywords = [word for word in tokens if not word in punctuations] 
    tokens_without_sw = [word for word in tokens if  not word in punctuations]           # removing stopwords
    

    
    return tokens_without_sw
def generatePostingList(docList):
    termWithpostingList = {}                # {'sample': [2,[2,3]]}              # means sample occured in 2 documents named as 2 and 3
    
    indexDoc = 0
    for pdf in docList:
        indexDoc += 1                 # starting document index from 1
        for word in pdf:
            if termWithpostingList.get(word) is  None: termWithpostingList[word] = [1,[indexDoc]]    # occurs 1 time in document (index document) 
            else:
                termWithpostingList[word][0] += 1                  # incrementing occurence
                termWithpostingList[word][1].append(indexDoc)         # appending document name (i.e index)
    print('printing terms with posting lists ********** ')
    return termWithpostingList
            

def saveDocTermIndex(docTextList):
    totalPdf = len(docTextList)
    
    for pdf in docTextList: 
        pdf.sort()                   # sorting alphabetically
        # print('sorting alphabetically ............. ')
      
        for word in pdf:            # working on the sorted pdf
            while(pdf.count(word) != 1): pdf.remove(word)                  #(while all duplicate words remove)  removing duplicate words, pdf.count(word) return the count of given word 
            
            
    
        # print(pdf)
        
    return generatePostingList(docTextList)          # documnet text list
        
        # now if pdf word is not presetnt words
    
def findWordInDoc(word, docTextList, docName):
#     
    
        
    
    print('findWordInDoc called')
    print('printing posting list ------->> ', docTextList[word])
    postingList = docTextList[word]
    output ='The word "' + word+ ' " occured in the following documents -> ' 
    for i in range(postingList[0]):                        # posting[0] contain the frequency of documnet
            output += docName[postingList[1][i]] 
    
    print(output)

files = ['sample.pdf', 'sample2.pdf']
# fileNameWithIndex = list(map(lambda file: files.index(file), files))
# print(fileNameWithIndex)
fileNameWithIndex = {}

fileIndexMap = [files.index(i) for i in files]
for file in range(len(files)):
    fileNameWithIndex[file+1] = files[file]
print(fileNameWithIndex)

fileNameIndexMap = map(lambda fileName : files.index(fileName), files) 
readingPdfOneByOne = list(map(lambda file : pdfRead(file), files))           # calling to pdfRead function fol all files, this is shortcut

k = saveDocTermIndex(readingPdfOneByOne)
# print(k)
find_word = 'Course'                # let's check if this word is present in the doc1 or doc2
findWordInDoc(find_word,k,fileNameWithIndex )                   # finding word in document
