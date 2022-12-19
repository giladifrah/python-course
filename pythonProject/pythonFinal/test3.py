
beers = open("log1.txt", "r")
guests = open("guests.log", "w")
hosts = open("hosts.log", "w")
my_dict = {}

text1 = (": I can do ", ": My yard is available ", " at ")
rep = (",", ",", ",")

# Read log and distinguish between guests (All) and hosts (Yard owners)

for line in beers:
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
