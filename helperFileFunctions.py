import os



def getArgs(exnum, attempt = None):
    cur_path = os.path.dirname(__file__)
    exName = 'rosalind_ba' + exnum + '.txt'
    if attempt is not None:
        exName = 'rosalind_ba' + exnum + ' (' + str(attempt) + ')' + '.txt'
    filePath = os.path.join( os.getcwd(), '..', '..', '..', 'Downloads',  exName )

    args = []
    new_path = os.path.relpath(filePath, cur_path)

    with open(new_path, 'r') as f:
        line = f.readlines()
        for i in range(len(line)):
            val = line[i][:-1]
            if val.isdigit():
                args.append(int(val))
            else:
                args.append(val)


    return args





def writeList(list):
    f = open('myfile.txt', 'w')
    for x in list:
        f.write('%s ' %x)

