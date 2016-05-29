import pickle
import json

# Create a new file in local dir
newFile = open('data.html', 'w')
newFile.write('Hello\n')
newFile.write('World!\n')
newFile.close()

# Read a file from local dir
newFile = open('data.html')
text = newFile.read().split()                                   # create a list of each obj

# Convert obj to string and wright to file
X, Y, Z = 43, 44, 45
S = 'Spam'
D = {'a': 1, 'b': 2}
L = [1, 2, 3, 4]
createFile = open('dataFile.txt', 'w')
createFile.write(S + '\n')
createFile.write('%s, %s, %s\n' % (X, Y, Z))
createFile.write(str(L) + '$' + str(D) + '\n')
createFile.close()

# Read each line of file and convert string to obj
fileToOpen = open('dataFile.txt')
line = fileToOpen.readline().rstrip()

line = fileToOpen.readline().split(',')                         # string to integers
numbers = [int(P) for P in line]

line = fileToOpen.readline()
parts = line.split('$')                                         # string to list / obj
objects = [eval(P) for P in parts]

# Object serialization - string of bytes
dictionary = {'a': 1, 'b': 2}
fileName = open('dataFile.txt', 'wb')                           # save obj to the file
pickle.dump(dictionary, fileName)
fileName.close()

fileName = open('dataFile.txt', 'rb')
importedDict = pickle.load(fileName)                            # read obj from the file

# Object serialization - json format
rec = dict(name='Sergey', job=['dev', 'mng'], age=34)
output = json.dump(rec, fp=open('json.txt', 'w'), indent=4)     # export obj to json file

readJson = json.load(open('json.txt'))                          # import json from file
