import re
import pickle
import math
import pandas as pd
import numpy as np

def voc(x):
    regx=re.compile(r"""[A-a-Z-z]+""")
    resultAll = regx.findall(x)
    resultUnique = list(set(resultAll))
    return [resultAll,resultUnique]
def vocfreq(x):
    regx=re.compile(r"""[A-a-Z-z]+""")
    resultAll = regx.findall(x)
    resultUnique = list(set(resultAll))
    freq=[resultAll.count(x) for x in resultUnique]
    freqVoc=pandas.DataFrame({"Word":resultUnique,"Freq":freq})
    return freqVoc

def pickleData(a,name):
    with open(name+'.pickle', 'wb') as handle:
        pickle.dump(a, handle, protocol=pickle.HIGHEST_PROTOCOL)

def loadPickle(a):
    with open(a, 'rb') as handle:
        return pickle.load(handle)
    
def readBook(a):
    with open(a, encoding="utf8") as file:
        return file.read()
def mostFreqWord(dic):
    for (k,v) in dic.items():
        if v == max(freqVocDic.values()):
            return k
