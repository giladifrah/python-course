import pandas as pd
# import numpy as np

beers = open("log1.txt", "r")
guests = open("guests.log", "w")
hosts = open("hosts.log", "w")
my_dict = {}

text1 = (": I can do ", ": My yard is available ", " at ")
rep = (",", ",", ",")
entries = 0

for line in beers:
    entries += 1
    if text1[1] in line:
        for txt1, repl in zip(text1, rep):
            line = line.replace(txt1, repl)
        hosts.write(line)
        guests.write(line)
        # my_dict.update({line})
    else:
        for txt1, repl in zip(text1, rep):
            line = line.replace(txt1, repl)
        guests.write(line)

beers.close()
guests.close()
hosts.close()

df = pd.read_csv('guests.log')
df.columns = ['Name', 'Day', 'Time']

shem = df.Name.unique()
yom = df.Day.unique()
sha = df.Time.unique()

# perfecttime = pd.unique(df[['Name', 'Day', 'Time']].values.ravel('k'))

# print(shem, '\n', yom, '\n', sha)
# print(entries)
# print(len(shem))

print(entries)

# print(line)
