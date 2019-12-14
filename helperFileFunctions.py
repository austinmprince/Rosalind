import os


# this function is a helper function that looks in the downloads folder and finds the data that we
# are looking for the problem
# returns a list of arguments in an array and requires the user to know the input and pass it into the function
# correctly
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




# writes a list of outputs to a text file 'myfile.txt'
# If you think your logic is correct then look to see if you should change the \n to something else
# or if there are extra spaces that could make the format incorrect
def writeList(list):
    f = open('myfile.txt', 'w')
    for x in list:
        f.write('\n%s' %x)

