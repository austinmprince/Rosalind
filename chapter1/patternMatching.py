from helperFileFunctions import *



# find the edit distance between two strings just using deletions
# BA1E
def hammingDistance(s1, s2):
    dist = 0
    for i in range(len(s1)):
        if s1[i] != s2[i]:
            dist += 1

    return dist


# find the number of occurences of a pattern in a larger string with at most hamming distance of d
# BA1H
def approxPatternMatch(pat, s, d):
    k = len(pat)
    occurIndex = []
    for i in range(len(s)-len(pat) - 1):
        if hammingDistance(s[i:i+k], pat) <= d:
            occurIndex.append(i)
    return occurIndex


# # find the most frequent kmer with up to d mismatches
# def freqWordsWMismatch(text, k, d):
#     freqWords = []
#     currMax = 0
#     for i in range(len(text) - k - 1):
#         for j in range(i, len(text) - k - 1):
#             if hammingDistance(s[i:i+k], s[j:j+k]) <= d and s[i:i+k] not in freqWords:
#                 freqWords.append(s[i:i+k])
#     for i in range(len(freqWords)):
#         for j in range(len(freqWords)):
#             if hammingDistance(freqWords[i], freqWords[j]) <= d:
#                 # print freqWords[i], freqWords[j]





# s = 'ACGTTGCATGTCGCATGATGCATGAGAGCT'
# k = 4
# d = 1

# freqWordsWMismatch(s, k, d)

# args = getArgs('1h')
#
# writeList(approxPatternMatch(args[0], args[1], args[2]))




