import numpy as np
import pandas as pd

# Remove duplicate lines from log.txt
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

beers = open("log.txt", "r")
guests = open("guests.log", "w")
hosts = open("hosts.log", "w")

text1 = (": I can do ", ": My yard is available ", " at ")  # Excess text
rep = (",", ",", ",")

# Read log and distinguish between guests (All) and hosts (Yard owners)
# Remove excess text and replace it with commas

for line in beers:
    if text1[1] in line:
        for txt1, repl in zip(text1, rep):
            line = line.replace(txt1, repl)
        hosts.write(line)
        guests.write(line)  # Hosts are also guests, obviously
    else:
        for txt1, repl in zip(text1, rep):
            line = line.replace(txt1, repl)
        guests.write(line)

beers.close()
guests.close()
hosts.close()

yards = pd.read_csv('hosts.log')
yards.columns = ['Name', 'Day', 'Time']
people = pd.read_csv("guests.log")
people.columns = ['Name', 'Day', 'Time']

"""
shem = sorted(yards.Name.unique())
yom = sorted(yards.Day.unique())
sha = sorted(yards.Time.unique())
"""

shem = yards.Name.unique()
yom = yards.Day.unique()
sha = yards.Time.unique()

# print(shem, '\n', yom, '\n', sha)

print(shem)
print(yards.Name.count())
print(type(shem))

shem = np.delete(shem, np.where(shem == 'Gil'))
print(shem)

# print(yards.Day + yards.Time)

while shem.any():
    for y in yards:
        for p in people:
            if p == y:
                continue
#            elif (y.Day + y.Time) == (p.Day + p.Time):

with open("hosts.log", "r") as hosts_check:
    while hosts_check.readline():
        with open("guests.log", "r") as guests_check:
            while guests_check.readline():
                name = guests_check.readline()
                # print(guests_check.readline().split(","))
                # print(name)
