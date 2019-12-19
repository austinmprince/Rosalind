from chapter1 import neighbors, patternMatching


def motifEnumeration(dna, k, d):
    patterns = []
    for i in range(len(dna[0])-k+1):
        currPattern = dna[0][i:i+k]
        neighborhood = neighbors.neighbors(currPattern, d)


