from chapter1.neighbors import neighbors, iterativeNeighbors

count = 0
baseString = ''
numPerms = 0
permList = []
with open('neighbors.txt', 'r') as f:
    line = f.readlines()
    for i in range(len(line)):

        if i == 1:
            baseString = line[i][:-1]
        elif i == 2:
            numPerms = int(line[i][:-1])
        elif i == len(line) - 1:

            permList.append(line[i])
        elif i > 3:
            permList.append(line[i][:-1])


print baseString, numPerms

neigh = iterativeNeighbors(baseString, numPerms)
neighRecursive = neighbors(baseString, numPerms)
print len(neighRecursive)
print len(permList)

print sorted(neighRecursive) == sorted(permList)
# neigh = neighbors('ATCGG', 3)
# print list(set(permList) - set(neigh))
# permList = sorted(permList)
# neigh = sorted(neigh)
# print len(permList)



list = []
for i in range(len(neigh)):
    if neigh[i] == permList[i]:
        list.append(True)






