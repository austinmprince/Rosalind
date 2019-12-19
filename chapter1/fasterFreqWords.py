from time import time
from helperFileFunctions import *


# convert symbol to number to be used in pattern to num
# helper function for patternToNum
def symbolToNum(s):
    vals = {'A': 0, 'C': 1, 'G': 2, 'T': 3}
    return vals[s]


# convert number to symbol to be used in number to pattern
# helper function for numToPattern
def numToSymbol(num):
    vals = {0: 'A', 1: 'C', 2: 'G', 3: 'T'}
    return vals[num]

# BA1L on Rosalind
# used to generate a frequency array
def patternToNum(pat):
    if len(pat) == 0:
        return 0
    pref = pat[:-1]

    sVal = symbolToNum(pat[-1])

    return (4 * patternToNum(pref)) + sVal

# BA1M on Rosalind
# Used in return frequent kmers once we have calculated the most frequent frequency array
def numToPattern(num, k):
    if k == 1:
        return numToSymbol(num)
    quot = num / 4
    rem = num % 4
    lastChar = numToSymbol(rem)
    return numToPattern(quot, k - 1) + lastChar



# BA1K on Rosalind
def getFrequencies(s, k):
    # create a frequency array of 4^k elements
    freqArray = [0] * (4 ** k)
    for i in range(len(s) - k + 1):
        # go through every k-mer and if that value occurs in the input string then increment the element at that index
        # in the freqArray
        freqArray[patternToNum(s[i:i+k])] += 1
    # return frequency array
    return freqArray

def fasterFreqWords(s, k):
    freqArray = getFrequencies(s, k)
    currMax = 0
    mostFreq = []
    for element in freqArray:
        if element > currMax:
            currMax = element
    for i in range(len(freqArray)):
        if freqArray[i] == currMax:
            mostFreq.append(numToPattern(i, k))

    return mostFreq


# given l - window size, k - length of kmer, t - number of times k-mer must appear, s - input string
# find the k-mers that form a clump of at least t occurences in a window of size l
# slow because we generate a new frequency array at each step, this is unnecessary
# we could simply generate on frequency array and look in the window every time that is of interest
# Answer correct
def clumpFinding(s, k, l, t):
    # loop from 0 to the final window with an increment of k
    clumps = []
    for i in range(0, len(s) - l + 1):


        #get the frequency array of the sub window
        subWindowFreqArray = getFrequencies(s[i:i+l], k)

        for i in range(len(subWindowFreqArray)):
            if subWindowFreqArray[i] >= t:
                freqWord = numToPattern(i, k)
                if freqWord not in clumps:
                    clumps.append(freqWord)
    return clumps

# doesnt work
# want to remove the first kmer from the freq array and then add the last kmer that is being added to the
# window to the freq array
# problem is that it is not updating frequency array correctly

# this clump finding algorithm ignores the reverse complimentary nature of DNA
# we are only looking for occurences of a string S in our windows not the reverse compliment of that string S'
# which would also be instructive in finding the DnaA box
# Rosalind BA1E
def fasterClumpFinding(s, k, l, t):
    freqArray = getFrequencies(s[:l], k)
    clumps = [0] * (4 ** k)
    freqClumpString = []
    for j in range(len(freqArray)):
            if freqArray[j] >= t:
                clumps[j] = 1

    for i in range(0, len(s) - l + 1):
        # print i
        # check if there is a kmer in the freq array that has a higher value than t if so
        # add to the clumps array

        # subtract the first kmer from the frequency array
        firstKMer = patternToNum(s[i:i+k])
        freqArray[firstKMer] -= 1

        # add the last kmer to the frequency array or increase its frequency by 1
        # last kmer goes from index i + l - k to i + l do this out on paper to figure out
        lastKMer = patternToNum(s[i+l-k:i+l])
        freqArray[lastKMer] += 1
        if freqArray[lastKMer] >= t:
            clumps[lastKMer] = 1


    for i in range(len(clumps)):
        if clumps[i] == 1:

            freqClumpString.append(numToPattern(i, k))

    return freqClumpString






