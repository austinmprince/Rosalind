from neighbors import neighbors
from fasterFreqWords import patternToNum, numToPattern, getFrequencies
from rosalindfunctions import retComps
from helperFileFunctions import writeList


#BA1J this works
# dont generate frequency array at the beginning or it would double/more than once count for kmers that appear in the string
# as a kmer is a dneighbor of itself (it has a hamming distance of 0 so thus is included in the neighbors)
# basically go through each kmer and generate the d neighborhood of the kmer and then add that to the frequency array
# then same process to find the max of the frequency array
def freqWordsWMismatch(text, k, d):
    freqArr = [0] * (4 ** k)
    for i in range(len(text) - k + 1):
        neighborhood = neighbors(text[i:i+k], d)
        for neighbor in neighborhood:
            freqArr[patternToNum(neighbor)] += 1
    currMax = max(freqArr)
    maxKmers = []
    for i in range(len(freqArr)):
        if freqArr[i] == currMax:
            maxKmers.append(numToPattern(i, k))
    return maxKmers

# Want to find the the kmers that maximize count of pattern and count'rev
# BA1J BA Rosalind
def freqWordsWMismatchComplement(text, k, d):
    freqArr = [0] * (4 ** k)
    for i in range(len(text) - k + 1):
        textStr = text[i:i+k]
        textRev = retComps(textStr)
        neighborhood = neighbors(textStr, d)
        neighborhoodRevComp = neighbors(textRev,d)
        for neighbor in neighborhood:
            freqArr[patternToNum(neighbor)] += 1
        for neighbor in neighborhoodRevComp:
            freqArr[patternToNum(neighbor)] += 1


    currMax = max(freqArr)
    maxKmers = []
    for i in range(len(freqArr)):
        if freqArr[i] == currMax:
            maxKmers.append(numToPattern(i, k))
    return maxKmers


s = 'CCTCAACGAACTTAAAAACCTCAACGAAGCAGGCCCCAGCAGGCCCCACTTAAAAAACTTAAAAAACTTCCATAAGCAGGCCCCCCTCAACGAAGCAGGCCCCACTTCCATACCTCAACGATTCAGGGATTTCAGGGATACTTCCATAACTTAAAAAACTTCCATAACTTCCATACCTCAACGAACTTCCATACCTCAACGAACTTAAAAAAGCAGGCCCCAGCAGGCCCCACTTCCATAACTTAAAAAACTTCCATAACTTCCATAACTTCCATAACTTCCATATTCAGGGATACTTCCATAACTTCCATAACTTCCATACCTCAACGAACTTCCATAACTTAAAAAACTTAAAAAAGCAGGCCCCTTCAGGGATACTTCCATATTCAGGGATCCTCAACGACCTCAACGAACTTCCATATTCAGGGATTTCAGGGATAGCAGGCCCCTTCAGGGATACTTCCATAACTTCCATAAGCAGGCCCCTTCAGGGATTTCAGGGATAGCAGGCCCCACTTAAAAAACTTCCATACCTCAACGATTCAGGGATAGCAGGCCCCACTTCCATACCTCAACGAACTTAAAAACCTCAACGACCTCAACGAACTTAAAAAAGCAGGCCCCCCTCAACGATTCAGGGATAGCAGGCCCCACTTCCATATTCAGGGATACTTCCATAACTTCCATAACTTAAAAACCTCAACGACCTCAACGAAGCAGGCCCCCCTCAACGAAGCAGGCCCCTTCAGGGATACTTAAAAAACTTCCATAACTTCCATACCTCAACGAACTTCCATACCTCAACGAAGCAGGCCCCACTTCCATAAGCAGGCCCCACTTAAAAAACTTAAAAAACTTCCATAAGCAGGCCCCAGCAGGCCCCAGCAGGCCCCCCTCAACGAACTTCCATA'
k = 6
d = 2

writeList(freqWordsWMismatchComplement(s, k, d))

