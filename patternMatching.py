from helperFileFunctions import *
from rosalindfunctions import t1k


# find the edit distance between two strings just using deletions
def hammingDistance(s1, s2):
    dist = 0
    for i in range(len(s1)):
        if s1[i] != s2[i]:
            dist += 1

    return dist


# find the number of occurences of a pattern in a larger string with at most hamming distance of d
def approxPatternMatch(pat, s, d):
    k = len(pat)
    occurIndex = []
    for i in range(len(s)-len(pat) - 1):
        if hammingDistance(s[i:i+k], pat) <= d:
            occurIndex.append(i)
    return occurIndex


# find the most frequent kmer with up to d mismatches
def freqWordsWMismatch(text, k, d):
    freqArray = t1k(text, k)





args = getArgs('1h')

writeList(approxPatternMatch(args[0], args[1], args[2]))




