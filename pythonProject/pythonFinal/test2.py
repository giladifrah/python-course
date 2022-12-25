import pandas as pd

beers = open("log.txt", "r")
guests = open("guests.log", "w")
hosts = open("hosts.log", "w")

text1 = (": I can do ", ": My yard is available ", " at ")
rep = (",", ",", ",")

for line in beers:
    if text1[1] in line:
        for txt1, repl in zip(text1, rep):
            line = line.replace(txt1, repl)
        hosts.write(line)
        guests.write(line)
    else:
        for txt1, repl in zip(text1, rep):
            line = line.replace(txt1, repl)
        guests.write(line)

beers.close()
guests.close()
hosts.close()

df = pd.read_csv('guests.log')
df.columns = ['Name', 'Day', 'Time']

shem = sorted(df.Name.unique())
yom = sorted(df.Day.unique())
sha = sorted(df.Time.unique())

# perfecttime = pd.unique(df[['Name']].values.ravel('k'))
# perfecttime = pd.unique(df[['Name', 'Day', 'Time']].values.ravel('k'))

print(shem, '\n', yom, '\n', sha)

print(shem[2])
