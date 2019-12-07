# find reverse compliment of a dna section
# first do so by reversing the string and then returning the dna
# compliment of that string
def revStr(s):
    listS = list(s)
    for i in range(len(s)//2):
        temp = listS[i]
        listS[i] = listS[len(s) - 1 - i]
        listS[len(s) - 1 - i] = temp

    return ''.join(listS)

def retComps(s):
  s = revStr(s)
  strDict = {'A':'T', 'C':'G', 'G':'C', 'T':'A'}
  listS = list(s)
  for i in range(len(listS)):
    listS[i] = strDict[listS[i]]

  return ''.join(listS)

# sliding window count occurences of pattern (pat) in string s
def t1a(s, pat):
    count = 0
    for i in range(len(s)-len(pat) + 1):
        if s[i:i+len(pat)] == pat:
            count += 1
    return count

# returns the most frequent kmers in a string s
# this is a brute force method which first computes a count array value at each index of count array
# is the number of times that kmer appears in the string
# then we loop through the count array to find max value/values


# frequent words t1b
# O(|text|^2*k) runtime not very fast
def t1b(s, k):
    freqWords = []
    count = []
    for i in range(len(s)-k + 1):
        pat = s[i:i + k]
        count.append(t1a(s, pat))
    numWords = max(count)
    for i in range(len(count)):
        if count[i] == numWords:
            freqWords.append(s[i:i+k])
    finList = []
    for element in freqWords:
        if element not in finList:
            finList.append(element)

    return finList

# excercise break pg 40
def patternToNumber(s):
    vals = {'A': 0, 'C': 1, 'G': 2, 'T': 3}
    num = 0
    for i in range(len(s)):
        num += vals[s[len(s) - i - 1]] * (4 ** i)
    return num


# takes a given num and returns the corresponding kmer
def numberToPattern(num, k):
    # remainder
    currNum = num
    strVal = []
    vals = {'A': 0, 'C': 1, 'G': 2, 'T': 3}
    valsRev = {0: 'A', 1: 'C', 2: 'G', 3: 'T'}
    added = False
    for i in range(k - 1, -1, -1):
        # in reverse order go through and see what the largest number you can subtract from the currnum is while
        # the currnum remains positive

        # starting at largest num subtract what you can
        for j in range(3, 0, -1):
            if currNum - (j * (4 ** i)) >= 0:
                strVal.append(valsRev[j])
                currNum -= j * (4 ** i)
                # print currNum
                added = True
                break

        # if nothing was added then fill out with A which goes where there is 0
        if not added:
            strVal.append('A')
            added = False
    # fill trailing places with A
    if len(strVal) < k:
        for i in range(k - len(strVal)):
            strVal.append('A')

    finStr = "".join(strVal)
    return finStr

def retSymbolVal(s):
    vals = {'A': 0, 'C': 1, 'G': 2, 'T': 3}
    return vals[s]

def numToSym(s):
    valsRev = {0: 'A', 1: 'C', 2: 'G', 3: 'T'}
    return valsRev[s]




# not done reverse the recursive logic from pattern to num book
def numToPatternRecursive(num, k):
    if k == 1:
        return numToSym(k)
    pref = num / 4
    r = num % 4
    symbol = numToSym(r)
    prefPat = numToPatternRecursive(pref, k-1)
    return prefPat + symbol


print numToPatternRecursive(78, 4)


def patternToNumRecursive(pat):
    if len(pat) == 0:
        return 0
    symbolVal = retSymbolVal(pat[-1])
    pref = pat[:-1]
    return 4 * patternToNumRecursive(pref) + symbolVal



def t1d(s, pat):
    occurList = []

    for i in range(len(s) - len(pat) - 1):
        if s[i:i+len(pat)] == pat:
            occurList.append(i)

            i += len(pat)



    return occurList







def t1k(s, k):
    freqArray = [0] * (4**k)

    for i in range(len(s) - k + 1):
        val = patternToNumRecursive(s[i:i+k])
        freqArray[val] += 1
        # freqArray[patternToNumber(s[i:i+k])] += 1
    return freqArray

def fasterFreqWords(s, k):
    freqArray = t1k(s,k)

    maxArray = []
    maxStrings = []
    currMax = 0

    for i in range(len(freqArray)):

        if freqArray[i] == currMax:

            maxArray.append(numToPatternRecursive(i, k))
    # print maxArray
    for i in range(len(maxArray)):
        maxStrings.append(numToPatternRecursive(maxArray[i], k))
    return maxStrings



s = 'ACGTTGCATGTCGCATGATGCATGAGAGCT'
k = 4

# print t1b(s, k)

# print numToPatternRecursive(78, 4)

print fasterFreqWords(s, k)


# def writeList(list):
#     f = open('myfile.txt', 'w')
#     for x in list:
#         f.write('%s ' %x)


# print fasterFreqWords('ACGTTGCATGTCGCATGATGCATGAGAGCT', 4)
s = 'ACATCTGACACCCAGAATAAGGGAGAACGAATGACGTGACCGAGGAGTAGACATAGTACTGTCTAGGTTATACTTGCACACAGTCGTGTCCAGTCTAGTCTACGAGATTCCTGTGGGTTTTACATGTGATCGCTATTCTCGTCCTGTTTGCCAAAAGGTAACGTCGGCTGGCTGGAGCAGAACGGTGAAAACTTAGAAGGTGTGAGTAGATAAATTTGGGGCCGAGTTAGTTTCATACGCTTCGTGCTTACCCACCCGTGATATCTATAATTGACGGTCCTAGACACGTTGCAGGGTGCCCACCAAAAGCAAGGCAGTGAAGGGTTGCCGAAACCGTACACTCCGATTGGAGCTTGGACCTAGAAGGTACCGGCCGGACGCCTAACGGATTCGTATGAATCTGAAGCGGCTAGTGCCGGTTCTCGGAACGTTAAGACGAGGGTCATGAGAGCACCTGCTAGGTTTAGTCACATAGCTCCCTGCGACGAGGTTAGGTACGTCCCGATTATGCAAGTCGCCCCTTTCGAACATTAGAACTGGCTTTAGATTTGCTACCCGTAATACAACACTCACCCGGCATCTAATATACTTACATAATACAGAGTGGA'
k = 7

# writeList(t1k(s, k))