from patternMatching import hammingDistance
from helperFileFunctions import *
from math import factorial

# this function generates the immediate neighbors of a string it does this by initializing the list
# to contain only the original pattern it then goes through and replaces each index with every possible base pair
# that is not the current base pair
def generateImmediateNeighborhood(patt):
    pattList = list(patt)
    neighborhood = [patt]
    nucleotides = ['A', 'C', 'G', 'T']
    for i in range(len(pattList)):
        for x in range(len(nucleotides)):
            if pattList[i] is not nucleotides[x]:
                oldVal = pattList[i]
                pattList[i] = nucleotides[x]
                s = ""
                neighborhood.append(s.join(pattList))
                pattList[i] = oldVal

    return neighborhood

# BA1N on Rosalind
# Generates the d neighborhood of a string can be used to find most frequent words with a minimum number of mismatches
def neighbors(patt, d):
    if d == 0:
        return patt
    if len(patt) == 1:
        return ['A','T','C','G']
    neighborhood = []
    bases = ['A', 'C', 'T', 'G']
    suffixNeighbors = neighbors(patt[1:], d)
    for text in suffixNeighbors:

        if hammingDistance(patt[1:], text) < d:
            for base in bases:
                perm = base + text

                neighborhood.append(perm)
        else:
            perm = patt[0] + text
            neighborhood.append(perm)

    return neighborhood


def nCr(n, r):
    topFact = factorial(n)
    bottomFact = factorial(r) * factorial(n - r)

    combVal = topFact / bottomFact
    return combVal

# gets the number of d-neighbors a string should have
# figured this out to check my answer
# equals sum(1, d) C(len(str), i) * 3 ^ i
# look at notes to figure out why
def getCombinations(strLen, d):
    sum = 1
    for i in range(1, d + 1):
        combos = nCr(strLen, i)
        sum += combos * (3 ** i)
    return sum




# args = getArgs('1n', 15)
#
#
# neigh2 = neighbors(args[0], args[1])
#
# writeList(neigh2)
# print len(neigh2)



