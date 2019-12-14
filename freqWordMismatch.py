from neighbors import neighbors
from fasterFreqWords import patternToNum, numToPattern

from rosalindfunctions import fasterFreqWords



def freqWordsWithMismatch(patt, k, d):
    freqArray = [0] * (4 ** k)
    for i in range(len(patt) - k + 1):
        currKmer = patt[i:i+k]
        freqArray[patternToNum(currKmer)] += 1
        neighborList = neighbors(currKmer, d)

        for neighbor in neighborList:
            freqArray[patternToNum(neighbor)] += 1
    return freqArray



patt = 'ACGTTGCATGTCGCATGATGCATGAGAGCT'
k = 4
d = 0

print freqWordsWithMismatch(patt, k, d)
print fasterFreqWords(patt, k)