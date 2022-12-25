# Compares all lines in a given file and removes duplicates.

# import time as t

# def get_time():
#    return t.strftime('%H:%M:%S')

fileName = 'log.txt'
with open(fileName, 'r') as f:
    file = f.readlines()

wordList = []
badList = []

for line in file:
    if line in wordList:
        badList.append(line)
    else:
        wordList.append(line)

file = open(fileName, 'w')

for line in wordList:
    file.write(line)

file.close()

print('Result: {0} duplicate lines removed from {1}.'.format(len(badList), fileName))

# print('[{0}]: {1} duplicate lines removed from {2}.'.format(get_time(), len(badList), fileName))
